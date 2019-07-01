from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from portfolio.db import Base, db_session

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False)
    content = Column(Text, unique=False, nullable=False)
    published = Column(Text, unique=False, nullable=False)
    publishDate = Column(Integer, unique=False, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, title=None, content=None, user_id=None, published=0):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.published = published

    def __repr__(self):
        return '<Article %r>' % (self.title)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)

class Article_category(Base):
    __tablename__ = 'article_category'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)
