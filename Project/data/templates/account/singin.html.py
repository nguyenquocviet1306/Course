# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1502090077.348385
_enable_loop = True
_template_filename = '/home/vietnguyen/PycharmProjects/Project/project/templates/account/singin.html'
_template_uri = '/account/singin.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div class="row">\n        <div class="col-md-6 col-md-offset-3">\n            <h1 class="text-center">Signin</h1>\n            {{ h.form(h.url(controller=\'account\', action=\'signin\'), method="POST") }}\n                    Email Address: {{h.text(\'email\', class="form-control")}}\n                    Password: {{h.password(\'password\', class="form-control")}}\n                <br>\n                {{h.submit(value="Sign in", name=\'submit\', class="form-control")}}\n            {{h.end_form()}}\n        </div>\n    </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/account/singin.html", "filename": "/home/vietnguyen/PycharmProjects/Project/project/templates/account/singin.html"}
__M_END_METADATA
"""
