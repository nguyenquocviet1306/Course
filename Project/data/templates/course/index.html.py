# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501658908.280761
_enable_loop = True
_template_filename = '/home/vietnguyen/PycharmProjects/Project/project/templates/course/index.html'
_template_uri = '/course/index.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>Title</title>\n    <link rel="stylesheet" href="/static/css/bootstrap.css" />\n     <link rel="stylesheet" href="/static/css/bootstrap-theme.css"/>\n</head>\n<body>\n<div class="page-header">\n  <h1> \u0110\u0103ng k\xfd th\xe0nh vi\xean </h1>\n</div>\n\n<div class="input-group input-group-lg">\n  <span class="input-group-addon">@</span>\n  <input type="text" class="form-control" placeholder="Username">\n</div>\n\n<div class="input-group input-group-lg">\n  <span class="input-group-addon">@</span>\n  <input type="text" class="form-control" placeholder="Password">\n</div>\n\n<div class="input-group input-group-lg">\n  <span class="input-group-addon">@</span>\n  <input type="text" class="form-control" placeholder="MSSV">\n</div>\n\n<button type="button" class="btn btn-default">\u0110\u0103ng k</button>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/course/index.html", "filename": "/home/vietnguyen/PycharmProjects/Project/project/templates/course/index.html"}
__M_END_METADATA
"""
