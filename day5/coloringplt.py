import matplotlib.pyplot as plt
x = ["python","java","c++","javascript","c#"]
y = [10,20,40,60,80,]
plt.title("Programming language Popularity")
colors = ["red","yellow","blue","black","violet"]
plt.bar(x,y,color=colors,edgecolor="black",linewidth=1)
plt.show()
