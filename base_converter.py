def to_base(n, base):
    if base < 2 or base > 36:
        print("Base must be between 2 and 36.")
        return
    if n == 0:
        return "0"
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = ""
    while n:
        remainder = n % base
        digits += symbols[remainder]
        n //= base
    return digits[::-1]

print("\nWelcome to Base Converter!\n")
main = True

while main == True:
    num_list = input("Enter the number and base (ex: 45 2): ")

    if num_list == "exit":
        print("")
        main = False
    else:
        num_list = num_list.split(" ")
        target_num = int(num_list[0])
        target_base = int(num_list[1])

        match target_base:
            case 2:
                print(target_num, "in binary is:", format(target_num, "0b"), "\n")
            case 8:
                print(target_num, "in octal is:", format(target_num, "0o"), "\n")
            case 16:
                print(target_num, "in hexadecimal is:", format(target_num, "0X"), "\n")
            case _:
                print(target_num, "in base", target_base, "is:", to_base(target_num, target_base), "\n")
