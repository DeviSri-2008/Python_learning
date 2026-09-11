import matplotlib.pyplot as plt
x = ['a','b','c']
y = [10,20,30]
plt.bar(x,y,color = 'skyblue')
plt.title("my saved plot")
plt.savefig("my-plot1.png")
plt.show()
