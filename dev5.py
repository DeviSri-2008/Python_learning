while(True):
    j = 1
    n = int(input("enter the N value"))
    if n == 0:
        break
    for i in range(n,n*10+1,n):
        print(j,"*",n,"=",j*n)
        j = j+1

 
    
