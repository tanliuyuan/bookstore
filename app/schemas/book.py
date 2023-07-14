from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.book import Book

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book