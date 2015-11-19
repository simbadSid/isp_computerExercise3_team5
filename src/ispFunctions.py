from scipy import *

import matplotlib.pyplot as plt
import numpy as np





def myMin(x):
	m = x[0]
	for k in range(len(x)):
		if (x[k] < m):
			m = x[k]        
	return m

def myMax(x):
	m = x[0]
	for k in range(0, len(x)):
		if (x[k] > m):
			m = x[k]        
	return m


def myMean(signal):
	res = signal[0]
	for k in range(1, len(signal)):
		res = res + signal[k]
	return res/len(signal)


def myStandardDeviation(signal):
	mean = myMean(signal)
	s	= 0
	for k in range(len(signal)):
		s += math.pow((signal[k] - mean),  2)
	return math.sqrt(s / (len(signal)-1))

# tv: true average value of the signal (unlike the mean which comes from experimental values)
def myAccuracy(signal, tv):
	mean = myMean(signal)
	return (math.fabs(tv - mean))

# Creates a histogram with an interval length equals 1.
def myHistogram(signal):
	histogram	= [0] * len(signal)
	minVal		= myMin(signal)
	for i in range(len(signal)):
		j = int(signal[i] - minVal)
		histogram[j] = histogram[j] + 1
	return histogram

#
#def myHistogram(signal, intervalLength):
#	histogram	= [0] * intervalLength
#	minVal		= myMin(signal)
#	for i in range(len(signal)):
#		j = int((signal[i] - minVal) / intervalLength)
#		histogram[j] = histogram[j] + 1
#	return histogram

def myHistogram(signal,intervalLength):
    minVal = myMin(signal)
    maxVal = myMax(signal)
    length = len(signal)
    N = int(ceil((maxVal-minVal)/intervalLength)) + 1
    h = [0]*N
    histoAxis = [m * intervalLength + minVal for m in xrange(N)]
    for i in range(0,length - 1):
            h[int(ceil((signal[i] - minVal)/intervalLength))] += 1

    return h,histoAxis
