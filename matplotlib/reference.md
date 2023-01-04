# Reference

## Plotting

```python
# create a line plot
plt.plot(x, y)

# create a scatter plot
plt.scatter(x, y)

# create a bar plot
plt.bar(x, y)

# create a bar plot with error bars
plt.bar(x, y, yerr=errors)

# create a histogram
plt.hist(x)

# create a box plot
plt.boxplot(x)

# create a pie chart
plt.pie(sizes, labels=labels)
```

## Customizing the Plot

```python
# add a title to the plot
plt.title('Plot Title')

# add labels to the x and y axes
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# set the x and y limits of the plot
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# add a grid to the plot
plt.grid(True)

# add a legend to the plot
plt.legend(loc='upper left')
```
## Showing and Saving the Plot

```python
# show the plot
plt.show()

# save the plot to a file
plt.savefig('plot.png')
```
