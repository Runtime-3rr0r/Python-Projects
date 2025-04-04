import turtle;from random import randint;from time import sleep;import string;savedNotes=[];noteData={};utils=["calc","notes","passGenerator","python"] # imports/vars/lists/dicts
games=["numberGuess"];savedFiles=["Not done yet!"];home=["saved files","games","utils"];directoryTree={"home":home,"games":games,"utils":utils,
"saved files":savedFiles};location="home"
def numberGuess(): # number guess game
    print("\nWelcome to Number Guess!")
    while True:
        num=randint(1,10)
        if int(input("\nPlease enter a number between 0 and 10: "))==num:print("You Win!") # if guess is answer then win
        else:print("Wrong!")
        if input("Play again? (y/n) ").lower()=="n":break # choose to exit loop
def python():
    cmds=[];ans="";line=1;print("Enter code below (\"run\" to run code):\n")
    while True:
        ans=input(f"{str(line)} ");line+=1
        if ans!="run":cmds.append(ans)
        else:print("\nRunning...\n");break
    for i in cmds:
        try:exec(i)
        except BaseException as error:print(f"An error ocurred at {i}","{}".format(error),"\n")
def passGenerator(): # password generator
    let=list(string.ascii_lowercase);sym=["!","@","#","$","$","%","^","&","*","(",")"]
    pwdStrength=int(input("\nEnter Password Strength (1, 2, 3):"));length=int(input("Enter Password Length:"));symType=0
    def simple(length): # only letters
        pwd=""
        for i in range(length): # add random letters to password
            if randint(0,1)==1:pwd+=let[randint(0,len(let)-1)].upper() # capitals
            else:pwd+=let[randint(0,len(let)-1)] # lowercase
        return pwd
    def medium(length): # letters/numbers
        pwd=""
        for i in range(length): # add random letters and numbers to password
            if randint(0,1)==1:
                if randint(0,1)==1:pwd+=let[randint(0,len(let)-1)].upper() # capitals
                else:pwd+=let[randint(0,len(let)-1)] # lowercase
            else:pwd+=str(randint(0,9)) # numbers
        return pwd
    def strong(length): # letters/numbers/specials
        pwd=""
        for i in range(length): # add random letters, numbers, and symbols to password
            symType=randint(0,2)
            if symType==1:
                if randint(0,1)==1:pwd+=let[randint(0,len(let)-1)].upper() # capitals
                else:pwd+=let[randint(0,len(let)-1)] # lowercase
            elif symType==2:pwd+=str(randint(0,9)) # numbers
            else:pwd+=sym[randint(0,len(sym)-1)] # symbols
        return pwd
    for i in range(3):print("\nPass %s: %s"%(str(i+1),simple(length))) if pwdStrength==1 else None # print simple password
    for i in range(3):print("\nPass %s: %s"%(str(i+1),medium(length))) if pwdStrength==2 else None # print medium password
    for i in range(3):print("\nPass %s: %s"%(str(i+1),strong(length))) if pwdStrength==3 else None # print strong password
    print("\n\n\n\n\n")
def notes(): # notes app
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere are your notes:\n")
        for note in savedNotes:print(note) if len(savedNotes)>0 else None # prints existing notes if any
        print("")
        if len(savedNotes)==0:print("You have no notes!\n") # tell user if has no notes
        ans=input("Enter note name to open, or create a new one! (\"exit\" to quit notes): ").lower()
        if ans not in savedNotes and ans!="exit": # creates new note
            if ans!="":savedNotes.append(ans);print(f'Note "{ans}" created\n') # adds new note to saved notes
            else:
                print("Note name cannot be empty...");repeat=True # no empty ones, thats dumb
                while repeat: # makes sure user isn't continuing to be dumb (creating existing or empty notes)
                    repeat=False;ans=input("Enter new note name: ").lower()
                    if ans in savedNotes:print(f'Note "{ans}" already exists...');repeat=True
                    elif ans=="":print("Note name cannot be empty...");repeat=True
        elif ans in savedNotes: # opens existing note
            print(f'Opening note "{ans}"...\n');sleep(.5)
            for i in range(14):print("\n")
            if ans in noteData: # if note has data, print and allow edits
                newContent=input(f'Editing note "{ans}"\n\n\ncurrent content:\n\n    {noteData[ans]}\n\ncontent to write ("none" to skip): ')
                if newContent!="none":noteData[ans]=newContent # adds inputted data to note data, skips if "none"
            else:noteData[ans]=input(f'Enter content for note "{ans}": ') # if note has no data, enter some data
        elif ans=="exit":print("Closing notes...\n");break # exits loop
def calculator(): # calculator
    while True: # gets first number, making sure user isn't dumb (entering non ints)
        try:x=float(input("Enter first number: "));break
        except ValueError:print("Thats not a number, dummy")
    while True: # gets second number, making sure user isn't dumb (entering non ints)
        try:y=float(input("Enter second number: "));break
        except ValueError:print("Thats not a number, dummy")
    while True: # gets an operation, making sure user isn't dumb (entering other than ops)
        op=input("Choose an op (+, -, *, /): ")
        if op not in ["+","-","*","/"]:print("Invalid op, dummy")
        else:break
    if op=="+":result=x+y # do some calculations
    elif op=="-":result=x-y
    elif op=="*":result=x*y
    elif op=="/" and y!=0:result=x/y
    else:print("Error! Division by zero.");return # if user is dumb and does x/0
    return result
print("\n\nWelcome to the Python Operating System! Type \"help\" for options.\n\n") # be nice to user
while True: # main
    print(location+": ",end="");ans=input() # kindly inform user of current directory
    if ans=="help": # help the user, since they are not smart
        print("Available commands:\n");print("move <location>: move to a location")
        print("show: lists available apps/files");print("<app name> run an app");print("exit: Exit the program\n")
    elif ans.startswith("move ") and ans[5:] in directoryTree:print("Changed directory to",ans[5:],"\n");location=ans[5:] # move to a desired location, if it exists
    elif ans.startswith("show"):print(directoryTree[location]) # show user everything in current location
    elif ans=="exit":print("Exiting...");break # exits program
    if location=="utils" and ans=="calc":print(calculator()) # only run apps if they are in the same directory as app
    if location=="utils" and ans=="notes":notes()
    if location=="utils" and ans=="passGenerator":passGenerator()
    if location=="utils" and ans=="python":python()
    if location=="games" and ans=="numberGuess":numberGuess()