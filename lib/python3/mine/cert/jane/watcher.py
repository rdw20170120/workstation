#!/usr/bin/env python

"""
    JANE Watcher monitors a specific directory for files matching a specific
    naming convention. These files represent different exam phases and
    contain data that is aggregated together to produce a final score.

    It is implemented as a daemon that outputs log messages as new files are
    created in the specified directory.

    It currently supports the following syntax:

    python watcher.py watch_dir

    watch_dir specifies the specific directory to monitor.
"""

import logging
import os
import re
import sys
import time
from Queue import Queue
from threading import Thread

from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer

import processor
from repository import PhaseRepository
from utility import get_regex, configure_logging


LOG = logging.getLogger('watcher')
DB_LOCATION = '/tmp/jane.db'


def process(queue):
    """
    Function invoked on a thread to get file names from a queue
    and process each one.
    """
    if os.path.exists(DB_LOCATION):
        os.remove(DB_LOCATION)
    repo = PhaseRepository('SQLite', DB_LOCATION)
    while True:
        file_path = queue.get()
        try:
            processor.process(repo, file_path)
        except StandardError as ex:
            LOG.error(ex.message)
        queue.task_done()


def scan_directory(directory, queue):
    """
    Function invoked to scan the specified directory and find files that
    match a specific regex and put those file names in the queue for
    processing by another thread.
    """
    logging.info('Scanning directory: ' + directory)
    exp = re.compile(get_regex())
    count = 0
    for file_name in os.listdir(directory):
        if exp.match(file_name) is not None:
            queue.put(directory + '/' + file_name)
            count = count + 1
    LOG.debug('Found %d matching files in directory: %s', count, directory)


class PhaseFileHandler(RegexMatchingEventHandler):
    """
    Class designed to be used in conjunction with WatchDog to monitor a specific
    folder and react to the creation of new files in it. The names of those files
    are placed on a queue for processing by another thread.
    """

    def __init__(self, queue):
        super(PhaseFileHandler, self).__init__(regexes=[get_regex()],
                                               ignore_directories=True)
        self.queue = queue

    def on_created(self, event):
        super(PhaseFileHandler, self).on_created(event)
        LOG.info('Received file: %s', event.src_path)
        self.queue.put(event.src_path)


if __name__ == "__main__":
    configure_logging()
    if len(sys.argv) < 2:
        LOG.error('No directory specified')
        sys.exit(2)
    TARGET = os.path.abspath(sys.argv[1])
    if not os.path.exists(TARGET):
        LOG.info('Waiting for directory %s to exist', TARGET)
        while not os.path.exists(TARGET):
            time.sleep(1)
        LOG.info('Directory %s now exists', TARGET)
    LOG.info('Monitoring directory: ' + TARGET)
    QUEUE = Queue()
    WORKER = Thread(target=process, args=(QUEUE,))
    WORKER.setDaemon(True)
    WORKER.start()
    OBSERVER = Observer()
    OBSERVER.schedule(PhaseFileHandler(QUEUE), TARGET)
    OBSERVER.start()
    scan_directory(TARGET, QUEUE)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        OBSERVER.stop()
    OBSERVER.join()
