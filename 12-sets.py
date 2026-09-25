"""
    set
    ***
        1) never allows duplicates
        2) unordered
        3) mutable
        4) {} / set()
        5) hetrogeneous
"""

# Example-1
# s1 = {}
# print(type(s1))     # <class 'dict'>
# s2 = set()
# print(type(s2))     # <class 'set'>

# Example-2
# s1 = {10,20,30,10,20}
# print(s1)       # {10, 20, 30}

# s2 = {"ravi","ravi","Ravi"}
# print(s2)

# s3 = set([10,20,30,10])
# print(s3)

# s4 = set((10,20,30,10,20))
# print(s4)

# # #O/p: {10, 20, 30}
# # {'Ravi', 'ravi'}
# # {10, 20, 30}
# # {10, 20, 30}


# Example-3
# s1 = {10,20,30}
# s1.add(40)
# print(s1)

# s1.update({50,60})
# print(s1)

# s1.update([70,80])
# print(s1)

# s1.update((90,100))
# print(s1)       # {70, 10, 80, 20, 90, 30, 100, 40, 50, 60}

# s1.remove(10)
# print(s1)

# # s1.remove(10)
# s1.discard(10)

# # pop - removes one random arbitory element
# x = s1.pop()
# print(x)

# s1.clear()
# print(s1)

# del s1
# print(s1)

# # Example-4
# s1 = {10,20,30}
# print(20 in s1)
# print(200 in s1)
# for element in s1:
#     if element == 20:
#         s1.remove(element)
#         s1.add(200)

# print(s1)


# # Example-5
# s1 = {1,2,3}
# s2 = {3,4,5}

# # s3 = s1.union(s2)
# # print(s3)           # {1, 2, 3, 4, 5}

# # s3 = s1 | s2
# # print(s3)           # {1, 2, 3, 4, 5}

# # s3 = s1.intersection(s2)
# # print(s3)

# # s3 = s1 & s2

# # print(s3)

# # #o/p: {1, 2, 3, 4, 5}
# # {1, 2, 3, 4, 5}
# # {3}
# # {3}

# #Example 6:
# # s3 = s1.difference(s2)
# # print(s3)       # {1, 2}

# # s3 = s2.difference(s1)
# # print(s3)

# # s3 = s1 - s2
# # print(s3)

# # s3 = s2 - s1
# # print(s3)

# # #o/p: {1, 2}
# # {4, 5}
# # {1, 2}
# # {4, 5}

# #Example 7: Cemetric difference
# s3 = s1.symmetric_difference(s2)
# print(s3)

# s3 = s1 ^ s2
# print(s3)
# #o/p: {1, 2, 4, 5}
# {1, 2, 4, 5}

# #Example-6:
# s1 = {1,2}
# s2 = {1,2,3,4}
# print(s1.issubset(s2)) #True
# print(s2.issuperset(s1)) #True

# #Example-7:

# s1={1,2,3}
# s2={4,5,6}
# print(s1.isdisjoint(s2)) #True

# #Example-8

# s1={10,20,30}
# print(len(s1)) #3

# #Example-9

# s1 = {1,2,3,4,5}
# s1 = {num**num for num in s1}
# print(s1) # {256, 1, 4, 3125, 27}


# closure - inner fun accessing outer function data
# able to access outer fun data even execution completion.
# def outer():
#    num = 100
#    def inner():
#       print(num)

#    return inner

# x = outer()
# x() #o/p: 100

#Example

# generators
# # "yield" keyword (used to implement the generators)
# def test():
#     yield 10    # pause
#     yield 20    # pause  
#     yield 30    # pause

# itr = test()
# print(itr)
# for x in itr:
#     print(x)

# def outer():
#     num = 100
#     print(num)
#     def inner():
#         nonlocal num
#         num = num + 900
#         print(num)
#     inner()
#     print(num)
# outer()



# num = 100       # global variable
# def outer():
#     # num = 50    # non local variable for inner() 
#     def inner():
#         # num = 10        # local variable for inner()
#         print(num)
#     inner()
# outer()