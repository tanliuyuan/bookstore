from flask import Blueprint

from app.models import db
from app.models.book import Book
from app.schemas.book import BookSchema


bp = Blueprint('book', __name__, url_prefix='/v1/books')


@bp.route('', methods=['GET'])
def get_all(page: int = 1, per_page: int = 10):
    books = db.paginate(db.select(Book), page=page, per_page=per_page)
    return BookSchema().dump(books, many=True)


@bp.route('/<string:uuid>', methods=['GET'])
def get_one(uuid: str):
    book = Book.query.filter(Book.uuid == uuid).one_or_404()
    return BookSchema().dump(book)
