ni=eval(input("enter the first number :"))
j=eval(input("enter the first number :"))
print("before swap",i,j)
i,j=j,i
print("after swap",i,j)
temp=i
i=j
j=temp
print ("using temp",i,j)
