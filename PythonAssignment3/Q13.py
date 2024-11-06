# Question 13: Write a program that converts a Roman numeral to its integer equivalent.

def roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    for i in range(len(roman)):
        if i > 0 and roman_values[roman[i]] > roman_values[roman[i - 1]]:
            integer_value += roman_values[roman[i]] - 2 * roman_values[roman[i - 1]]
        else:
            integer_value += roman_values[roman[i]]
    return integer_value

user_input = input("Enter a Roman numeral: ")
print(roman_to_integer(user_input))
