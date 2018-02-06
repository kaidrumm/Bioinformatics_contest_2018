from decimal import *
import sys
import numpy as np
from bigfloat import BigFloat
import math

finput = open(sys.argv[1], 'r')
foutput = open(sys.argv[2], 'w')

n = int(finput.readline())
while n > 0 :
	line = finput.readline().split(" ")
	a = BigFloat.exact(line[0], precision=1000) # glucose
	b = BigFloat.exact(line[1], precision=1000) # oxygen
	x = BigFloat.exact(line[2], precision=1000) # bank
	print "\n$%.2f in bank, $%.2f for glucose, $%.2f for oxygen" % (x, a, b)
	o = 12*a*x / (457*a + 6*b)
	g = (x - b*o)/a
	print "Buy %f oxygen and %f glucose" % (o, g)
	print "%f moles of oxygen at $%f/mole costs %f" % (o, b, o*b)
	print "%f moles of glucose at $%f/mole costs %f" % (g, a, g*a)
	r = 38 * (o / 6)
	print "%f moles of ATP by respiration" % r
	ferment = g - (o / 6)
	print "%f moles of ATP by fermentation" % ferment
	ATP = r + ferment
	print "%f moles of ATP total" % ATP
	# if 38*a < (a + 6*b) :
	# 	ATP = x / a
	# else: 
	# 	ATP = (38 * x) / (6 * b + a)
	foutput.write(str(ATP) + '\n')
	n -= 1
