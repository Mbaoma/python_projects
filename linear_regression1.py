#import numpy and matplotlib modules
import numpy as np
import matplotlib.pyplot as plt
#define a function for the formulae
def features_preferences(x,y):
	#number of data points
	n= np.size(x)
	#mean of x and y
	a_x,a_y= np.mean(x), np.mean(y)
	ssxy= np.sum(y* x) - n * a_x * a_y
	ssxx= np.sum(x* x) - n * (a_x * a_x)
	b_1= ssxy / ssxx
	b_0= a_y - (b_1 * a_x)
	return (b_1,b_0)
#define a function to plot the graph
def plot_graph(x,y,b):
	plt.scatter(x,y,color="r", s=20, marker="o")
# calculate value of y predicted
	y_predicted= b[0] + (b[1] * x)
	plt.plot(x,y_predicted, color="b")
	plt.xlabel("x axis")
	plt.ylabel("y axis")
	plt.show()
#define a function that holds the x & y values
def main():
	x= np.array([0,1,2,3,4,5,6,7,8,9])
	y= np.array([1,3,2,5,7,8,8,9,10,12])
	b= features_preferences(x,y)
	plot_graph(x,y,b)
if __name__== "__main__":
	main()