from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from project.model.meta import Base

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    code = Column(String(100))

    def __init__(self,name='',code=''):
        self.name = name
        self.code = code

    def __repr__(self):
        return "<Course('%s')" % self.name