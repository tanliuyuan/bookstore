from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.models.user import User
from app.schemas.user import UserSchema


bp = Blueprint('user', __name__, url_prefix='/v1/users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@bp.route('', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    users = db.paginate(
        db.select(User).order_by(User.created_at.desc()), 
        page=page, 
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'users': users_schema.dump(users.items),
        'pagination': {
            'page': users.page,
            'pages': users.pages,
            'per_page': users.per_page,
            'total': users.total,
            'has_next': users.has_next,
            'has_prev': users.has_prev
        }
    })


@bp.route('/<string:uuid>', methods=['GET'])
def get_one(uuid: str):
    user = User.query.filter(User.uuid == uuid).first_or_404()
    return jsonify(user_schema.dump(user))


@bp.route('', methods=['POST'])
def create():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # Validate required fields
        if not data.get('first_name') or not data.get('last_name'):
            return jsonify({'error': 'First name and last name are required'}), 400
            
        user = user_schema.load(data, session=db.session)
        db.session.add(user)
        db.session.commit()
        
        return jsonify(user_schema.dump(user)), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['PUT'])
def update(uuid: str):
    try:
        user = User.query.filter(User.uuid == uuid).first_or_404()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        for field in ['first_name', 'last_name']:
            if field in data:
                setattr(user, field, data[field])
        
        db.session.commit()
        return jsonify(user_schema.dump(user))
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['DELETE'])
def delete(uuid: str):
    try:
        user = User.query.filter(User.uuid == uuid).first_or_404()
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'message': 'User deleted successfully'}), 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400 