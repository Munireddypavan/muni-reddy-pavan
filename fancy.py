n=eval(input("enter the number:"))
x=0
for i in str(n):
    x+=n%10
    n//=10
print(x)

while(n!=0):
    x+=m%10
    n//=10
print(x)
