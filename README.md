# QR Decomposition from Scratch

Trying to learn numerical algorithms for QR decomposition. This repo
explores a simple implementation of Givens rotation to compute 
QR decomposition. 

# How to run 
```
$python3 qr_givens.py 
```

```
A:
[[ 12 -51   5]
 [  6 167 -68]
 [ -4  24 -41]]
---
k= 0  z= 2  u= 0
A:
 [[ 12 -51   5]
 [  6 167 -68]
 [ -4  24 -41]]
G:
[[ 0.9486833   0.         -0.31622777]
 [ 0.          1.          0.        ]
 [ 0.31622777  0.          0.9486833 ]]
GG:
[[ 12.64911064 -55.97231458  17.7087549 ]
 [  6.         167.         -68.        ]
 [  0.           6.64078309 -37.31487639]]
---
k= 0  z= 1  u= 0
A:
 [[ 12.64911064 -55.97231458  17.7087549 ]
 [  6.         167.         -68.        ]
 [  0.           6.64078309 -37.31487639]]
G:
 [[ 0.9035079   0.42857143  0.        ]
 [-0.42857143  0.9035079   0.        ]
 [ 0.          0.          1.        ]]
GG:
 [[ 14.          21.         -13.14285714]
 [  0.         174.87395461 -69.02800378]
 [  0.           6.64078309 -37.31487639]]
---
k= 1  z= 2  u= 1
A:
 [[ 14.          21.         -13.14285714]
 [  0.         174.87395461 -69.02800378]
 [  0.           6.64078309 -37.31487639]]
G:
 [[ 1.          0.          0.        ]
 [ 0.          0.99927974  0.03794733]
 [ 0.         -0.03794733  0.99927974]]
GG:
[[ 1.40000000e+01  2.10000000e+01 -1.31428571e+01]
 [ 0.00000000e+00  1.75000000e+02 -7.03942857e+01]
 [ 0.00000000e+00 -3.51323558e-16 -3.46685714e+01]]
---done
R:
 [[ 1.40000000e+01  2.10000000e+01 -1.31428571e+01]
 [ 0.00000000e+00  1.75000000e+02 -7.03942857e+01]
 [ 0.00000000e+00 -3.51323558e-16 -3.46685714e+01]]
Q:
[[ 0.85714286 -0.39428571  0.33142857]
 [ 0.42857143  0.90285714 -0.03428571]
 [-0.28571429  0.17142857  0.94285714]]
Qt.Q:
[[ 1.00000000e+00 -1.77012600e-17  3.39864191e-17]
 [-1.77012600e-17  1.00000000e+00  1.49540244e-18]
 [ 3.39864191e-17  1.49540244e-18  1.00000000e+00]]
Q.R:
[[ 12. -51.   5.]
 [  6. 167. -68.]
 [ -4.  24. -41.]]
```

# References:
- https://www.math.usm.edu/lambers/mat610/sum10/lecture9.pdf
- https://en.wikipedia.org/wiki/Givens_rotation 
