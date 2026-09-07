print("Welcome to bank!")
amount = 5000
a = input("enter the name:")
b = input("enter the password:")
if b == "sree" and a == "devi":
    print("login successful\nwelcome devi\n your account balance is 5000")
    while(True):
        c = input("do you want to deposit press y/n")
        if c == "y" :
            deposit = int(input("enter the amount to deposit"))
            amount +=deposit
            print("your account balance is",amount)
        else:
            print("thank you for banking with us")
            break
else:
    print("login failed",a)




