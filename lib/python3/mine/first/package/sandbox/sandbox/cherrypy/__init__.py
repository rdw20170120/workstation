# Marks a Python package

import logging
import types

import cherrypy

import sandbox
import sandbox.web.page.home

debug = False

''' Dump the object hierarchy rooted at 'cherrypy'.

    This facilitates understanding of the CherryPy web server, its parts, and
    any configured sites, applications, and pages.

    TODO: should modules be dumped, perhaps by adding them to a queue as they
    are encountered, dumping the next from the queue when the previous module
    dump is finished, and starting with putting 'cherrypy' on the module queue?
'''
class CherryPyDumper(object):
    def populate(self):
        self._dump_line('Dump of CherryPy module "cherrypy"...')
        # Start by dumping the contents of the cherrypy module
        self._dump_dir('cherrypy', cherrypy)

    def render(self):
        return sandbox.force_unicode('\n'.join(self._lines))

    def _dedent(self):
        self._level -= 1

    def _dump_attribute(self, parent, name):
        name = sandbox.force_unicode(name)
        attribute = self._getattr(parent, name)
        if attribute is parent:
            self._dump_line('"' + name + '" references self')
        elif name.startswith('__') and name.endswith('__'):
            if debug:
                self._dump_line('"' + name + '": <special>')
        else:
            self._dump_pair(name, attribute)

    def _dump_dir(self, parent_name, parent):
        parent_name = sandbox.force_unicode(parent_name)
        if parent in self._had_dir:
            self._dump_line('object has previously been dumped')
        else:
            self._had_dir.append(parent)
            for name in dir(parent):
                self._dump_attribute(parent, name)

    def _dump_line(self, line):
        line = sandbox.force_unicode(line)
        self._lines.append(
            sandbox.force_unicode(self._indentation * self._level + line)
        )

    def _dump_pair(self, name, value):
        datatype = type(value)
        name = sandbox.force_unicode(name)
        # Handle None values
        if isinstance(value, type(None)):
            self._dump_pair_as_string(name, value, datatype)
        # Handle boolean values
        elif isinstance(value, bool):
            self._dump_pair_as_string(name, value, datatype)
        # Handle textual values
        elif isinstance(value, bytes):
            self._dump_pair_as_quoted_string(name, value, datatype)
        elif isinstance(value, str):
            self._dump_pair_as_quoted_string(name, value, datatype)
        # Handle numeric values
        elif isinstance(value, complex):
            self._dump_pair_as_string(name, value, datatype)
        elif isinstance(value, float):
            self._dump_pair_as_string(name, value, datatype)
        elif isinstance(value, int):
            self._dump_pair_as_string(name, value, datatype)
        elif isinstance(value, int):
            self._dump_pair_as_string(name, value, datatype)
        # Handle other built-in values
#        elif isinstance(value, types.BuiltinFunctionType):
#            self._maybe_dump_pair_as_object_shallow(name, value)
#        elif isinstance(value, types.BuiltinMethodType):
#            self._maybe_dump_pair_as_object_shallow(name, value)
        elif isinstance(value, types.FileType):
            self._dump_pair_as_object_shallow(name, value)
        elif isinstance(value, types.FunctionType):
            self._maybe_dump_pair_as_object_shallow(name, value)
        elif isinstance(value, types.MethodType):
            self._maybe_dump_pair_as_object_shallow(name, value)
        elif isinstance(value, types.ModuleType):
            self._maybe_dump_pair_as_object_shallow(name, value)
        elif isinstance(value, type):
            self._maybe_dump_pair_as_object_shallow(name, value)
        # Handle containers
        elif isinstance(value, dict):
            self._dump_line('"' + name + '": {')
            self._indent()
            for key in list(value.keys()):
                self._dump_pair(str(key), value[key])
            self._dedent()
            self._dump_line('}')
        elif isinstance(value, list):
            self._dump_line('"' + name + '": [')
            self._indent()
            for index, item in enumerate(value):
                self._dump_pair(str(index), item)
            self._dedent()
            self._dump_line(']')
        elif isinstance(value, set):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, tuple):
            self._dump_line('"' + name + '": (')
            self._indent()
            for item in value:
                self._dump_pair(None, item)
            self._dedent()
            self._dump_line(')')
        # Handle internal library values
        elif isinstance(value, logging.FileHandler):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, logging.Formatter):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, logging.Logger):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, logging.Manager):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, logging.PlaceHolder):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, logging.StreamHandler):
            self._dump_pair_as_object_deep(name, value)
        # Handle external library values
        elif isinstance(value, cherrypy._cpchecker.Checker):
            self._dump_pair_as_object_shallow(name, value)
        elif isinstance(value, cherrypy._cplogging.LogManager):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cpserver.Server):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cptools.Tool):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cptools.Toolbox):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cptree.Application):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cptree.Tree):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._cpwsgi.CPWSGIApp):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._GlobalLogManager):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy._Serving):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy.process.plugins.Autoreloader):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy.process.plugins.SignalHandler):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy.process.wspbus._StateEnum):
            self._dump_pair_as_object_deep(name, value)
        elif isinstance(value, cherrypy.process.wspbus.Bus):
            self._dump_pair_as_object_shallow(name, value)
        # Handle application values
        elif isinstance(value, sandbox.web.page.home.Home):
            self._dump_pair_as_object_deep(name, value)
        # Handle unknown values
        else:
            self._dump_pair_as_string(name, value, 'unknown')

    def _dump_pair_as_object_deep(self, name, value):
        self._dump_pair_as_object_shallow(name, value)
        self._indent()
        self._dump_dir(name, value)
        self._dedent()

    def _dump_pair_as_object_shallow(self, name, value):
        self._dump_line(
            '"' + name + '": ' + sandbox.force_unicode(str(value))
        )

    def _dump_pair_as_quoted_string(self, name, value, datatype=None):
        if not isinstance(datatype, str):
            datatype = sandbox.force_unicode(str(datatype))
        self._dump_line(
            '"' + name + '": ' +
            datatype +
            ' "' + sandbox.force_unicode(str(value)) + '"'
        )

    def _dump_pair_as_string(self, name, value, datatype=None):
        if not isinstance(datatype, str):
            datatype = sandbox.force_unicode(str(datatype))
        self._dump_line(
            '"' + name + '": ' +
            datatype + ' ' +
            sandbox.force_unicode(str(value))
        )
        
    def _dump_pair_as_type(self, name, value):
        self._dump_line(
            '"' + name + '": ' +
            sandbox.force_unicode(str(type(value)))
        )

    def _getattr(self, parent, name):
        name = sandbox.force_unicode(name)
        attribute = getattr(parent, name)
        attribute = sandbox.force_unicode(attribute)
        return attribute

    def _indent(self):
        self._level += 1

    def _maybe_dump_pair_as_object_shallow(self, name, value):
        if debug:
            self._dump_pair_as_object_shallow(name, value)

    def _maybe_dump_pair_as_string(self, name, value, datatype=None):
        if debug:
            self._dump_pair_as_string(name, value, datatype)

    def _maybe_dump_pair_as_type(self, name, value):
        if debug:
            self._dump_pair_as_type(name, value)

    def __init__(self):
        self._had_dir = []
        self._indentation = '  '
        self._level = 0
        self._lines = []

def dump():
    dumper = CherryPyDumper()
    dumper.populate()
    return dumper.render()
