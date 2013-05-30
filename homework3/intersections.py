"""
Script that finds and plots the intersection
of two known functions.
"""
from newton import solve
import numpy as np
from numpy import pi, cos, sin
import pylab

guesses = np.array([-2.15, -1.7,-.9,1.3])
solns = np.zeros(4)

def fvals_intersect(x):
	"""
    Return f(x) and f'(x) for f(x) = x*cos(pi*x)
	"""
	f = x*cos(pi*x) - 1 + 0.6*x**2
	fp = -x*sin(pi*x)*pi + cos(pi*x) +1.2*x
	return f, fp

for j in range(len(guesses)):
	soln, i = solve(fvals_intersect, guesses[j])
	solns[j]=soln
	print 'With initial guess x0 = %22.15e,' % guesses[j]
	print '\tsolve returns x = %22.15e after %i iterations' % (soln, i)


#Begin Plotting
x = pylab.linspace(-5,5,1000)
fsolns = solns*cos(pi*solns)
pylab.plot(x,x*cos(pi*x),x,1-.6*x**2,solns,fsolns,'ko')
pylab.savefig('intersections.png')
