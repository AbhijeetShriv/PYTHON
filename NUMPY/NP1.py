import numpy as np

# Generate 20 random marks between 0 and 100
marks = np.random.randint(0, 101, 20)

# Statistical calculations
mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
