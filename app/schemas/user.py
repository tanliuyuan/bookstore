from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.user import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
    
    full_name = fields.Method("get_full_name")
    
    def get_full_name(self, obj):
        return obj.full_name 