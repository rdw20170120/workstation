# CherryPy helper

import cherrypy

class CherryPy(object):
    @classmethod
    def set_content_type(cls, content_type):
        cherrypy.response.headers['Content-Type'] = content_type
