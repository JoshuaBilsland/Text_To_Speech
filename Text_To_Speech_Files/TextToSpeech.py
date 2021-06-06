import pyttsx3

#Initialize Text-to-Speech engine 
engine = pyttsx3.init()

#Welcome Message
engine.say("Welcome to the text to speech program.")
print("Welcome to the text to speech program!")
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
    #Save to mp3 
    saveToMp3 = input ("Do you want to save this speech to an mp3 file? (Y/N) :")
    if saveToMp3 == "Y":
        print()
        print("Saving to mp3 file...")
        print()
        engine.save_to_file(textToConvert,"TextToSpeech.mp3")
        engine.runAndWait()
        print()
        print("Save successful")
        print()
    
    #Asks user if they want to use the program again
    validInput = False
    while validInput == False:
        print()
        repeatProgram = input ("Do you want to use the program again? (Y/N) :")
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







