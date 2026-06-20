# Check Armstrong Number
n = int(input("Enter a number: "))

temp = n
digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")