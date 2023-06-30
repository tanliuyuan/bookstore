from sqlalchemy import Column, Text, Integer

from .base import BaseModel


class Log(BaseModel):
    __tablename__ = 'log'
    request = Column(Text)
    response = Column(Text)
    status_code = Column(Integer)
