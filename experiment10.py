import matplotlib.pyplot as plt
import numpy as np

#1
x= [1,2,3]
y= [10,20,30]
plt.plot(x,y)
plt.xlabel(" lenght in cm")
plt.ylabel(" lenght in mm")
plt.title("chart")
plt.show()

x=np.linspace(0.1,2*np.pi,41)
y=np.exp(np.sin(x))
plt.stem(x, y)
plt.show()

#2
x = [3, 1, 3, 12, 2, 4, 4] 
y = [3, 2, 1, 4, 5, 6, 7] 


# This will plot a simple bar chart
plt.bar(x, y)
# Title to the plot
plt.title("Bar Chart")
# Adding the legends
plt.legend(["bar"])
plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 4] 
# This will plot a simple histogram
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
# Title to the plot
plt.title("Histogram")
# Adding the legends
plt.legend(["bar"])
plt.show()

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]
# This will plot a simple scatter chart
plt.scatter(x, y)
# Adding legend to the plot
plt.legend("A")
# Title to the plot
plt.title("Scatter chart")
plt.show()

np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
# Creating plot
plt.boxplot(data)

# show plot
plt.show()
x = [1, 2, 3, 4] 
# this will explode the 1st wedge
# i.e. will separate the 1st wedge
# from the chart
e  =(0.1, 0, 0, 0)
# This will plot a simple pie chart
plt.pie(x, explode = e)
# Title to the plot
plt.title("Pie chart")
plt.show()

# importing matplotlib
import matplotlib.pyplot as plt 
# making a simple plot
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]
# creating error
y_error = 0.2
# plotting graph
plt.plot(x, y)
plt.errorbar(x, y,yerr = y_error,fmt ='o')
plt.show()

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [1, 8, 27, 64, 125]
# Creating the figure object
fig = plt.figure()
# keeping the projection = 3d
# creates the 3d plot
ax = plt.axes(projection = '3d')
ax.plot3D(z, y, x)
plt.show()
