'''
from matplotlib import pyplot as plt
lithology = ["a", "b", "c", "d", "e", "f", "g"]
depth = [1061.50, 1061.60, 1061.70, 1061.80, 1061.90, 1062.00, 1062.10]
#line graph showing, lithology on x axis and depth on y axis
plt.plot(lithology, depth, marker= "o", color = "blue", linestyle= "solid")
#label both axis
plt.xlabel('Lithology')
plt.ylabel('Depth (m)')
#add a title
plt.title('A Litho Log')
#display chart
plt.show()
'''

#bar chart, showing amount of coal mined in 2018
from matplotlib import pyplot as plt
month = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov", "Dec"]
amount = [900, 800, 750, 700, 630, 770, 850, 1000, 500,400,350,200 ]
xs = [i + 0.6 for i, _ in enumerate(month)] #to set the bars to the center
plt.bar(xs,amount)
plt.title("A bar chart to show the amount of coal mined in 2018")
plt.xlabel("Months")
plt.ylabel("Amount in tonnes")
plt.xticks([i + 0.5 for i, _ in enumerate(month)], month) #prints items in months at center of bars
plt.show()