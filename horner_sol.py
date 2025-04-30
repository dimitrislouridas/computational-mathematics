import numpy as np

a = np.array( [ [ 3, 0, -2, 0, 1, 0 ] ] ).T # 3x^5 − 2x^3 + x
x0 = -2

def horner( a, x0 ):
    b = np.zeros_like( a )  # or use: b = np.zeros ( len(a) )
    b[0] = a[0]
    for i in range( 1, b.shape[0] ):
        b[i] = x0 * b[i-1] + a[i]
    
    return b[-1].item() 

print( horner( a, x0 ) )