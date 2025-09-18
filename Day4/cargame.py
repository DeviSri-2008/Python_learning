command = ""
while command != input("<").lower():
     command  =="quit"
if command == "start":
     print("car started")
elif command == "stop":
     print("car stopped")
elif command == "help":
     print(""" 
     start _ to start the car
     stop _ to stop the car
     quit _ to  quit
   """)
else:
     print("sorry i dont understand that!")