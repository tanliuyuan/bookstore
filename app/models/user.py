from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    
    # Relationships
    user_roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")
    roles = relationship("Role", secondary="user_role", back_populates="users", viewonly=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
