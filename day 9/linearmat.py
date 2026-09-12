import matplotlib.pyplot as plt
x = []
y = [] 
for i in range(-100,101):
    x.append(i)
    y.append(i*i)
plt.plot(x,y,linewidth=5)
plt.xlabel('x')
plt.ylabel('y = x*x')
plt.title('plot of x vs x*x')
plt.grid(True)
plt.savefig('one.png')
plt.show()

