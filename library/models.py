
from datetime import datetime 
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, Text, Float, ForeignKey, Boolean
)
from sqlalchemy.orm import relationship
from .db import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column( 'id', Integer, primary_key=True)
    name = Column('name', String(100), nullable=False)
    bio = Column('bio', String, nullable=True)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)

   
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column('id' ,Integer, primary_key=True)
    title = Column('title',String(200), nullable=False)
    author_id = Column('author_id',Integer, ForeignKey("authors.id"))
    published_year = Column('published_year',Integer)
    isbn = Column("isbn",String(13), unique=True)
    is_available = Column('is_available',Boolean, default=True)

    created_at = Column('created_at',DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    
    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")

class Student(Base):
    __tablename__ = "students"

    id = Column('id',Integer, primary_key=True)
    full_name = Column('full_name',String(150), nullable=False)
    email = Column('email',String(100), nullable=False, unique=True)
    grade = Column('grade',String(20), nullable=True)
    registered_at = Column('registered_at',DateTime, default=datetime.utcnow)

    
    borrows = relationship("Borrow", back_populates="student")

class Borrow(Base):
    __tablename__ = "borrows"

    id = Column('id',Integer, primary_key=True)

    student_id = Column('student_id',Integer, ForeignKey("students.id"))
    book_id = Column('book_id',Integer, ForeignKey("books.id"))

    borrowed_at = Column('borrowed_at',DateTime, default=datetime.utcnow)
    due_date = Column('due_date',DateTime, default=datetime.utcnow)
    returned_at = Column('returned_at',DateTime, nullable=True)

 
    student = relationship("Student", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")        