import pandas as pandu
import openpyxl

data = {
    'Name': ['Abhijeet', 'Abhi', 'Curiem'],
    'Age': [20, 21, 19],
    'Course': ['BCA', 'BCA', 'BCA']
}
# Keys = Column names
# Values = Column data

data1 = pandu.DataFrame(data)

print(data1)

data2 = [
    ('Amit', 20, 'BCA'),
    ('Ravi', 21, 'BCA'),
    ('Neha', 19, 'BCA')
]

data3 = pandu.DataFrame(data2, columns=['Name', 'Age', 'Course'])
print(data3)
df = pandu.read_csv("students.csv")
print(df)

# df = pandu.read_excel("students.xlsx")
# print(df)
print(df.head(2))  # This method displays first 5 rows by default
print(df.tail())  # This method displays last 5 rows by default
df.info()  # This method displays Column Names, Data Types, Non-Null Values and Memory Usage.
print(
    df.describe())  # This method displays count:Number of values, mean: Average, std: Standard deviation, min: Minimum value, 25%: First quartile,
# 50%: Median, 75%: Third quartile, max: Maximum value.
