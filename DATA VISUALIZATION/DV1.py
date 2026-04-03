import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'March']
profit = [2000, 3000, 2500]

plt.plot(months, profit)
plt.xlabel("Months")
plt.ylabel("Company Profit")
plt.title("Over 3 Months")
plt.show()
