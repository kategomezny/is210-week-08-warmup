#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple branching statement"""


YOUR_PRESSURE = raw_input('What is your blood pressure? ')

if int(YOUR_PRESSURE) <= 89:
    BP_STATUS = 'Low'

elif int(YOUR_PRESSURE) <= 119:
    BP_STATUS = 'Ideal'

elif int(YOUR_PRESSURE) <= 139:
    BP_STATUS = 'Warning'

elif int(YOUR_PRESSURE) <= 159:
    BP_STATUS = 'High'

else:
    BP_STATUS = 'Emergency'

print 'Your status is currently: {}'.format(BP_STATUS)
