# Given the following inputs, indicate in each case (1) to (16), whether the statements will execute
# successfully. If so, give what will be the outcome of execution. Also, give the output of print
# statements (where applicable):
# address = 'B-6, Lodhi road, Delhi'
# list1 = [1, 2, 3]
# list2 = ['a', 1, 'z', 26, 'd', 4]
# tuple1 = ('a', 'e', 'i', 'o', 'u')
# tuple2 = ([2, 4, 6, 8], [3, 6, 9], [4, 8], 5)
# 1. list1[3] = 4
# 2. print(list1 * 2)
# 3. print(min(list2))
# 4. print(max(list1))
# 5. print(list(address))
# 6. list2.extend(['e', 5])
#    print(list2)
# 7. list2.append(['e', 5])
#    print(list2)
# 8. names = ['rohan', 'mohan', 'gita']
#    names.sort(key=len)
#    print(names)
# 9. list3 = [(x * 2) for x in range(1, 11)]
#    print(list3)
# 10. del list3[1:]
#     print(list3)
# 11. list4 = [x + y for x in range(1, 5) for y in range(1, 5)]
#     print(list4)
# 12. tuple2[3] = 6
# 13. tuple2.append(5)
# 14. t1 = tuple2 + (5)
# 15. ', '.join(tuple1)
# 16. list(zip(['apple', 'orange'], ('red', 'orange')))

address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2, 4, 6, 8], [3, 6, 9], [4, 8], 5)

# 1. list1[3] = 4
try:
    list1[3] = 4
except IndexError as e:
    print(f"1. Error: {e}")

# 2. print(list1 * 2)
print("2.", list1 * 2)

# 3. print(min(list2))
try:
    print("3.", min(list2))
except TypeError as e:
    print(f"3. Error: {e}")

# 4. print(max(list1))
print("4.", max(list1))

# 5. print(list(address))
print("5.", list(address))

# 6. list2.extend(['e', 5])
list2.extend(['e', 5])
print("6.", list2)

# 7. list2.append(['e', 5])
list2.append(['e', 5])
print("7.", list2)

# 8. names.sort(key=len)
names = ['rohan', 'mohan', 'gita']
names.sort(key=len)
print("8.", names)

# 9. list3 = [(x * 2) for x in range(1, 11)]
list3 = [(x * 2) for x in range(1, 11)]
print("9.", list3)

# 10. del list3[1:]
del list3[1:]
print("10.", list3)

# 11. list4 = [x + y for x in range(1, 5) for y in range(1, 5)]
list4 = [x + y for x in range(1, 5) for y in range(1, 5)]
print("11.", list4)

# 12. tuple2[3] = 6
try:
    tuple2[3] = 6
except TypeError as e:
    print(f"12. Error: {e}")

# 13. tuple2.append(5)
try:
    tuple2.append(5)
except AttributeError as e:
    print(f"13. Error: {e}")

# 14. t1 = tuple2 + (5)
try:
    t1 = tuple2 + (5)
    print("14.", t1)
except TypeError as e:
    print(f"14. Error: {e}")

# 15. ', '.join(tuple1)
print("15.", ', '.join(tuple1))

# 16. list(zip(['apple', 'orange'], ('red', 'orange')))
print("16.", list(zip(['apple', 'orange'], ('red', 'orange'))))
