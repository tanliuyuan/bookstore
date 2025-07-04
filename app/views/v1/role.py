from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.models import db
from app.models.role import Role
from app.schemas.role import RoleSchema


bp = Blueprint('role', __name__, url_prefix='/v1/roles')
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)


@bp.route('', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)  
    per_page = request.args.get('per_page', 10, type=int)
    
    roles = db.paginate(
        db.select(Role).order_by(Role.created_at.desc()), 
        page=page, 
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'roles': roles_schema.dump(roles.items),
        'pagination': {
            'page': roles.page,
            'pages': roles.pages,
            'per_page': roles.per_page,
            'total': roles.total,
            'has_next': roles.has_next,
            'has_prev': roles.has_prev
        }
    })


@bp.route('/<string:uuid>', methods=['GET'])
def get_one(uuid: str):
    role = Role.query.filter(Role.uuid == uuid).first_or_404()
    return jsonify(role_schema.dump(role))


@bp.route('', methods=['POST'])
def create():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        if not data.get('name'):
            return jsonify({'error': 'Role name is required'}), 400
            
        role = role_schema.load(data, session=db.session)
        db.session.add(role)
        db.session.commit()
        
        return jsonify(role_schema.dump(role)), 201
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Role with this name already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['PUT'])
def update(uuid: str):
    try:
        role = Role.query.filter(Role.uuid == uuid).first_or_404()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        if 'name' in data:
            role.name = data['name']
        
        db.session.commit()
        return jsonify(role_schema.dump(role))
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Role with this name already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/<string:uuid>', methods=['DELETE'])
def delete(uuid: str):
    try:
        role = Role.query.filter(Role.uuid == uuid).first_or_404()
        db.session.delete(role)
        db.session.commit()
        
        return jsonify({'message': 'Role deleted successfully'}), 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400 