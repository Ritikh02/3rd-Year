# 20. Twenty students were asked to rate on a scale of 1 to 5 the quality of the food in the student cafeteria, 
# with 1 being "awful" and 5 being "excellent." Place the 20 responses in a list.
# Determine and display the frequency of each rating. Use the built-in (or user-defined) functions and 
# statistics module functions to display the following response statistics: minimum, maximum, range, mean, 
# median, mode, variance, and standard deviation.

from collections import Counter
import statistics

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
freq = Counter(responses)

print("Frequencies:", freq)
print("Minimum:", min(responses))
print("Maximum:", max(responses))
print("Range:", max(responses) - min(responses))
print("Mean:", statistics.mean(responses))
print("Median:", statistics.median(responses))
print("Mode:", statistics.mode(responses))
print("Variance:", statistics.variance(responses))
print("Standard Deviation:", statistics.stdev(responses))
