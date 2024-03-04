n=input("enter the number for sum of even:")
x=len(n)
n=int(n)
even=0
n1=n
for  i in range (0,x,1):
    if((n%10)%2==0):
        even+=n%10
    n=n//10
print(even)
n=eval(input("enter the number for sum of odd:"))
even=0
n1=n
while(n>0):
    if((n%10)%2!=0):
        even+=n%10
    n=n//10
print(even)
