import random

def gen_binary(n):
    number = ""
    for _ in range(n):
        number += str(random.randint(0, 1))
    return number

print("Welcome to Binary Guesser!\n")
game = True

total_bits = 4

while game == True:
    binary_to_guess = gen_binary(total_bits)
    print("What decimal number is equivalent to [", binary_to_guess, "]")
    answer_num = int(input("Enter the decimal: "))

    binary_to_decimal = int(binary_to_guess, 2)

    if answer_num == binary_to_decimal:
        print("\nCorrect!\nThe number was", binary_to_decimal,"\n")
        game = True
    else:
        print("\nWrong!\nThe number was", binary_to_decimal, "\n")
        game = False
