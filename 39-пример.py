# A*x**2+B*x+C=0 kvadrat tenglama
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
D=B**2-4*A*C
if D>0:
    print('dva resheniya')
    X1=((-B**2+D)*0.5)/2*A
    X2=((-B**2-D)*0.5)/2*A
    print(X1,X2)
    if D==0:
        print('odno resheniye',X)
        X=(-B**2)/2*A
    print(X)
else:
    print('net resheniya')
