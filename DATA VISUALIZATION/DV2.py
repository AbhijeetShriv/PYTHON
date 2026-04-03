import matplotlib.pyplot as plt

students = ['Amit', 'Neha', 'Rahul']
marks = [5, 10, 15]
colors = ['red', 'yellow', 'blue']
plt.bar(students, marks, color=colors)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Result Comparison")
plt.show()
