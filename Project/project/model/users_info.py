from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from project.model.meta import Base
from sqlalchemy.orm import *


class UsersInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.uid'))
    name = Column(String(100))
    avatar = Column(String(100))
<<<<<<< HEAD
    token = Column(String(100))
    active = Column(Integer)
=======
>>>>>>> c080db6552c22b175d87a4973cb1a84173fb9f97

    user = relationship("Users",
                    backref=backref("user_info", uselist=False))

<<<<<<< HEAD
    def __init__(self, name='', avatar='',active='',token=''):
        self.name = name
        self.avatar = avatar
        self.active = 0
        self.token = token
=======
    def __init__(self, name='', avatar=''):
        self.name = name
        self.avatar = avatar

>>>>>>> c080db6552c22b175d87a4973cb1a84173fb9f97
    def __repr__(self):
        return "<User_Info('%s')" % self.name