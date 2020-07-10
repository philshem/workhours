#!/usr/bin/env python

'''
python script to plot the hours of a workweek
most changes to the data should be made in config.py
'''

import matplotlib.pyplot as plt

# parameters and data can be changed here:
import config

def main():

	# plot empty bars
	plt.bar(range(1,config.ND+1), [config.NH]*config.ND, fill=False, width=1,linewidth=0.75,align='center')

	# add horizontal lines to signify hours of day
	for y in range(config.NH):
		plt.hlines(y=y, xmin=0.5, xmax=config.ND+0.5, linewidth=0.5, color='gray')

	for x in config.data:
		plt.bar(x.get('day')+1.0, x.get('hours'), fill=True, color=x.get('color','g'),alpha=0.7,width=1,)
		#print(x)

	# add day of week to x label
	plt.xticks(range(1,config.ND+2), config.x_days[0:config.ND], ha='center')

	# calculate total hours and days for figure header
	sum_hours = sum([x.get('hours') for x in config.data])
	count_days = sum([1 for x in config.data if x.get('hours',0) > 0])

	# add header, and x/y axis labels
	plt.title('{} total hours over a {}-day workweek'.format(sum_hours,count_days))
	#plt.xlabel('Day of the week')
	plt.ylabel('Hours per workday')

	# set dimenions of graph to center workweek
	plt.xlim(0, config.ND + 1)
	plt.ylim(-1, config.NH + 1)

	# plot graph
	plt.show()

if __name__ == "__main__":
	main()
