# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

numbers = int(input(f'Enter numbers '))

def sum_of_digits(number):
    digits_sum = 0
    for char in str(number):
        digits_sum += int(char)
        return digits_sum

def digital_root(number):
    while number > 9:
        number = sum_of_digits(number)
        return number

print(digital_root(493193))