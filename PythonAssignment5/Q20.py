# 20. Write a Python program to change Mukesh’s net worth to 9650 in the following dictionary:
sample_dict = {
    'person1': {'name': 'Bezos', 'net worth': 21880},
    'person2': {'name': 'Elon', 'net worth': 31570},
    'person3': {'name': 'Mukesh', 'net worth': 965}
}

for key, value in sample_dict.items():
    if value['name'] == 'Mukesh':
        value['net worth'] = 9650

print(sample_dict)