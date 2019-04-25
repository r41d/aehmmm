#!/usr/bin/env python3
# -*- coding: utf-8 *-*

import sys
import csv
import itertools
import datetime
import collections

import matplotlib
import matplotlib.pyplot as plt

def prepareDatetimes(raw_data):
	timestamps = [int(x[0]) for x in raw_data]
	return list(map(datetime.datetime.fromtimestamp, timestamps))

def plotByMinute(datetimes, savefile):
	HMkey = lambda x: x.strftime("%H:%M") # x.time()
	sortByMinute = sorted(datetimes, key=lambda x: x.timestamp())
	tsByMinute = {day:len(list(turns)) for day, turns in itertools.groupby(sortByMinute, key=HMkey)}
	minutelyCnt = collections.OrderedDict(sorted(tsByMinute.items()))
	for x,y in minutelyCnt.items():
		print(x,y)

	plt.plot(minutelyCnt.keys(), minutelyCnt.values())
	plt.savefig(savefile, dpi=300)
	#plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Please supply filename")
		sys.exit(1)
	with open(sys.argv[1], newline='') as f:
		raw_data = [r for r in csv.reader(f)]
	datetimes = prepareDatetimes(raw_data)
	plotByMinute(datetimes, sys.argv[1]+'.png')

