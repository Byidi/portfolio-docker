from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from portfolio.db import Base, db_session
from portfolio.utils.tools import slugify

class Projet(Base):
    __tablename__ = 'prjoet'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False)
    description = Column(String(50), unique=False, nullable=False)
    date = Column(Integer, unique=False, nullable=False)

    def __init__(self, title=None, description=None, date=None):
        self.title = title
        self.description = description
        self.date = date

    def __repr__(self):
        return '<Projet %r>' % (self.title)
