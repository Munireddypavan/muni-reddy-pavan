n = eval(input("enter the number"))
temp = n
num = 0
rev = 0

while(n > 0):
    num = n % 10
    rev = rev * 10
    rev += num 
    n = n // 10

if rev == temp:
    print("palindrome")
else:
    print("not palindrome")

