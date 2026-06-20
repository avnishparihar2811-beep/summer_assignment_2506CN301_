# Write a program to Find sum of digits of a number
n=int(input("Enter the no: "))

sum=0
while n>0:
    sum+=n%10
    n=n//10
print(sum)