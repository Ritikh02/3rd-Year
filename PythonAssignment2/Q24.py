# Write a program that reads an integer from the user and checks which digits (0-9) have appeared in the number.


num = input("Enter an integer: ")
digits_seen = set(num)

digit_words = {
    '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE',
    '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN',
    '8': 'EIGHT', '9': 'NINE'
}

output = ' '.join(digit_words[digit] for digit in sorted(digits_seen))

print(f"The digits that appeared are: {output}")
