from matplotlib import pyplot as plt

# define data
x = [1, 2, 3, 4, 5, 6, 7,8]
y1 = [24,30,38,186,256,356,311,653]
y2 = [23,28,37,178,248,345,294,632]


# plot line graphs
plt.plot(x, y1, color="pink", marker='o')
plt.plot(x, y2, color="gray", marker='o')

# add labels
plt.title("TESLA 10-Year Stock Analysis")
plt.xlabel("Year")
plt.ylabel("Stock Value")

# legend 
legend_labels = ["TSLA Highs", "TSLA Lows"]
plt.legend(legend_labels, loc=8)

plt.show()
