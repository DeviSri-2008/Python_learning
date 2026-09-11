import matplotlib.pyplot as plt
x = ["apples","bannans","cherries","date","grapes","blueberry"]
y = [80,20,10,50,90,100]
plt.bar(x,y,color = "blue",edgecolor="black",linewidth=2)
plt.title("fruit inventory")
plt.xlabel("fruits")
plt.ylabel("fruits in stock")
plt.show()
