import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import formencode
import project.lib.helpers as h
from project.lib.base import BaseController, render
from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import ValidAuthKitUser
from project.model import meta
import project.model as model
from project.model import *
from project.lib.base import BaseController, render_jinja2

log = logging.getLogger(__name__)


class LoginForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    password = formencode.validators.ByteString(not_empty=True)

class AccountController(BaseController):

    def signin(self):
        if not h.auth.authorized(h.auth.is_valid_user):
            print ("chua dang nhap")
            if request.params:
                print ("vao day khong nhi ")
                user = Session.query(model.Users). \
                    filter_by(email=request.params['email'],
                              password=request.params['password']). \
                    first()
                if user:
                    print ("dang nhap roi")
                    session['user'] = user
                    session.save()
                    print (user)
                else:
                    return render_jinja2('/account/singin.html')
            else:
                print ("vao 1")
                return render_jinja2('/account/singin.html')
        else:
            print ("vao 2")
            user_group = Session.query(Users).filter_by(email=request.environ['REMOTE_USER']).first()
            print ("AABBBB")
            print (user_group.email == 'admin@gmail.com')
            if (user_group.email == 'admin@gmail.com'):
                return redirect(h.url('signedin'))
                #return redirect(url(controller='courses', action='index'))
            else :
                return redirect(url(controller='students', action='show', id = user_group.id))

    @authorize(ValidAuthKitUser())
    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        del session['user']
        session.delete()
        return render_jinja2('/account/singout.html')

    @authorize(ValidAuthKitUser())
    def signedin(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        # print(1)
        # print(authorize(h.auth.has_auth_kit_role('admin')))
        #print (student_group_id)
        redirect(url(controller='courses', action='index'))

