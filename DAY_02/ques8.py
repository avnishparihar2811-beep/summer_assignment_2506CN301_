# Write a program to Check whether a number is palindrome
n=int(input("Enter the number: "))
check=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if rev==check:
    print("The number is palindrome")
else:
    print("No, it is not palindrome")