#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

MYLEN = len(MYINPUT)
LONGSTR = 'long' if MYLEN > MAX_LENGTH else LONGSTR

OUTPUT = 'That certainly was a {0} story!'.format(LONGSTR)
print OUTPUT
