#!/usr/bin/env python

# import logging
import sys

from my_logging import adjust_logging
from trigger import configure
from my_logging import configure_logging
from my_exam import environment
from my_exam import ENV_PROD
from my_exam import EXAM_ID
from my_psutil import get_uptime
from logging import getLogger
from trigger import Trigger


LOG = getLogger('exam-manage')


def main():
    try:
        configure_logging()
        # adjust_logging()

        LOG.debug("main() try = began")
        uptime_in_minutes = get_uptime() / 60
        LOG.info("System has been up for %d minutes", uptime_in_minutes)

        Trigger.exam_id = EXAM_ID
        Trigger.url_template = 'http://tiny.cc/CB-' + EXAM_ID + '-{0}'
        configure()
        Trigger.visit_all(uptime_in_minutes)
    except BaseException as e:
        LOG.error("main() except = failure")
        LOG.exception(e)
        sys.exit(1)
    else:
        LOG.debug("main() else = success")
        sys.exit(0)
    finally:
        LOG.debug("main() finally = ended")


if __name__ == '__main__':
    main()


""" Disabled content
"""

