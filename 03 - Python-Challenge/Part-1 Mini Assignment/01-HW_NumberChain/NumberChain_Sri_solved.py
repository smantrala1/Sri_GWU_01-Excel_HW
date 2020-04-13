# Initial variable to track game play

usercontinue = "y"
# Set start and last number
startvalue = 0 

while usercontinue == "y":
    uservalue = int(input("How Many Numbers?"))
    #endvalue = uservalue
    for x in range(uservalue):
        currentnumber = startvalue + x
        print(currentnumber)

    startvalue = currentnumber + 1
 
    usercontinue = input("Continue the chain: (y)es or (n)o?")

