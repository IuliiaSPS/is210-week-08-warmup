#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_05"""

PRESSURE = raw_input('What is your blood pressure? ')
PRESSURE = int(PRESSURE)
if PRESSURE < 89:
    BP_STATUS = 'Low'
elif 90 >= PRESSURE <= 119:
    BP_STATUS = 'Ideal'
elif 120 >= PRESSURE >= 139:
    BP_STATUS = 'Warning'
elif 140 >= PRESSURE >= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergerncy'

print 'Yor status is currently: {0}!'.format(BP_STATUS)
