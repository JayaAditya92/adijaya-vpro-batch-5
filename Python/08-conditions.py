
# Ex1:
# age = 20
# if age >= 18:
#     print("Eligible !!!")

# Ex2:
# age = 16
# if age >= 18:
#     print("Major !!!")
# else:
#     print("Minor !!!")

# Ex3:

# marks = 75
# if marks >= 90:
#     print("A")
# elif marks >=75:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("D")

# Example 4:

# # Output (AB)
# x = 10
# if x > 5:
#     print("A")
# if x > 8:
#     print("B")
# if x > 15:
#     print("C")

# # Output : A
# if x > 5:
#     print("A")
# elif x > 8:
#     print("B")
# elif x > 15:
#     print("C")

# Example 5:
# age = 34
# salary = 60000
# if age>=18 and salary>=30000:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible")

# Example: 6

# age = 34
# is_citizen = True
# if age >=18 and is_citizen:
#     print("Eligible for Vote !!!")


# Example 7:

# age = 17
# has_permission = True
# if age>=18 or has_permission:
#     print("Allowed !!!")

# Example 8: O/P: Eligible for Loan

# age=34
# salary=60000
# exp=8

# if age >=18 and (salary>=30000 or exp>=3):
#     print("Eligible for Loan")
# else:
#     print("No Eligible for loan")  

# age = 25
# salary = 20000
# exp = 5

# if age >= 18 and (salary >=30000 or exp>=3):
#     print("Eligible for Loan")
# else:
#     print("No Eligible for Loan")

# Example 9: Login O/p: Please Login

# logged_in = False
# if not logged_in:
#     print("Please Login")
# else:
#     print("Logout")

# Ex10: O/p: Entry Allowed
# age = 25
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry Allowed")

#EX 11: output: Restricted !!!

# age = 20
# has_id = False
# if age >= 18:
#     if has_id:
#         print("Entry Allowed")
#     else:
#         print("Restricted !!!")
# else:
#     print("Not Eligible")

# EX 12: Restricted !!!

# age = 20
# if age >= 18:
#     if age >= 21:
#         print("Enter !!!")
#     else:
#         print("Restricted !!!")


# # ex 13: o/p: Admin Login

# username = "admin"
# if username == "admin":
#     print("Admin Login !!!")
# else:
#     print("User Login !!!")

# ex 14: username="" whenever we give empty string its give Falsy value Output: User Login

# username = ""           # Falsy Value
# if username == "admin":
#     print("Admin Login !!!")
# else:
#     print("User Login !!!")

# Falsy - False, None, 0, 0.0,"",[],(),{},set() outout: Empty

# items = []
# if items:
#     print("Availble !!!")
# else:
#     print("Empty !!!")


# x = 0
# if x:
#     print("Hello")
# else:
#     print("Welcome")

# #Using Content String
# x = "0"
# if x:
#     print("Hello")
# else:
#     print("Welcome")

# #output: Hello
# result = None
# if result:
#     print("Empty")
# else:
#     print("Hello")

#Empty
# result = None
# if result is None:
#     print("Empty !!!")

# # list1 = [10,20]
# # list2 = [20,10]
# # print(list1 == list2)       # False

# list1 = [10,20,30]
# list2 = [10,20,30]
# print(list1 is list2)       # False
# print(list1 == list2)       # True

# output: Found!!! Not Found Found

# lang = ["Java","ML","Python"]
# if "Python" in lang:
#     print("Found !!!")
# else:
#     print("Not Found !!!")

# if "Python" not in lang:
#     print("Found !!!")
# else:
#     print("Not Found !!!")

# str = "MachineLearning"
# if "Machine" in str:
#     print("Found !!!")

# age = 25
# if 18 <= age <= 60:                 # age >= 18 and age <=60
#     print("Work !!!")
# else:
#     print("Not Eligible !!!")

# x = 10
# 5 < x < 20        # x > 5 and x < 20
                    # 5 < x and x < 20

# 5 < x > 20

# age = 20
# res = "Major" if age>=18 else "Minor"
# print(res)

# # output:300
# num1 = 100
# num2 = 200
# num3 = 300
# res = num1 if (num1>num2 and num1>num3) else num2 if num2>num3 else num3
# print(res)

x = 10
if x / 0 or x > 5:
    print("Hello")
else:
    print("Welcome")