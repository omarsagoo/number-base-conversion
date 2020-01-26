from math import modf
import string


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    dec_num = 0
    # initialize variable to store the max exponent the base is going to use. 
    max_expo = len(digits) - 1
    # store all the digits to be used, up to hexatridecimal (base32).
    # stored as a list, the index of the digit used in the array is the value in decimal
    hexatri_string = string.digits + string.ascii_lowercase
    # iterate through the string of digits (where all letters are lowercased)
    for digit in digits.lower():
        # incrememnt a variable storing the value of the decimal number with the index multiplied by the 
        # base to the power of the corresponding exponent
        dec_num += hexatri_string.index(digit) * (base ** max_expo)
        # decrement the exponent by one
        max_expo -= 1

    # return the decimal number
    return dec_num

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    num_str = ''
    # store all the digits to be used, up to hexatridecimal (base32).
    # stored as a list, the index of the digit used in the array is the value in decimal
    hexatri_string = string.digits + string.ascii_lowercase

    # while loop: check while the number does not equal 0
    while number != 0:
        # using python math module modf store the decimal, and the whole number from the original 
        # number divided by the base. i.e. 19.8  dec = .8, whole = 19
        dec, whole = modf(number/base)
        # reasign the number variable
        number = whole
        # prepend the appropriate digit into a string of the numbers
        num_str = hexatri_string[round(dec*base)] + num_str

    # return the number in the corresponding base
    return num_str

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # check if the given number is base 10,
    # if it is, encode the number to the requested base
    # else, decode the number into base 10 then encode into the requested base
    if base1 == 10:
        return encode(int(digits), base2)
    else:
        dec_digits = decode(digits, base1)
        return str(encode(int(dec_digits), base2))

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
