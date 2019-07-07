from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from portfolio.db import Base, db_session
from portfolio.utils.tools import slugify

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False)
    description = Column(Text, unique=False, nullable=False)
    url = Column(Text, unique=True, nullable=True)
    git = Column(Text, unique=True, nullable=True)
    date = Column(Integer, unique=False, nullable=False)

    def __init__(self, title=None, description=None, date=None):
        self.title = title
        self.description = description
        self.date = date

    def __repr__(self):
        return '<Project %r>' % (self.title)
