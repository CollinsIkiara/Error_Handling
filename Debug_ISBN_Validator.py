def validate_isbn(isbn, length=None):
    # Handle missing length (called with only one argument)
    if length is None:
        print('Enter comma-separated values.')
        return
    # Handle non-numeric or invalid length
    if not isinstance(length, int):
        print('Length must be a number.')
        return
    # Handle length that is not 10 or 13
    if length != 10 and length != 13:
        print('Length should be 10 or 13.')
        return
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    main_digits = isbn[0:length - 1]
    given_check_digit = isbn[length - 1]
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    try:
        values = user_input.split(',')
        isbn = values[0]
        length_str = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

# main()

validate_isbn('1530051126', 10)     # Valid ISBN Code.
validate_isbn('080442957X', 10)     # Valid ISBN Code.
validate_isbn('9781530051120', 13)  # Valid ISBN Code.
validate_isbn('1530051125', 10)     # Invalid ISBN Code.
validate_isbn('9781530051120', 10)  # ISBN-10 code should be 10 digits long.
validate_isbn('1530051126', 13)     # ISBN-13 code should be 13 digits long.
validate_isbn('15-0051126', 10)     # Invalid character was found.
validate_isbn('1530051126', 9)      # Length should be 10 or 13.
validate_isbn('1530051125', 'A')    # Length must be a number.
validate_isbn('1530051125')         # Enter comma-separated values.