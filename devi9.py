a = int(input("enter the starting value"))
b = int(input("enter the ending value"))
for i in range(a,b):
    if i%7 == 0 or i%5 == 0:
        continue
    else:
        print(i)
