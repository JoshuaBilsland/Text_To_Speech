import pyttsx3

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')

# Welcome Message
engine.say("Welcome to the text to speech program")
print("Welcome to the text to speech program!")
engine.runAndWait()

# Start input loop
continueLoop = True
while continueLoop == True:
    # Change voice
    validInput = False
    while validInput == False:
        print("Please select which voice is used")
        maleOrFemaleVoice = input("Enter 'M' for male or 'F' for female :")
        if maleOrFemaleVoice == "M":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            print("Voice set to male")
            engine.say("Voice set to male")
            engine.runAndWait()
            validInput = True
        elif maleOrFemaleVoice == "F":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)
            print("Voice set to female")
            engine.say("Voice set to female")
            engine.runAndWait()
            validInput = True
        else:
            print("Please only enter 'M' for male or 'F' for female")
            validInput = False
            continueLoop = True

    # Change speech rate
    validInput = False
    while validInput == False:
        try:    
            rate = engine.getProperty('rate')
            speechRate = int(input("Enter speech rate (In words per minute) :"))
            engine.setProperty('rate', speechRate)
            print("Speech rate set to", speechRate, "words per minute")
            speechRateSetMessage = ("Speech rate set to",speechRate,"words per minute")
            engine.say(speechRateSetMessage)
            engine.runAndWait()
            validInput = True
        except:
            print("Please only enter a whole number")
            validInput = False

    # Convert text to speech
    textToConvert = input("Enter text that you would like to convert to speech:")
    engine.say(textToConvert)
    # Play the speech
    print("Playing speech...")
    engine.runAndWait()
    # Save to mp3
    validInput = False
    while validInput == False:
        saveToMp3 = input("Do you want to save this speech to an mp3 file? (Y/N) :")
        if saveToMp3 == "Y":
            print("Saving to mp3 file...")
            engine.save_to_file(textToConvert, "TextToSpeech.mp3")
            engine.runAndWait()
            print("Save successful")
            validInput = True
        elif saveToMp3 == "N":
            print("Ok, no problem")
            validInput = True
        else:
            print("Please only enter 'Y' or 'N'")
            
    # Asks user if they want to use the program again
    validInput = False
    while validInput == False:
        repeatProgram = input("Do you want to use the program again? (Y/N) :")
        if repeatProgram == "Y":
            continueLoop = True
            validInput = True
        elif repeatProgram == "N":
            continueLoop = False
            validInput = True
        else:
            print("Please only enter 'Y' or 'N'")
            
# End of program
print("------------------")
print(" Program Finished ")
print("------------------")
