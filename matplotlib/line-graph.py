from matplotlib import pyplot as plt

###### PART 1. Line Graphs ######  
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

# plot line graphs
plt.plot(time, revenue, color='purple', linestyle = '--')
plt.plot(time, costs, color='#82edc9', marker = 's')
plt.show()

# axis bounds
plt.axis([0, 8, 200, 1000])

# label axes
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')


###### PART 2. Sub Plots ###### 
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# First Subplot
plt.subplot(1,2, 1)
plt.plot(months,temperature)
plt.title('First Subplot')
 
# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, "o")
plt.title('Second Subplot')
 
# Display both subplots
plt.show()

###### PART 3. Sub Plots II ###### 
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(bottom=0.2, wspace=0.35)
plt.show()

###### PART 4. Legends ###### 
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=8)

plt.show()

###### PART 5. Modify Ticks ###### 
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Axis Labels
ax = plt.subplot()

# x-axis
ax.set_xticks(months)
ax.set_xticklabels(month_names)

# y-axis
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])


plt.show()


###### PART 6. Figures ######
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure(figsize=(4, 10))

# Figure 1
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

# Figure 2
plt.figure(figsize=(7, 3)) 
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
