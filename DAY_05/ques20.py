# Find Largest Prime Factor
n = int(input("Enter a number: "))

largest = 1

for i in range(2, n + 1):
    if n % i == 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            largest = i

print("Largest Prime Factor =", largest)