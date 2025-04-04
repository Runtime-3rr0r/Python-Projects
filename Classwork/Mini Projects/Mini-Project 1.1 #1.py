# Import libraries
import turtle as trtl

# Setup turtle (the right way)
pt = trtl.Turtle()
pt.pensize(10)
pt.speed(100)

print("\n\nWELCOME! I can tell if you are saying nice things or mean things!\n")

# Draw face functions
def drawHappyFace():
    pt.circle(100)
    pt.penup()
    pt.lt(90)
    pt.fd(75)
    pt.rt(90)
    pt.bk(70)
    pt.rt(75)
    pt.pendown()
    pt.circle(75, 150)
    pt.penup()
    pt.rt(75)
    pt.bk(70)
    pt.lt(90)
    pt.fd(25)
    pt.rt(90)
    pt.fd(35)
    pt.pendown()
    pt.circle(10)
    pt.penup()
    pt.bk(70)
    pt.pendown()
    pt.circle(10)

def drawSadFace():
    pt.circle(100)
    pt.penup()
    pt.lt(90)
    pt.fd(75)
    pt.rt(90)
    pt.bk(70)
    pt.rt(105)
    pt.pendown()
    pt.circle(75, -150)
    pt.penup()
    pt.lt(75)
    pt.fd(70)
    pt.rt(90)
    pt.fd(50)
    pt.rt(90)
    pt.fd(35)
    pt.pendown()
    pt.circle(10)
    pt.penup()
    pt.bk(70)
    pt.pendown()
    pt.circle(10)

# Main
while True:
    # Open and setup training file
    trainingFile = open(r"trainingData.txt", "a+")
    trainingFile.seek(0)
    trainingData = trainingFile.readlines()

    # Create dictionary
    responseData = {}

    # Variable declars
    currentPhrase = ""
    sentiment = 0
    hasWord = False

    # Add words from traning file to dictionary as positive/negative
    for i in range(len(trainingData)):
        currentPhrase = trainingData[i - 1]
        currentPhrase = currentPhrase.replace("\n", "")
        currentPhrase = currentPhrase.split(":")
        responseData[currentPhrase[0].lower()] = currentPhrase[1]

    # Get rid of unneccesary punctuation
    print("\nSay something nice! (or mean)")
    response = input("\nWrite:")
    response = response.replace("!", "")
    response = response.replace("?", "")
    response = response.replace(".", "")
    response = response.replace(",", "")
    response = response.replace(";", "")
    response = response.replace(":", "")
    response = response.split()

    # Check if word is positive/negative from dictionary
    for i in range(len(response)):
        if response[i - 1].lower() in responseData:
            if responseData[response[i - 1].lower()] == "pos":
                sentiment += 1
            elif responseData[response[i - 1].lower()] == "neg":
                sentiment -= 1
           
            # Show that word was in dictionary
            hasWord = True
   
    # Print if statement was net positive/negative
    if hasWord:
        if sentiment > 0:
            print("This is a positive phrase!")
           
            # Draw a happy face
            drawHappyFace()
        else:
            print("This is a negative phrase!")

            # Draw a sad face
            drawSadFace()

    # If no word found then add it as positive/negative
    else:
        response = input("\nI don't recognize these words...\nWere there any words that had a positive or negative meaning (y/n): ").lower()
        if response == "y":
            response = input("\nWhat word(s) were positive or negative? (seperate by commas):")
            response = response.split(", ")
                   
            # Repeat for each word inputted
            for i in range(len(response)):
                print("Was", response[i - 1], "a positive or negative word? (p/n:)", end = "")
                ans = input()

                # Write to file
                if ans == "p":
                    writeString = "\n" + response[i - 1] + ":" + "pos"
                    trainingFile.write(writeString)
                elif ans == "n":
                    writeString = "\n" + response[i - 1] + ":" + "neg"
                    trainingFile.write(writeString)
                
                print(i)
        elif response == "n":
            print("\nOk! Phrase was not saved.\n")

    # reset painter
    input("Check the drawing! (Enter to continue)")
    pt.clear()
    pt.penup()
    pt.goto(0, 0)
    pt.pendown()