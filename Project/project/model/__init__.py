"""The application's model objects"""
from project.model.meta import Session, Base

from project.model.users import Users
from project.model.users_info import UsersInfo
from project.model.course import Course
import sqlalchemy as sa
import meta
from sqlalchemy import orm
from sqlalchemy import types

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

association_table = sa.Table('association', Base.metadata,
                                 sa.Column('user_id', sa.types.Integer, sa.ForeignKey('users.uid')),
                                 sa.Column('course_id', sa.types.Integer, sa.ForeignKey('course.id'))
                                 )
