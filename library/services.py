from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Author , Student, Borrow , Book
from .db import get_db

def create_author(name: str, bio: str = None) -> Author:
    """Yangi muallif yaratish"""
    pass

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""
    pass

def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    pass

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    pass

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    pass

def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    pass

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    pass

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    pass

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    pass

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    pass

def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    pass

def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    pass

def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    pass

def update_student_grade(student_id: int, grade: str) -> Student | None:
    """Talaba sinfini yangilash"""
    pass


