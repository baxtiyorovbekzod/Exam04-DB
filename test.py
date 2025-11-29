from datetime import datetime
from library.create_tables import init_db
from library.services import (
    create_author, 
    get_author_by_id
    , get_all_authors
    , update_author, 
    delete_author,
    create_book,
    get_book_by_id,
      get_all_books,
        search_books_by_title,
          delete_book,
    create_student, get_student_by_id, get_all_students, update_student_grade,
    borrow_book, return_book, get_currently_borrowed_books
)


init_db()





# author = create_author(name='ok', bio='yaxshi')



# author_fetched = get_author_by_id(1)
# print("ID bo'yicha muallif:", author_fetched.name if author_fetched else None)

# updated_author = update_author(1, 'lm', "qarada")
# print("Yangilangan bio:", updated_author.bio if updated_author else None)








# book = create_book('J.K. Rowling', author_id=1, published_year=2020, isbn='1234567890133')

# book_fetched = get_book_by_id(1)
# print("ID bo'yicha kitob:", book_fetched.title if book_fetched else None)

# results = search_books_by_title("10")
# print("Qidiruv natijasi:", [b.title for b in results])






# student = create_student("bekzod", "bek@mail.com", "11-b")


# student_fetched = get_student_by_id(3)
# print("ID bo'yicha talaba:", student_fetched.full_name if student_fetched else None)

# updated_student = update_student_grade(1, "11-B")
# print("Yangilangan sinf:", updated_student.grade if updated_student else None)



