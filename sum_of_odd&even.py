#sum of odd and even
def sum_of_odd_and_even(a):
    odd ,even=0,0
    for i in a:
        while i !=0:
            digit=i%10         #345%10=5
            if digit %2==0:     #5%2=1
                even += digit
            else:
                odd +=digit             #5
            i //=10 #34
    return even,odd
a=[345,334,454,224,789]
odd,even=sum_of_odd_and_even(a)
print("odd",odd)
print("even",even)

