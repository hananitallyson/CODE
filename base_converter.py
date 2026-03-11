def to_base(n, base):
    if n == 0:
        return "0"  
    digits = ""
    while n:
        digits += str(n % base)
        n //= base
    return digits[::-1]

print("\nWelcome to Base Converter!")

num_list = input("Enter the number and base (ex: 45 2): ")
num_list = num_list.split(" ")

target_num = int(num_list[0])
target_base = int(num_list[1])

match target_base:
    case 2:
        print(target_num, "in binary is:", format(target_num, "0b"), "\n")
    case 8:
        print(target_num, "in octal is:", format(target_num, "0o"), "\n")
    case 16:
        print(target_num, "in hexadecimal is:", format(target_num, "0x"), "\n")
    case _:
        print(target_num, "in base", target_base, "is:", to_base(target_num, target_base), "\n")
