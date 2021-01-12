from matplotlib import pyplot as plt

###### PART 1. Simple Bar Plots ######  
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales, color='teal')

# ax object
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.title('Simple Bar Chart')

plt.show()


###### PART 2. Side-By-Side Bars ######  
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1, color='lightblue')

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store2_x,sales2, color='teal')
plt.title('Side-By-Side Bars')

plt.show()



###### PART 3. Stacked Bars ######  
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(sales1)),
  sales1) 

sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(sales2)),
  sales2,
  bottom=sales1, color='lavender')

legend_labels=["Location 1", "Location 2"]
plt.legend(legend_labels)
plt.show()


###### PART 4. Error Bars ######  
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr=error, capsize=5, color='slateblue')
plt.title('Error Bars')
plt.show()
