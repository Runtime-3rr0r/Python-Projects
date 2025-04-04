def init():global highScoreFile;global highScore;global data;highScoreFile=open("highScores.txt","a+");highScoreFile.seek(0);data=highScoreFile.readlines();highScore={}
def readHighScore(data,highScore):
    for i in range(len(data)):data[i-1]=data[i-1].replace("\n","");currentItem=data[i-1].split(":");highScore[currentItem[0].lower()]=currentItem[1]
def getScore(playerName,highScore,highScoreFile,data):
    try:return highScore[playerName]
    except:
        KeyError
        if input("\nUsername not found\nAdd user? (y/n): ").lower()=="y":writeHighScore(playerName,"0",highScoreFile,data);print("\nAdded user:",playerName,"\n")
def writeHighScore(playerName,score,highScoreFile,data):
    if len(data)==0:writeData=playerName+":"+score
    else:writeData="\n"+playerName+":"+score
    highScoreFile.write(writeData)
init();readHighScore(data,highScore);print("Score:",getScore(input("\n\n\nPlease enter username: ").lower(),highScore,highScoreFile,data))