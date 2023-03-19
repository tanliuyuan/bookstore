from sqlalchemy import Column, String

from app.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = 'book'
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=True)
    isbn = Column(String(13), nullable=False)
