from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from portfolio.db import Base, db_session
from portfolio.utils import slugify

association_table = Table('assoc_article_category', Base.metadata,
    Column('category_id', Integer, ForeignKey('category.id')),
    Column('article_id', Integer, ForeignKey('article.id'))
)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False, nullable=False)
    slug = Column(String(50), unique=False, nullable=False)
    content = Column(Text, unique=False, nullable=False)
    published = Column(Text, unique=False, nullable=False)
    publishDate = Column(Integer, unique=False, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    categories = relationship(
        "Category",
        secondary=association_table,
        back_populates="articles")

    def __init__(self, title=None, content=None, user_id=None, slug=None, published=0):
        self.title = title
        if slug is None:
            self.slug = slugify(self.title)
        else:
            self.slug = slug
        endif
        self.content = content
        self.user_id = user_id
        self.published = published

    def __repr__(self):
        return '<Article %r>' % (self.title)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)

    articles = relationship(
        "Article",
        secondary=association_table,
        back_populates="categories")

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)
