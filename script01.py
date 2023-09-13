import subprocess




print("1. Display the default gateway\n2. Test Local Connectivity\n3. Test Remote Connectivity\n4. Test DNS Resolution\n5. Exit/quit the script")

userInput = input("Type a number 1-5: ")

userInput = int(userInput)

while(True):
    if(userInput == 1):
        result = subprocess.run("ipconfig")
    elif(userInput == 2):
        result = subprocess.run("ping 127.0.0.1")
    elif(userInput == 3):
        result = subprocess.run("ping 129.21.3.17")
    elif(userInput == 4):
        result = subprocess.run("ping www.google.com")
    elif(userInput == 5):
        break
    userInput = input("Type a number 1-5: ")
    userInput = int(userInput)
