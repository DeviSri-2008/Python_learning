import matplotlib.pyplot as plt
x = []
for i in range(1,11):
    x.append(i)
print(x)
y = []
for i in range(1,11):
    y.append(i**2)
print(y)
plt.bar(x,y,color = "pink")
plt.show()
