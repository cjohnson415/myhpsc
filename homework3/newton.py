"""
Module that implements newtons method
for finding roots of functions.
"""

def solve(fvals, x0, debug=False):
    """
    Finds the root of the function f, specified
    by fvals and returns the final iterate
    as well as the number of iterations
    """

    if debug:
        print 'Initial guess: x = %22.15e' %  x0

    maxiter = 20
    tol = 1.e-14
    x = x0
    for i in range(maxiter):
        fx, fp = fvals(x)
        if abs(fx) < tol:
            break
        x = x - fx/fp
        if debug:
            print 'After %i iterations, x =  %22.15e' % (i+1,x)

    if i + 1 == maxiter:
        print "Warning: convergence never reached"

    return x, i


# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
