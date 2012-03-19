#!/usr/bin/env python
"""
Script that says hello
"""

import sys


def do_stuff(name="World"):
    print "Hello %s!" % name


if __name__ == '__main__':
    if len(sys.argv) > 1:
        do_stuff(sys.argv[1])
    else:
        do_stuff()
