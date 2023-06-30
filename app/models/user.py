from sqlalchemy import Column, String

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
