def verify_card_number(card_number):
    """Determines whether a card number is valid or invalid

        :params card_number: string - a string of numbers to be checked.
        :return total: integer - the total of the sum of odd and even digits in the card_number
    """
    # Get odd digits from the reveresed card number
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    # Add each digit to the sum_of_odd_digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Get the even digits from the reversed card number
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    # Multiply even digits by 2 and add the numbers together if value is 10 or greater.
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    """Translates card number to be able to verify whether the card number is valid or invalid
    """
    # In a live application card_number should be captured from input
    card_number = '4111-1111-4555-1134' 
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
