# Marks a Python package

import codecs
import logging

def force_unicode(value, encodings=(
    'utf-8-sig',
    'utf-16',
    'utf-16BE',
    'utf-16LE',
    'utf-32',
    'utf-32BE',
    'utf-32LE',
    'utf-7',
    'iso-8859-15',
    'iso-8859-1',
)):
    if isinstance(value, str):
        if not isinstance(value, str):
            if not value:
                return ''
            else:
                for encoding in encodings:
                    try:
                        return str(value, encoding)
                    except UnicodeDecodeError as e:
                        #print 'Tried "' + encoding + '" -> ' + str(e)
                        pass
                raise ValueError(
                    'Failed to convert to Unicode\n' +
                    '"' + value + '"' +
                    ' of length ' + str(len(value))
                )
    return value

def override_file_handler_formatter(logger, formatter):
    for h in logger.handlers:
        logger.debug(
            'Found ' + str(h) + ' on ' + str(logger)
        )
        if isinstance(h, logging.FileHandler):
            h.setFormatter(formatter)
            logger.debug(
                'Overrode formatter to ' + str(formatter) + ' on ' + str(h)
            )

def write_file(filename, content, encoding='utf-8'):
    with codecs.open(filename, 'w', encoding) as file:
        file.write(force_unicode(content))
