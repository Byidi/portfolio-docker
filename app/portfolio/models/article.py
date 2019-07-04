from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from portfolio.db import Base, db_session
from portfolio.utils.tools import slugify

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False)
    slug = Column(String(50), unique=False, nullable=False)
    content = Column(Text, unique=False, nullable=False)
    publishedDate = Column(Integer, unique=False, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, title=None, slug=None, content=None, publishedDate=-1, category_id=None, user_id=None):
        self.title = title
        if slug is None:
            self.slug = slugify(self.title)
        else:
            self.slug = slug
        endif
        self.content = content
        self.publishedDate = publishedDate
        self.category_id = category_id
        self.user_id = user_id

    def __repr__(self):
        return '<Article %r>' % (self.title)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    article = relationship('Article', backref='category', lazy=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)
