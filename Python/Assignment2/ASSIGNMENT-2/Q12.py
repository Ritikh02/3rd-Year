# Write a program to find out the mean, median, and mode of 1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6


from statistics import mean, median, mode

data = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]
mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)

print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")
