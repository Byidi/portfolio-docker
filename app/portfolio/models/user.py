from sqlalchemy import Column, Integer, String
from portfolio.db import Base, db_session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(250), unique=False)
    permission = Column(Integer, unique=False)

    def __init__(self, name=None, email=None, password=None, permission=0):
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
