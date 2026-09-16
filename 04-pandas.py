# import pandas as pd
# students = pd.DataFrame({
#     "student_id":[101,102,103,104],
#     "name":["Std1","Std2","Std3","Std4"]
# })
# marks = pd.DataFrame({
#     "student_id":[101,102,103,105],
#     "marks":[80,90,75,88]
# })
# result = pd.merge(students,marks,on="student_id",how="inner")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="left")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="right")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="outer")
# print(result)

# import pandas as pd
# df = pd.DataFrame({
#     "name":["Std1","Std2","Std3","Std4"],
#     "marks":[80,90,70,60],
#     "age":[20,21,22,23]
# })

# df["marks"] = 100
# print(df)

# df["marks"] = df["marks"] + 10
# print(df)

# df[["marks","age"]] = 0
# print(df)


#Eliminate the Data/ Summarizing the data
#Summarizing the data is called pivot table

# import pandas as pd
# df = pd.DataFrame({
#     "Name":["Ram","Ram","Ravi","Ravi"],
#     "products":["Laptop","Mobile","Laptop","Mobile"],
#     "sales":[50000,20000,60000,30000]
# })
# print(df)
# print("------------------------")
# result = df.pivot(index="Name",columns="products",values="sales")
# print(result)

# read two excel sheets and generate output output.xlsx
#(one.xlsx & two.xlsx) --> output.xlsx

# import pandas as pd
# df = pd.DataFrame({
#     "Name":["Ram","Ravi","Anil","Kiran"],
#     "marks":[80,None,90,None]
# })

# df.drop(1,inplace=True)
# print(df)

# df.drop([0,2,3],inplace=True)
# print(df)

# res= df.fillna(0)                 #Fill the missed data with 0 and update the original dataframe
# print(res)         

# res= df["marks"].fillna(0)
# print(df)

# #Fill the missed data with the mean and update the original dataframe
# df["marks"]= df["marks"].fillna(df["marks"].mean())
# print(df)

# #Fill the missed data with the previous value and update the original dataframe
# df["marks"]= df["marks"].ffill()
# print(df) 

# #Fill the missed data with the next value and update the original dataframe
# df["marks"]=df["marks"].bfill()
# print(df)             

#Fill the missed data with 100 and update the original dataframe
# df.fillna(100,inplace=True)
# print(df)

# #Fill the missed data with the previous value and update the original dataframe
# df.ffill(inplace=True)
# print(df)

# print(df)                          
# print(df.isnull())            #Missed Data: True
# print(df.isna())              #Missed Data: True

# # print(df.isnull().sum())        #Missed Data: Count of True #Name: 0 Marks: 2

# res=df.dropna()                       #Drop the rows which have missed data
# print(res)          #2 rec
# print(df)            #4 rec

# df.dropna(inplace=True)                 #Drop the rows which have missed data and update the original dataframe
# print(df)