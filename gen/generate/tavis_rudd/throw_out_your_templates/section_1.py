# -*- coding: utf-8 -*-

################################################################################
# 1: str/unicode wrappers used to prevent double-escaping. This is the
# same concept as django.utils.safestring and webhelpers.html.literal

default_encoding = 'utf-8'


''' Disabled content
class safe_bytes(str):
    def decode(self, *args, **kws):
        return safe_unicode(super(safe_bytes, self).encode(*args, **kws))

    def __add__(self, o):
        res = super(safe_bytes, self).__add__(o)
        if isinstance(o, safe_unicode):
            return safe_unicode(res)
        elif isinstance(o, safe_bytes):
            return safe_bytes(res)
        else:
            return res


class safe_unicode(str):
    def encode(self, *args, **kws):
        return safe_bytes(super(safe_unicode, self).encode(*args, **kws))

    def __add__(self, o):
        res = super(safe_unicode, self).__add__(o)
        return (safe_unicode(res)
                if isinstance(o, (safe_unicode, safe_bytes)) else res)

'''

