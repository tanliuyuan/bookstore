from sqlalchemy import Column, FetchedValue, Integer, String, DateTime, text, func
from main import db


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = ({
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci'
    })

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    uuid = Column(
        String(36),
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=FetchedValue()
    )
