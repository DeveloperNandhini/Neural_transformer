#find the largest number
a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
if (a>b and a>c):
    print("a is largest")
elif (b>a and b>c):
    print("b is largest")
elif (c>b and c>a):
    print("c is largest")
else:
    print("nothing is largest")
