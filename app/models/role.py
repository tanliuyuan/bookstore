from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Role(BaseModel):
    __tablename__ = 'role'
    name = Column(String(100), nullable=False, unique=True)
    
    # Relationships
    user_roles = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")
    users = relationship("User", secondary="user_role", back_populates="roles", viewonly=True)
