a=int(input("Enter first numbers"))
b=int(input("Enter second numbers"))
while(b!=0):
    r=a%b
    a=b
    b=r
print("GCD of given number is:",a)    