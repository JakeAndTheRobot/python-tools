# import matplotlib
import matplotlib.pyplot as plt

# create a line plot
plt.plot(x, y)

# create a scatter plot
plt.scatter(x, y)

# create a bar plot
plt.bar(x, y)

# create a histogram
plt.hist(x)

# create a box plot
plt.boxplot(x)

# add a title to the plot
plt.title('Plot Title')

# add labels to the x and y axes
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# show the plot
plt.show()

# save the plot to a file
plt.savefig('plot.png')
