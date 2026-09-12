import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
x=[]
y=[]
for i in range(0,100,1):
    x.append(i)
    y.append(i)
ax1.set_xlabel("Variable X")
ax1.set_ylabel("Variable Y")
ax1.scatter(x, y, color='violet',hatch = patterns)
plt.savefig("hi.png")
plt.show()
