#!/usr/bin/env python

'''
change these to update your graph
'''

# change the day, total hours per day, and also the color
# note: currently it's not possible to have multiple colors per day
# list of colors https://matplotlib.org/3.1.0/gallery/color/named_colors.html
data = [{'day': 0, 'hours' : 4.0, 'color' : 'b'},
		{'day': 1, 'hours' : 4.5, 'color' : 'lime'},
		{'day': 2, 'hours' : 6.5, 'color' : 'g'},
		{'day': 3, 'hours' : 4.5, 'color' : 'lime'},
		{'day': 4, 'hours' : 1.5, 'color' : 'r'},
		]

# define days of the week
x_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#alternative would be to use a library
#import calender; d = dict(zip(range(7),list(calendar.day_name)))

# note: changing these values below will probably break the code
# number of days in a workweek (must be integer)
ND = 5
# number of hours in a workday (must be integer)
NH = 8