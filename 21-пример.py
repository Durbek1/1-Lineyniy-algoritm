x1=float(input('x1='))
y1=float(input('y1='))
x2=float(input('x2='))
y2=float(input('y2='))
x3=float(input('x3='))
y3=float(input('y3='))
p=float(input('p='))
a = ((x1-x2)**2 +(y1-y2)**2)**(0.5)
b = ((x1-x3)**2 +(y1-y3)**2)**(0.5)
c = ((x3-x2)**2 +(y3-y2)**2)**(0.5)
s=(p*(p-a)*(p-b)*(p-c))**0.5
p=(a+b+c)/2
print(s,p)
