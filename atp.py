from decimal import *
import sys
import numpy as np
from bigfloat import BigFloat

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'w')

n = int(f.readline())
while n > 0 :
	line = f.readline().split(" ")
	a = BigFloat.exact(line[0], precision=1000) # glucose
	b = BigFloat.exact(line[1], precision=1000) # oxygen
	x = BigFloat.exact(line[2], precision=1000) # bank
	if 38*a < (a + 6*b) :
		ATP = 2 * x / a
	else: 
		ATP = (38 * x) / (6 * b + a)
	g.write(str(ATP) + '\n')
	n -= 1
