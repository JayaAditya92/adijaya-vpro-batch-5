import pandas as pd
students = pd.DataFrame({
    "student_id":[101,102,103,104],
    "name":["Std1","Std2","Std3","Std4"]
})
marks = pd.DataFrame({
    "student_id":[101,102,103,105],
    "marks":[80,90,75,88]
})
# result = pd.merge(students,marks,on="student_id",how="inner")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="left")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="right")
# print(result)

# result = pd.merge(students,marks,on="student_id",how="outer")
# print(result)
