from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class UserRole(BaseModel):
    __tablename__ = 'user_role'
    user_id = Column(ForeignKey("user.id"), nullable=False)
    role_id = Column(ForeignKey("role.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
