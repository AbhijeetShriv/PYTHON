import matplotlib.pyplot as plt

brands = ['Samsung', 'Nokia', 'Xiomi']
market_share = [38.5, 29.1, 25.5]
plt.pie(market_share, labels=brands, autopct='%1.1f%%')
plt.title("Mobile Market Share")
plt.show()
