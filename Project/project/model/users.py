from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from project.model.meta import Base
from sqlalchemy.orm import *

class Users(Base):
    __tablename__ = "users"

    id = Column('uid',Integer, primary_key=True)
    email = Column('username',String(100))
    password = Column('password',String(100))
    group_id = Column('group_uid',Integer)

<<<<<<< HEAD

=======
>>>>>>> c080db6552c22b175d87a4973cb1a84173fb9f97
    courses = relationship("Course",
                           secondary='association',
                           backref="users")


    def __repr__(self):
        return "<User('%s')" % self.email