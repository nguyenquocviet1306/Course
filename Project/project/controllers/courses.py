import logging

import formencode
from authkit.authorize import authorize
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import project.lib.helpers as h

from project.lib.base import BaseController, render_jinja2
from project.model import *

log = logging.getLogger(__name__)

class NewFormCourse(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    code = formencode.validators.String(not_empty=True)


class CoursesController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/courses.mako')
        # or, return a string
        #return render_jinja2('/course/index.html')
        return render_jinja2('/layout/admin.html')

    def new(self):
        return render_jinja2('/course/addcourse.html')

    @restrict('POST')
    @validate(schema=NewFormCourse(), form='new')
    def create(self):
        name = request.params['name']
        code = request.params['code']
        a = Course()
        a.name = name
        a.code = code
        Session.add(a)
        Session.commit()

    def showlist(self):
        c.title = 'Show Courses'

        c.studentall = Session.query(Course).all()

        return render_jinja2('/course/list.html')

    #@authorize(h.auth.has_delete_role)
    def delete(self, id):
        Session.delete(Session.query(Course).filter(Course.id == id).one())
        Session.commit()
        return redirect(url(controller='courses', action='index'))

    def showlist_item(self):
        student = Session.query(Users).filter_by(email=request.environ['REMOTE_USER']).first()
        c.student_courses = Session.query(association_table).filter(user_id = student.id).all()
        return render_jinja2('/students/show_item.html')