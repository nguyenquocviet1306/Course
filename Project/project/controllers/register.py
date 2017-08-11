import logging

from authkit.authorize.pylons_adaptors import authorize
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict

from project.model.meta import Session
import project.model as model
import project.lib.helpers as h
import formencode

from project.lib.base import BaseController, render_jinja2

log = logging.getLogger(__name__)

class RegisterController(BaseController):

    #@authorize(h.auth.is_valid_user)
    @restrict('POST')
    def create(self):
        student = Session.query(model.Users).filter_by(email=request.environ['REMOTE_USER']).first()
        print (request.environ['REMOTE_USER'])
        print ("Email la : ")
        print (student)
        course_id = request.params['code']
        course = Session.query(model.Course).filter_by(code = course_id).first()
        if not course:
            abort(404, '404 Course Not Found')
        register = Session.query(model.association_table).filter_by(user_id=student.id,
                                                                    course_id=course_id).first()
        if register:
            print ('Da dang ki tu truoc')
        else:
            student.courses.append(course)
            Session.commit()
            print ('Dang ki thanh cong')