
"""
Demonstration module for quadratic interpolation.
Module that fits a quadratic function to 3 data points.
Modified by: Charlie
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve
import os.path as path

def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:

    A = np.vstack([np.ones(3), xi, xi**2]).T
    b = yi

    # Solve for the coefficients

    c = solve(A,b)

    return c

def plot_quad(xi, yi):
    """
    Quadratic interpolation plus plotting. Outputs quadratic.png
    """

    # Get coefficients

    c = quad_interp(xi,yi) 

    # Plot the resulting polynomial

    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)   # points to evaluate polynomial
    y = c[0] + c[1]*x + c[2]*x**2

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-2,8)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('quadratic.png')   # save figure as .png file

def cubic_interp(xi, yi):
    """
    Cubic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,3.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3.
    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message

    # Set up linear system to interpolate through data points:

    A = np.vstack([np.ones(4), xi, xi**2, xi**3]).T
    b = yi

    # Solve for the coefficients

    c = solve(A,b)

    return c

def plot_cubic(xi, yi):
    """
    Cubic interpolation plus plotting. Outputs cubic.png
    """

    # Get coefficients

    c = cubic_interp(xi,yi)

    # Plot the resulting polynomial

    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)   # points to evaluate polynomial
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-15,15)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('cubic.png')   # save figure as .png file

def poly_interp(xi, yi):
    """
    Generalized polynomial interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for all i = 0,1,2,3...
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3 + ....
    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have the same length"
    assert len(xi)==len(yi), error_message

    # Set up linear system to interpolate through data points:

    n = len(xi)
    A = np.ones((n,n))
    for i in range(0,n):
        A[:,i] = xi**i
    b = yi

    # Solve for the coefficients

    c = solve(A,b)

    return c

def plot_poly(xi, yi):
    """
    Generalized polynomial interpolation plus plotting.
    Outputs poly.png
    """
    # Get coefficients

    c = poly_interp(xi,yi)

    # Plot the resulting polynomial

    n = len(c)
    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)   # points to evaluate polynomial
    y = c[n-1]
    for j in range(n-1, 0, -1):
        y = y*x + c[j-1]

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-15,15)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('poly.png')   # save figure as .png file

def test_poly1():
    """
    Test general polynomial interpolation
    """
    xi = np.array([0.,-1.,1., -2.])
    yi = np.array([-1.,-2.,4., 13.])
    c = cubic_interp(xi,yi)
    c_true = np.array([-1.,  5.,  2., -2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_quad2():
    """
    Test whether plot_quad outputs a file
    """
    xi = np.array([1.,2.,3.])
    yi = np.array([3.,6.,7.])
    plot_quad(xi,yi)
    print path.realpath(__file__)
    assert path.isfile(path.realpath(__file__)[:-7] + '/quadratic.png'), \
        'plot_quad failed to output a file'

def test_cubic1():
    """
    Test cubic interpolation
    """
    xi = np.array([0.,-1.,1., -2.])
    yi = np.array([-1.,-2.,4., 13.])
    c = cubic_interp(xi,yi)
    c_true = np.array([-1.,  5.,  2., -2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1.,  0.,  2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    test_quad1()
    test_quad2()
    test_cubic1()

