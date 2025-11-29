from datetime import datetime, timedelta
from sqlalchemy import or_, not_
from .models import Author, Book, Student, Borrow
from .db import get_db




def create_author(name: str, bio: str = None) -> Author:
    """Yangi muallif yaratish"""
    author = Author(
        name = name,
        bio = bio,
    )
    
    with get_db() as session:
        session.add(author)
        session.commit()

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""
    with get_db() as session:
        author = session.get(Author, author_id)
        return author

def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    with get_db() as session:
        authors = session.query(Author).all()
        return authors

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            return None
        
        if name:
            author.name = name
        if bio:
            author.bio = bio

        session.commit()
        session.refresh(author)
        return author

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            return False
        
        if author.books:
            return False

        session.delete(author)
        session.commit()
        return True




def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    book = Book(
        title = title,
        author_id = author_id,
        published_year = published_year,
        isbn = isbn
    )

    with get_db() as session:
        session.add(book)
        session.commit()
        

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    with get_db() as session:
        book = session.get(Book, book_id)
        return book

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    with get_db() as session:
        books = session.query(Book).all()
        return books

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    with get_db() as session:
        books = session.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
        return books

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    with get_db() as session:
        book = session.get(Book, book_id)
        if not book:
            return False
        
        session.delete(book)
        session.commit()




def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    student = Student(
        full_name=full_name,
        email=email,
        grade=grade
    )
    with get_db() as session:
        session.add(student)
        session.commit()
        return student

def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    with get_db() as session:
        result = session.get(Student, student_id)
        return result

def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    with get_db() as session:
        return session.query(Student).all()

def update_student_grade(student_id: int, grade: str) -> Student | None:
    with get_db() as session:
        student = session.get(Student, student_id)
        if not student:
            return None
        student.grade = grade
        session.commit()
        session.refresh(student)  
        return student




def borrow_book(student_id: int, book_id: int) -> Borrow | None:
    """
    Talabaga kitob berish
    
    Quyidagilarni tekshirish kerak:
    1. Student va Book mavjudligini
    2. Kitobning is_available=True ekanligini
    3. Talabada 3 tadan ortiq qaytarilmagan kitob yo'qligini yani 3 tagacha kitob borrow qila oladi
    
    Transaction ichida:
    - Borrow yozuvi yaratish
    - Book.is_available = False qilish
    - due_date ni hisoblash (14 kun)
    
    Returns:
        Borrow object yoki None (xatolik bo'lsa)
    """
    with get_db() as session:
        student = session.get(Student, student_id)
        book = session.get(Book, book_id)

        if not student:
            return None
        if not book:
            return None
        if book.is_available == False:
            return None

         
        active_borrows = session.query(Borrow).filter(
            Borrow.student_id == student_id,
            Borrow.returned_at == None
        ).count()
        if active_borrows >= 3:
            return None

        borrowed_at = datetime.now()

   
        due_date = borrowed_at + timedelta(days=14)


        borrow = Borrow(
            student_id=student_id,
            book_id=book_id,
            borrowed_at=borrowed_at,
            due_date=due_date,
            returned_at=None
        )

        book.is_available = True  
        book.is_available = False
        session.add(borrow)
        session.commit()
 #datetime kutubxonasi ichida timedelta degani bor ekan o'sha orqali qildim 14 kunlikni       
def return_book(borrow_id: int) -> bool:

    """
    Kitobni qaytarish
    
    Transaction ichida:
    - Borrow.returned_at ni to'ldirish
    - Book.is_available = True qilish
    
    Returns:
        True (muvaffaqiyatli) yoki False (xatolik)
    """
    with get_db() as session:
        borrow = session.get(Borrow, borrow_id)
        if not borrow:
            return False
        if borrow.returned_at != None:
            return False

        borrow.returned_at = datetime.now()

        book = session.get(Book, borrow.book_id)
        if book != None:
            book.is_available = True

        session.commit()





def get_student_borrow_count(student_id: int) -> int:
    """Talabaning jami olgan kitoblari soni"""
    with get_db() as session:
        count = session.query(Borrow).filter(Borrow.student_id == student_id).count()
        return count            
    
def get_currently_borrowed_books() -> list[tuple[Book, Student, datetime]]:
    """Hozirda band bo'lgan kitoblar va ularni olgan talabalar"""
    with get_db() as session:
        borrows = session.query(Borrow).filter(Borrow.returned_at == None).all()
        result = []
        for borrow in borrows:
            student = session.get(Student, borrow.student_id)
            book = session.get(Book, borrow.book_id)
            result.append((book, student, borrow.borrowed_at))
        return result   
    
def get_books_by_author(author_id: int) -> list[Book]:
    """Muayyan muallifning barcha kitoblari"""
    with get_db() as session:
        books = session.query(Book).filter(Book.author_id == author_id).all()
    return books

def get_overdue_borrows() -> list[tuple[Borrow, Student, Book, int]]:
    """
    Kechikkan kitoblar ro'yxati
    Returns:
    List of tuples: (Borrow, Student, Book, kechikkan_kunlar)
    faqat returned_at=NULL va due_date o'tgan yozuvlar
    """