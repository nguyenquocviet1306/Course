import logging

import formencode
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict

import project.lib.helpers as h
from formencode import htmlfill
from pylons.decorators import validate
from project.model import *
from array import array
from flask import Flask
# from flask import Flask, flash, redirect, render_template, request, session, abort
import os

from project.lib.base import BaseController, render_jinja2

log = logging.getLogger(__name__)

class NewFormStudent(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    password = formencode.validators.ByteString(not_empty=True)
    email = formencode.validators.Email(not_empty=True)

class StudentsController(BaseController):
    def index(self):
        # Return a rendered template
        # return render('/students.mako')
        # or, return a string
        return render_jinja2('/layout/index.html')

    @restrict('POST')
    @validate(schema=NewFormStudent(), form='new')
    def create(self):
        email = request.params['email']
        password = request.params['password']
        groupid = 2
        a = Users()
        a.email = email
        a.password = password
        a.group_id = groupid
        Session.add(a)
        Session.commit()
        return "OK"

    def new(self):
        return render_jinja2('/students/new.html')

    def showlist(self):
        c.title = 'Show Student'

        c.studentall = Session.query(Users).all()

        return render_jinja2('/students/list.html')

    def show(self, id, format='html'):
        c.student = Session.query(Users).filter_by(id = id).first()
        if not c.student:
            abort(404, '404 Not Found')
        c.student_courses = Session.query(association_table).filter_by(user_id=c.student.id).all()
        print (c.student_courses)
        print ("AAAAAAA")
        print (c.student.courses)

        #course = Course()
        #c.array1 = []
        #for item in c.student_courses:
         #   c.array1.append( Session.query(Course).filter_by(id = item.course_id).all())

        # print (c.array1)
        #for course in c.array1:
         #   print (course.id)
        return render_jinja2('/students/show_item.html')

    def edit(self,id = None):
        if id is None:
            abort(404)
        student_q = Session.query(Users)
        student = student_q.filter_by(id=id).first()
        if student is None:
            abort(404)
        values = {
                'name': student.name,
                'password': student.password,
                'email': student.email
            }

        return htmlfill.render(render_jinja2('/students/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewFormStudent(), form='edit')
    def save(self, id=None):
        student_q = meta.Session.query(Users)
        student = student_q.filter_by(id=id).first()
        if student is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(student, k) != v:
                setattr(student, k, v)
        meta.Session.commit()
        session['flash'] = 'Page successfully updated.'
        session.save()
        return "Moved temporarily"






