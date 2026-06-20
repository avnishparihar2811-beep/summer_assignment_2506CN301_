# Write a program to Find product of digits
n=int(input("Enter the number: "))
p=1
while n>0:
    p=p*(n%10)
    n=n//10
print(p)