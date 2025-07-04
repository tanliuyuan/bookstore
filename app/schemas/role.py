from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.role import Role


class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True 