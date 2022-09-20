import numpy as np 
import math

# A Simple implementation of Givens rotation to compute QR decomposition 


# References:
# https://www.math.usm.edu/lambers/mat610/sum10/lecture9.pdf
# https://en.wikipedia.org/wiki/Givens_rotation 



def givens( a, b ):
    hyp = 1.0 / np.sqrt( a*a + b*b )
    #hyp = 1.0 / math.hypot( a, b )
    return a*hyp, -b*hyp

def Givens( A, k, z, u):
    print( "k=", k, ' z=', z , ' u=', u )
    print( 'A:\n', A )
    cos, sin = givens(A[u, k], A[z, k] )
    
    
    
    if False:
        g = np.array( [ [cos, -sin], [sin, cos] ] )
        print( 'g:\n', g )

    G = np.eye( A.shape[0], A.shape[0] )
    G[ z, z ] = cos 
    G[ u, u ] = cos 
    G[ u, z ] = -sin 
    G[ z, u] = sin 
    print( "G:\n", G )

    if False: 
        vv = np.array( [ [A[1,0] ], [ A[2,0] ] ] ) 
        print( 'vv:\n', vv )
        gg = np.matmul( g, vv )
        print( 'gg:\n', gg )

    GG = np.matmul( G, A )
    print( "GG:\n", GG )
    
    return G, GG

    
if False: 
    A = np.array( [\
    [0.8147, 0.0975, 0.1576], \
    [0.9058, 0.2785, 0.9706],\
    [0.1270, 0.5469, 0.9572],\
    [0.9134, 0.9575, 0.4854],\
    [0.6324, 0.9649, 0.8003]\
    ])
    print( 'A:\n', A )
    
    G_cum = np.eye(A.shape[0], A.shape[1])
    
    
    ########
    print( "---")
    k=0 ; z=4 ; u=3
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G, G_cum )
    
    print( "---")
    A = GG 
    k=0 ; z=3 ; u=2
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G, G_cum )
    
    print( "---")
    A = GG 
    k=0 ; z=2 ; u=1
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G, G_cum )
    
    print( "---")
    A = GG 
    k=0 ; z=1 ; u=0
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G, G_cum )
    
    
    print( "---")
    A = GG 
    k=1 ; z=4 ; u=3
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G, G_cum )
    
    print( "---done")
    R = GG 
    Q = G_cum.transpose()
    print( "R:\n", R )
    print( "Q:\n", Q )
    print( "Qt.Q:\n", np.matmul( Q.transpose(), Q ) )
    print( "Q.R:\n", np.matmul( Q, R ))


    
########
if True:
    A = np.array( [ [12, -51, 5], [6, 167, -68], [-4, 24, -41] ])
    print( "A:\n", A )
    
    G_cum = np.eye(3,3)
    
    print ( "---")
    k = 0 #column 
    z = 2 #zero out this index 
    u = 0 #using this index 
    G, GG = Givens( A, k, z, u )
    G_cum = np.matmul( G , G_cum )
    
    print ( "---")
    A = GG 
    k = 0 ;z = 1;u = 0
    G, GG = Givens( A, k, z, u)
    G_cum = np.matmul( G, G_cum )
    
    print ( "---")
    A = GG 
    k = 1; z = 2; u = 1
    G, GG = Givens( A, k, z, u)
    G_cum = np.matmul( G, G_cum )
    
    print( "---done")
    R = GG 
    Q = G_cum.transpose()
    print( "R:\n", R )
    print( "Q:\n", Q )
    print( "Qt.Q:\n", np.matmul( Q.transpose(), Q ) )
    print( "Q.R:\n", np.matmul( Q, R ))


