from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.models.book import Book
from app.schemas.book import BookSchema


bp = Blueprint('book', __name__, url_prefix='/v1/books')
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@bp.route('', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    books = db.paginate(
        db.select(Book).order_by(Book.created_at.desc()), 
        page=page, 
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'books': books_schema.dump(books.items),
        'pagination': {
            'page': books.page,
            'pages': books.pages,
            'per_page': books.per_page,
            'total': books.total,
            'has_next': books.has_next,
            'has_prev': books.has_prev
        }
    })


@bp.route('/<string:uuid>', methods=['GET'])
def get_one(uuid: str):
    book = Book.query.filter(Book.uuid == uuid).first_or_404()
    return jsonify(book_schema.dump(book))


@bp.route('', methods=['POST'])
def create():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        book = book_schema.load(data, session=db.session)
        db.session.add(book)
        db.session.commit()
        
        return jsonify(book_schema.dump(book)), 201
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Book with this ISBN already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['PUT'])
def update(uuid: str):
    try:
        book = Book.query.filter(Book.uuid == uuid).first_or_404()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        for field in ['title', 'author', 'isbn']:
            if field in data:
                setattr(book, field, data[field])
        
        db.session.commit()
        return jsonify(book_schema.dump(book))
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Book with this ISBN already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['DELETE'])
def delete(uuid: str):
    try:
        book = Book.query.filter(Book.uuid == uuid).first_or_404()
        db.session.delete(book)
        db.session.commit()
        
        return jsonify({'message': 'Book deleted successfully'}), 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
