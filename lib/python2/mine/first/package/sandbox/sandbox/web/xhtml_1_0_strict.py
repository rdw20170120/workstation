# XHTML 1.0 content renderer

class Renderer(object):
    def attribute(self, name, value):
        # TODO: screen attribute name
        # TODO: screen attribute value
        return '{0}="{1}"'.format(name, value)

    def body(self, content):
        return '<body>{0}</body>'.format(content)

    def content_type(self):
        return 'application/xhtml+xml'

    def document_type(self):
        return '''<!DOCTYPE html PUBLIC
'-//W3C//DTD XHTML 1.0 Strict//EN'
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'
>'''

    def encoding(self):
        return 'UTF-8'

    def head(self, title, content, refresh_in_seconds=0):
        return '<head>{0}{1}{2}{3}</head>'.format(
            self._meta_content_type(),
            self._meta_refresh(refresh_in_seconds),
            self._title(title),
            content,
        )

    def html(self, head, body):
        return '{0}{1}{2}{3}{4}{5}'.format(
            self._declaration(),
            self.document_type(),
            self._prolog(),
            head,
            body,
            self._epilog(),
        )

    def img(self, alt, src):
        return '<img {1} {0}/>'.format(
            self.attribute('alt', alt),
            self.attribute('src', src),
        )

    def p(self, content):
        return '<p>{0}</p>'.format(content)

    def style(self, media, css):
        return '<style {2} {1}>{0}</style>'.format(
            css,
            self.attribute('media', media),
            self.attribute('type', 'text/css'),
        )

    def _declaration(self):
        return '<?xml {1} {0}?>'.format(
            self.attribute('encoding', self.encoding()),
            self.attribute('version', '1.0'),
        )

    def _epilog(self):
        return '</html>'

    def _meta(self, http_equiv, content):
        return '<meta {1} {0}/>'.format(
            self.attribute('content', '{0}'.format(content)),
            self.attribute('http-equiv', http_equiv),
        )

    def _meta_content_type(self):
        return self._meta(
            'Content-Type',
            '{0};charset={1}'.format(self.content_type(), self.encoding()),
        )

    def _meta_refresh(self, seconds):
        if seconds > 0:
            return self._meta('Refresh', seconds)
        else:
            return ''
        
    def _prolog(self):
        return '''<html
xmlns='http://www.w3.org/1999/xhtml'
xml:lang='en' lang='en' dir='ltr'
>'''

    def _title(self, text):
        return '<title>{0}</title>'.format(text)
