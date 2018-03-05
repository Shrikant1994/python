a=float(input("enter the value for A:"))
b=float(input("enter the value for B:"))
c=float(input("enter the value for C:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is %0.2f' %area)
