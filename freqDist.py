#!/usr/bin/env python
#James Parks

rawData = []
sets = []

def sort(rawData, sets):
	sortedData = {}
	for thisSet in sets:
		sortedData[thisSet] = []
	for thisItem in rawData:
		for thisSet in sets:
			valMin, valMax = thisSet.split("-")
			if float(thisItem) > float(valMin):
				if float(thisItem) < float(valMax):
					sortedData[thisSet].append(thisItem)
	return sortedData

def sortFreq(rawData, sets):
	sortedData = {}
	sorted = sort(rawData, sets)
	for thisSet in sets:
		sortedData[thisSet] = len(sorted[thisSet]

def relativeFreq(rawData, sets):
	freqSort = sortFreq(rawData, sets)
	sortedData = {}
	for thisSet in sets:
		sortedData[thisSet] = freqSort[thisSet] / len(rawData]
	return sortedData

def percentFreq(rawData, sets):
	relFreq = relativeFreq(rawData, sets)
	sortedData = {}
	for thisSet in sets:
		sortedData[thisSet] = relFreqSort[thisSet] * 100
	return sortedData

def cumulativePercentFreq(rawData, sets):
	sortedData = {}
	percFreq = percentFreq(rawData, sets)
	lastVal = 0
	for thisSet in sets:
		thisVal = percFrea[thisSet]
		sortedData[thisSet] = float(thisVal) + float(lastVal)
		lastVal = lastVal + thisVal
	return sortedData

def cumulativeRelFreq(rawData, sets):
	sortedData = {}
	relFreq = relativeFreq(rawData, sets)
	lastVal = 0
	for thisSet in sets:
		thisVal = relFreq[thisSet]
		sortedData[thisSet] = float(thisVal) + float(lastVal)
		lastVal = lastVal + thisVal
	return sortedData 
