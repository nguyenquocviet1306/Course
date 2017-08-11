# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501820811.626155
_enable_loop = True
_template_filename = '/home/vietnguyen/PycharmProjects/Project/project/templates/course/addcourse.html'
_template_uri = '/course/addcourse.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<link rel="stylesheet" href="/static/css/bootstrap.css"/>\n<link rel="stylesheet" href="/stactic/css/bootstrap-theme.css"/>\n{{h.form(h.url(controller=\'courses\', action=\'create\'), method="post")}}\n<div class="page-header">\n    <h1> Add Course </h1>\n</div>\n<div class="col-md-6">\n<form role="form">\n    <div class="form-group">\n    <label for="course">Course \'s name :  </label>\n    <input type="text" class="form-control" id="course" placeholder="Enter course \'s name" name="name">\n  </div>\n  <div class="form-group">\n    <label for="email">Course \'s code : </label>\n    <input type="text" class="form-control" id="email" placeholder="Enter course \'s code" name="code" >\n  </div>\n\n  <button type="submit" class="btn btn-default">Add</button>\n</form>\n</div>\n{{h.end_form()}}')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/course/addcourse.html", "filename": "/home/vietnguyen/PycharmProjects/Project/project/templates/course/addcourse.html"}
__M_END_METADATA
"""
