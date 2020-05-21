# View (MVC pattern) for the home page

class View(object):
    def page(self):
        return self._renderer.html(
            head=self._head(),
            body=self._body(),
        )

    def _body(self):
        return self._renderer.body('{0}{1}{2}{3}'.format(
            self._renderer.p('Hello world!'),
            self._renderer.p(
                'The time of this response is {0}'.format(self._response_time)
            ),
            self._renderer.p(self._renderer.img(
                alt='favorite icon',
                src='favicon.ico',
            )),
            self._renderer.p(self._renderer.img(
                alt='made with CherryPy (small)',
                src='static/made_with_cherrypy_small.png',
            )),
        ))

    def _head(self):
        return self._renderer.head(
            'Hello',
            self._renderer.style('screen', None),
            30,
        )

    def __init__(self, renderer, response_time):
        self._renderer = renderer
        # TODO: screen user-supplied data for web safety
        self._response_time = response_time
