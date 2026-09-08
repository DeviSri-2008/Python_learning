n = int(input("enter the number"))
for i in range(n):
    if n%15 == 0:
        continue
    elif i == 10:
        for j in range(n):
            if j == 4:
                break;
            else:
                print(j,end='')
    else:
        print(i,end='')
        
        
        
       
        
