# Controller (MVC pattern) for the home page

import cherrypy

from sandbox.web.cherrypy_3_1_2 import CherryPy
from sandbox.web.xhtml_1_0_strict import Renderer
import sandbox.web.view.home

class Home(object):
    @cherrypy.expose
    def index(self):
        renderer = Renderer()
        CherryPy.set_content_type(renderer.content_type())
        view = sandbox.web.view.home.View(
            renderer,
            cherrypy.response.time,
        )
        return view.page()
