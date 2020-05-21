#!/usr/bin/python2.6
# Run my CherryPy web server

import logging
import os

import cherrypy

import sandbox
import sandbox.cherrypy

from sandbox.web import page

_current_directory = os.path.join(os.getcwd(), os.path.dirname(__file__))

site_config = {
    'global': {
        'log.access_file': os.path.join(_current_directory, 'access.log'),
        'log.error_file': os.path.join(_current_directory, 'error.log'),
        'log.screen': True,
        'request.show_mismatched_params': True,
        'server.environment': 'development',
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'server.thread_pool': 10,
        'tools.decode.on': True,
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8',
        'tools.gzip.on': True,
        'tools.log_headers.on': True,
        'tools.log_tracebacks.on': True,
        'tools.sessions.persistent': False,
    },
}

application_config = {
    '/': {
#        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    },
    '/favicon.ico': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': os.path.join(
            _current_directory, 'favorite.ico'
        ),
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(_current_directory, 'static'),
        'tools.staticdir.match': r'\.(css|gif|html?|ico|jpe?g|js|png|swf)$',
    },
}

if __name__ == '__main__':
    # Prepare the site configuration
    cherrypy.config.update(site_config)

    # Prepare the application configuration
    _app = cherrypy.tree.mount(
        page.Home(),
        '/',
        config=application_config
    )

    # Prepare the web server
    if hasattr(cherrypy.engine, 'signal_handler'):
        # Activate signal handling on Unix
        cherrypy.engine.signal_handler.subscribe()
    if hasattr(cherrypy.engine, 'console_control_handler'):
        # Activate console handling on Windows
        cherrypy.engine.console_control_handler.subscribe()

    # Prepare logging
    _formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    sandbox.override_file_handler_formatter(cherrypy.log.error_log, _formatter)
    sandbox.override_file_handler_formatter(_app.log.error_log, _formatter)
    cherrypy.log.error_log.debug('Starting CherryPy web server...')
    _app.log.error_log.debug('Starting CherryPy application...')

    # Dump CherryPy
    sandbox.write_file(
        os.path.join(_current_directory, 'CherryPy.out'),
        sandbox.cherrypy.dump(),
    )

    # Startup the web server
    cherrypy.engine.start()
    cherrypy.engine.block()
