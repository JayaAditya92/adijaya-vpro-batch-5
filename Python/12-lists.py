"""
    collection of hetrogeneous elements
    allows duplicates
    inded starts from 0
    mutable
    supports negative indexes
"""

# Example-1
# list1 = [10,20,30,40,50]
# print(list1[3])
# print(list1[::-1])

# Example-2
# list1 = [10,20,30,40,50]
# found = False
# search_element = input("Enter Number : ")
# for num in list1:
#     if num == int(search_element):
#         found = True
#         print(found)


# #Example-3
# list1 = [10,20,30,40,50]

# print(list1[::-1])

# list1.reverse()
# print(list1)

# result = []
# for i in range(len(list1)-1,-1,-1):
#     result.append(list1[i])
# print(result)

# Example-4
# list1 = [(1,2),(3,4)]
# # Iterate

# for item in list1:
#     print(item)
# #Iterate and display each value separately

# list1 = [(1, 2), (3, 4)]

# for a, b in list1:
#     print(a, b)

# #Display with a message
# list1 = [(1, 2), (3, 4)]

# for a, b in list1:
#     print("First value:", a)
#     print("Second value:", b)

# #Using nested for loops

# list1 = [(1, 2), (3, 4)]

# for item in list1:
#     for value in item:
#         print(value)

# # Example-5
# list1 = [{"num1":200},{"num2":100}]
# # logic for addition

# # Example-6
# list1 = [10,20]
# # list1.append([30,40])
# # print(list1)
# list1.extend([30,40])
# print(list1)