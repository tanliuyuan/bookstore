from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.user_role import UserRole
from .user import UserSchema
from .role import RoleSchema


class UserRoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserRole
        load_instance = True
    
    user = fields.Nested(UserSchema, dump_only=True)
    role = fields.Nested(RoleSchema, dump_only=True) 