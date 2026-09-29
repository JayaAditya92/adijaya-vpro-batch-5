# msg="Python"
# print(msg)

# msg="Hello"
# print(msg[0])
# print(msg[-5])


# print(msg[4])
# print(msg[-4])

# print(msg[0:2])
# print(msg[1:3]) # 1 and 2 included and 3 - exculded
# print(msg[2:])
# print(msg[:3]) # 0 - included and 3 - exculded

# print(msg[-3:])
# print(msg[-5:-3]) #-5  and -4 included and -3 excluded

# print(msg[::-1]) 
# print(msg[::-2])
# print(msg[::-3])

msg1="Welcome"
# print(msg1[0], msg1[-7])
# print(msg1[3], msg1[-4])
# print(msg1[::2])           #Wloe
# print(msg1[::-1])          #emocleW
# print(msg1[::3])           #Wce
# print(msg1[::-2])          #eolW
# print(msg1[::-3])          #ecW

# print(msg1[0:2])             #We
# print(msg1[:2])              #We
# print(msg1[:0+2])            #We
# print(msg1[3:])              #come

# print(msg1[-2:])               #me
# print(msg1[-4:])               #come
# print(msg1[-7:-5])             #We


# print(msg1[:-7])               #Empty String
# print(msg1[:-5])               #We
# print(msg1[:-4])               #Wel

# #We cannot change the string because it is immutable
# msg1[0] = "w"  # This will raise an error

# #we are contacting the string to change the first letter
# print("w" +msg1[1:])  #welcome

#Vpro Started Generative AI to include one variable in another variable we can use f-string
name="Vpro"
course="Generative AI"

# msg=f"{name} Started {course}"
# print(msg)

# msg="{} started {}".format(name,course)
# print(msg)

# msg="{1} started {0}".format(course,name)
# print(msg)

# msg="""
# 1)GenAI
# 2)AgenticAI
# 3)ML
# 4)DL
# 5)NLP
# 5)Cloud Deployment 
# """
# print(msg)

# """
# int
# ***
#   positive
#   negative
#   0

# """
# #Python allowed underscore in the number to make it more readable.
# # num1=12_34_56_789
# # print(num1)  #123456789

# ******************************************
# # Q) Why Python allowed underscore?
# # Ans) Python allowed underscore in the number to make it more readable. For example, 1_000_000 is more readable than 1000000. 
# But this facilty is not available in other programming languages like C, C++, Java, etc. So, Python is more readable than other programming languages.

# num1=2_00
# num2=1_00
# add=num1+num2
# sub=num1-num2
# print(add)  #300
# print(sub)  #100

# Note: Hexadecimal, Octal and Binary numbers are also allowed in Python. Who will converted into decimal number automatically by Python.
# num1=0X123ABC
# print(num1)  #1194684

# num2=0o123
# print(num2)  #83

# num3=0b1010
# print(num3)  #10