# PLOTTING MATHEMATICAL FUNCTIONS

import numpy as np
import matplotlib.pyplot as plt


x_values = np.linspace(0, 20,  100)

y_values = np.sin(x_values)

plt.plot(x_values, y_values)
plt.show()

x = np.linspace(0, 10, 100)
y = (6 * x - 30 ) ** 2

plt.plot(x, y)
plt.show()


# multiple graphs on the same axis  and Legends


x = np.linspace(0.1, 5, 200)
y1 = 2 * x
y2 = x ** 2
y3 =  np.log(x)
plt.plot(x, y1, "b-", label = "straight line")
plt.plot(x, y2, "r-", label = "expo")
plt.plot(x, y3, "g-", label = "logarithm")
plt.legend(loc = "upper left")
plt.show()

# sub-plots,  we want to draw multiple graphs but we don’t want them
# in the same plot necessarily

x = np.linspace(0,5, 200)
y11 = np.sin(x)
y22 = np.sqrt(x)
plt.subplot(211)
plt.plot(x , y11, "r-")

plt.subplot(212)
plt.plot(x, y22, "g--")
plt.show()

# Instead of plotting into subplots, we can also go ahead and plot our graphs
# into multiple windows. In Matplotlib we call these figures

plt.figure(1)
plt.plot(x, y11, "r-")
plt.figure(2)
plt.plot(x, y22, "g--")

#  setting tiltes

x = np.linspace(0, 50, 100)
y0 = np.sin(x)
plt.title("sine function")
plt.suptitle("Data science")
plt.grid(True)
plt.plot(x,y0)
plt.show()

plt.savefig("functions.png")

# histograms
# We start by defining a mean value mu (average height) and a standard
# deviation sigma . To create our x-values, we use our mu and sigma
# combined with 10000 randomly generated values. Notice that we are using
# the randn function here. This function generates values for a standard
# normal distribution , which means that we will get a bell curve of values

mu, sigma = 172, 4
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, density=True, facecolor="green")
plt.xlabel("height")
plt.ylabel("Probability")
plt.title("Hieght of Students")

plt.text(160, 0.125, "u = 171, a = 4")
# . Last but not least,
# we set the ranges for the two axes. Our x-values range from 155 to 190 and
# our y-values from 0 to 0.15. Also, the grid is turned on.
plt.axis(( 155 , 190 , 0 , 0.15 ))
plt.grid(True)
plt.show()


# Bar chart

bob = (90, 66, 87, 76)
charles = (89, 76, 45, 99)
daniel = (39, 79, 55,80)

skills = ("Python", "Java", "Networking", "Machine Learning")

width = 0.2
index = np.arange(4)

# We then use the bar function to plot our bar chart. For this, we define an
# array with the indices one to four and a bar width of 0.2.

plt.bar(index, bob, width=width, label="bob")
plt.bar(index + width, charles, width=width, label="charles")
plt.bar(index + width * 2, daniel, width=width, label="daniel")

plt.xticks(index + width, skills)
plt.ylim(0, 120)
plt.title('IT SKILLS LEVELS')
plt.xlabel("IT skill")
plt.ylabel('SKILLS LEVELS')
plt.legend()
plt.show()


# PIE CHART

labels = ("South African", "Angolan", "English", "Brazilian")

values = (47, 23, 20, 10)

plt.pie(values, labels=labels, autopct="%.2f%", shadow=True)
plt.title("CPT Nationalities")
plt.show()