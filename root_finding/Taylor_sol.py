import numpy as np
import matplotlib.pyplot as plt

x = [ -5.5, -10, -5, -1, 0, 1, 5, 10 ]

m = {}
def fact( n ):
    """Calculate factorial."""
    if n <= 1:
        return 1
    if n in m:
        return m[n]
    m[n] = n * fact(n-1)
    return m[n]

def Taylor( x0, order=50 ):
    """Calculate the Taylor series for exp(x) centered at x0."""
    errors = np.zeros( (order+1,1) )  # initializing the absolute errors
    expected = np.full( (order+1,1), np.exp(x0) ) # the expected/real values of e^x

    term = 1
    errors[0] = np.abs( 1 - expected[0] )  # first term of the absolute error in the Taylor series

    series_sum = 1
    pow_x = 1
    for i in range(1,order+1):
        pow_x *= x0
        term = pow_x / fact(i)
        #term = ( term / i ) * x0
        series_sum += term
        errors[i] = np.abs( series_sum - expected[i] )

    return series_sum, (errors, expected) # errors = absolute errors, expected = expected values of e^x

L = np.linspace( -2.5, 2.5, 20 )    # values to print the Taylor series at

print(L)
plt.plot( L, np.exp(L), label='exp' )

# for each order i=0... calculate Taylor per point L and plot values
for myorder in range( 10 ): 

    val = []
    for i in L:
        val.append( Taylor(i, myorder)[0] )   # Taylor(i, myorder)[0] returns the Taylor series value at x=i where order=myorder
    plt.plot( L, val, label='order='+str(myorder+1) )

plt.grid(True)
plt.legend()
plt.show()

cnt = 0
plt.figure()


# for each x in x, calculate the absolute relative error and plot it
for i in x: 

    ans, errors = Taylor( i )
    cnt += 1
    plt.subplot( 2, 4, cnt )
    plt.plot( errors[0] / errors[1] , label='absolute relative error' ) # errors[0] corresponds to the absolute error, and errors[1] corresponds to the expected value.
    #plt.legend()
    plt.xlabel( 'order' )
    if (cnt-1) % 4 == 0:
        plt.ylabel( 'absolute relative error' )
    plt.title( 'x = ' + str(i) )
plt.show()

