import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    Id = Column(Integer, primary_key=True)
    Username = Column(String(55), nullable=False)
    Email = Column(String(55),nullable=False)
    Comment_id = Column(Integer,ForeignKey('comment.id'))

class Post(Base):
    __tablename__ = 'post'
    Id = Column(Integer, primary_key=True)
    Caption = Column(String(600), nullable=False)
    Likes = Column(Integer)
    User_id = Column(Integer, ForeignKey('user.id'))


class Media (Base):
    __tablename__= 'media'
    Id = Column(Integer, primary_key=True)
    Type = Column(String(250),nullable=False)
    Post_Id = Column(Integer, ForeignKey('post.id'))

class Comment (Base):
    __tablename__= 'comment'
    Id = Column(Integer, primary_key=True)
    Text = Column(String(250),nullable=False)
    Post_Id = Column(Integer, ForeignKey('post.id'))
    User_id = Column(Integer, ForeignKey('user.id'))

class Favorite (Base):
    __tablename__= 'favorite'
    Id = Column(Integer, primary_key=True)
    Post_Id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e