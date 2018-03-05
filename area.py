a=float(input('enter the first side A:'))
b=float(input('enter the second side B:'))
c=float(input('enter the third side C:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is %0.2f' %area)
