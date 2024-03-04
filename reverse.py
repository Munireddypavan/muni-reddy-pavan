n=eval(input("enter the number:"))
nxt=0
while(n>0):
    one=n%10
    nxt=nxt*10+one
    n=n//10
print(nxt)
