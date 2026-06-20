# Print Armstrong Numbers in a Range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)