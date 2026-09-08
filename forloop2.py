n = int(input("enter the n value:"))
for i in range(n): 
    if n%15 == 0:
        continue
    elif i == 10:
        for j in range(n):
            if j == 4:
                break;
            else:
                print(j)
    else:
        print(i)
        
        
        
       
        
