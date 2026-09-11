def hi(msg):
    msg = msg.upper()
    if "hello" in msg:
        return "Hi there!"
    elif "bye" in msg:
        return "Goodbye!"
    else:
        return "I dont understand."
x = input("Enter the string")
print(hi(x))
