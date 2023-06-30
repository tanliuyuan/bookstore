from sqlalchemy import Column, ForeignKey

from .base import BaseModel


class UserRole(BaseModel):
    __tablename__ = 'user_role'
    user_id = Column(ForeignKey("user.id"), nullable=False)
    role_id = Column(ForeignKey("role.id"), nullable=False)
