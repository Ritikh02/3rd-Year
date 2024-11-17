# 26. a) How many times does the filter operation call its lambda argument?
# b) How many times does the map operation call its lambda argument?
# c) If you reverse the filter and map operations, how many times does the map operation call its lambda argument?

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# The original expression
list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))

# Answer:
# a) The filter operation iterates over each element of the list and applies the lambda function to check if the element is odd. 
#    The filter lambda function `lambda x: x % 2 != 0` will be called once for every element in the `numbers` list, which contains 10 elements. 
#    So, the filter operation calls its lambda argument 10 times.

# b) The map operation applies its lambda function to each element returned by the filter operation. 
#    The filter operation returns only the odd numbers from the list. 
#    The odd numbers in `numbers` are: [3, 7, 1, 9, 5]. 
#    So, the map operation will call its lambda function once for each odd number, which is 5 times.

# c) If you reverse the filter and map operations, the map operation will first square every element in the list. 
#    Then the filter operation will check if the squared number is odd. 
#    The map operation will iterate over all the elements in the list, and thus, it will call its lambda function 10 times, 
#    because it processes each element in the `numbers` list before the filter is applied.
