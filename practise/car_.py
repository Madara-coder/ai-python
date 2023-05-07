# Building the car game using python...

"""start - to start the car
stop - to stop the car
quit - to exit
"""
command = ""
started = False # use of the boolean algebra

print("Waiting for the command......")

while command != "quit": # while True: // can be written as alternative
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started")
       
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command == "quit":
        print("The game is exited.")
        break
    else:
        print("\n Sorry! Command not understood\n")
    
        
    