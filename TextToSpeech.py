import pyttsx3

#Initialize Test-to-Speech engine 
engine = pyttsx3.init()

#Welcome Message
engine.say("Welcome to the text to speech program.")
engine.runAndWait()

#Start input loop
continueLoop = True
while continueLoop == True:
    #Convert text to speech 
    print()
    textToConvert = input ("Enter text that you would like to convert to speech:")
    print()
    engine.say(textToConvert)
    #Play the speech 
    engine.runAndWait()
    #Asks user if they want to use the program again
    validInput = False
    while validInput == False:
        print()
        repeatProgram = input("Do you want to use the program again? (Y/N) :")
        print()
        if repeatProgram == "Y":
            continueLoop = True
            validInput = True 
        elif repeatProgram == "N":
            continueLoop = False 
            validInput = True
        else:
            print()
            print("Please only enter Y/N")
            print()

#End of program
print("------------------")
print(" Program Finished ")
print("------------------")







