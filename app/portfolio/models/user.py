from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from portfolio.db import Base, db_session

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(250), unique=False, nullable=False)
    permission = Column(Integer, unique=False, nullable=False)
    register = Column(Integer, unique=False, nullable=True)
    lastLogin = Column(Integer, unique=False, nullable=True)
    article = relationship('Article', backref='user', lazy=True)

    def __init__(self, name=None, email=None, password=None, permission=-1):
        self.name = name
        self.email = email
        self.password = password
        self.permission = permission

    def __repr__(self):
        return '<User %r>' % (self.name)

    def save(self):
        if self.name == None:
            return 'empty_name'
        elif self.email == None:
            return 'empty_email'
        elif self.password == None:
            return 'empty_password'
        elif User.query.filter_by(name=self.name).first() is not None:
            return 'user_exist'

        db_session.add(self)
        return db_session.commit()
