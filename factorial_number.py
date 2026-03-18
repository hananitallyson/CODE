number = int(input("\nEnter a number (e.g. 5): "))
factorial = number
factors = number - 1

while factors != 1:
    factorial *= factors
    factors -= 1

print(f"{number}! is equal to {factorial}.\n")
