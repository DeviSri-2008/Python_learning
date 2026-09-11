import matplotlib.pyplot as plt
labels = ["B+ve","B-ve","AB+ve","AB-ve"]
sizes = [40,30,20,10]
colors = ['red','blue','green','yellow']
plt.pie(sizes,labels=labels,colors=colors,startangle=140)
plt.title("blood group")
plt.show()
