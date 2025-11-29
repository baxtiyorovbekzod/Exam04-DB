from datetime import date
from library.create_tables import init_db
from library.services import (
    create_author,
    create_book,
    get_all_authors,
    get_all_books,
    get_author_by_id,
    get_book_by_id,
    search_books_by_title,
    delete_author,
    delete_book
)

init_db()


create_author(name="leo", bio="ok")
print("Mualliflar yaratildi.")