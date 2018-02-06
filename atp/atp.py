from decimal import *
import sys
import numpy as np

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'w')

n = int(f.readline())
while n > 0 :
	line = f.readline().split(" ")
	a = float(line[0]) # glucose
	b = float(line[1]) # oxygen 
	x = float(line[2]) # bank   
	if 16*a <= (a + 6*b) :
		ATP = 2 * x / a
	else: 
		ATP = (38 * x) / (6 * b + a)
	g.write(str(ATP) + '\n')
	n -= 1
