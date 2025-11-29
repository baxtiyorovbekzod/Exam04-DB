from datetime import datetime
from sqlalchemy import(
    Column, String, Boolean, Float, Integer, Date, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .db import Base, get_db


class Author(Base):
    __tablename__ = 'authors'

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(length=100), nullable=False)
    bio = Column('bio', Text, nullable=True)

    created_at = Column('created_at', DateTime, default=datetime.now)

    books = relationship('Book', back_populates='author')

    def __str__(self):
        return f'Author(id={self.id}, name="{self.name} {self.bio}")'

    def __repr__(self):
        return f'Author(id={self.id}, name="{self.name} {self.bio}")'


class Book(Base):
    __tablename__ = 'books'

    id = Column('id', Integer, primary_key= True)
    title = Column('title', String(length=200), nullable=False)
    author_id = Column('author_id', ForeignKey('authors.id', ondelete='CASCADE'))
    published_year = Column('published_year', Integer)
    isbn = Column('isbn', String(length=13), unique=True)
    is_available = Column('is_available', Boolean, default=True)

    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    author = relationship('Author', back_populates='books')
    borrows = relationship('Borrow', back_populates='book')

    def __str__(self):
        return f'Book(id={self.id}, name="{self.title} {self.author_id}")'

    def __repr__(self):
        return f'Book(id={self.id}, name="{self.title} {self.author_id}")'


class Student(Base):
    __tablename__ = 'students'

    id = Column('id', Integer, primary_key=True)
    full_name = Column('full_name', String(length=150), nullable=False)
    email = Column('email', String(length=100), nullable=False)
    grade = Column('grade', String(20))
    registered_at = Column('registered_at', DateTime, default=datetime.now)

    borrows = relationship('Borrow', back_populates='student')
    
    def __str__(self):
        return f'Student (id={self.id}, name="{self.full_name} {self.email}")'

    def __repr__(self):
         return f'Student (id={self.id}, name="{self.full_name} {self.email}")'


class Borrow(Base):
    __tablename__ = 'borrows'

    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    book_id = Column('book_id', ForeignKey('books.id', ondelete='CASCADE'))
    borrowed_at = Column('borrowed_at', DateTime, default=datetime.now)
    due_date = Column('due_date', DateTime, default=datetime.now)
    returned_at = Column('returned_at', DateTime, default=datetime.now, nullable=False)

    student = relationship("Student", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")


    
    def __str__(self):
        return f'Borrow (id={self.id}, name="{self.student_id} {self.book_id}")'

    def __repr__(self):
        return f'Borrow (id={self.id}, name="{self.student_id} {self.book_id}")'