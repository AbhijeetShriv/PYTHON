import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
s = pd.Series([85, 90, 78], index=['Maths', 'Science', 'English'])
print(s)

data = {
    'Maths': 85,
    'Science': 90,
    'English': 78,
    'Computer': 92
}

# Creating Pandas Series from dictionary
s = pd.Series(data)

print(s)
