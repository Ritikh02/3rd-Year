# 5. A dictionary which maps country names to Internet top-level domains (TLDs) is given as follows:
# tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
# Perform the following tasks and display the results:

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a) Check whether the dictionary contains the key 'Canada'.
print('Canada' in tlds)

# b) Check whether the dictionary contains the key 'France'.
print('France' in tlds)

# c) Iterate through the key-value pairs and display them in a two-column format.
for country, tld in tlds.items():
    print(f"{country}\t{tld}")

# d) Add the key–value pair 'Sweden' and 'sw' (incorrect TLD).
tlds['Sweden'] = 'sw'

# e) Update the value for the key 'Sweden' to 'se' (correct TLD).
tlds['Sweden'] = 'se'

# f) Use dictionary comprehension to reverse the keys and values.
reversed_tlds = {v: k for k, v in tlds.items()}
print(reversed_tlds)