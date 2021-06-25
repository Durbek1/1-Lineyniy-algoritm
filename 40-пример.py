# A*x**2+B*x+C=0 kvadrat tenglama
A1=float(input('A='))
B1=float(input('B='))
C1=float(input('C='))
A2=float(input('A='))
B2=float(input('B='))
C2=float(input('C='))
D=(A1*B2-A2*B1)
X=(C1*B2-C2*B1)/D
Y=(C2*A1-A2*C1)/D
print(X,Y,D)
