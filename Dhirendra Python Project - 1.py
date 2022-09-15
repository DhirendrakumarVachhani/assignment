# Word Puzzle Game develope by Dhirendrakumar Vachhani as a Project-1 
# for Full Stack Web Development using Python

print("\nWord Puzzle Game:\n\nIn the game the user has to solve this puzzle for 5 words,one at a time.")
print("\nUser get score +1 for each correct answer and -1 for each wrong answer.")
print("\nAt last you get final score.\n")

print("Press Enter to start your Game\n")
input()

score=0
def checkString(l,score):
    if l==lans:
        score+=1
        print("\nCorrect\n")
    else:
        score-=1
        print("\nWrong\n")
    return score

i=1
while i:
    l=[x.lower() for x in input("Arrange the letters to form a valid word:\nNPTHEEAL\n")]
    lans=['e','l','e','p','h','a','n','t']
    score=checkString(l,score)

    l=[x.lower() for x in input("Arrange the letters to form a valid word:\nNSUEEEQC\n")]
    lans=['s','e','q','u','e','n','c','e']
    score=checkString(l,score)

    l=[x.lower() for x in input("Arrange the letters to form a valid word:\nTTTMSANEE\n")]
    lans=['s','t','a','t','e','m','e','n','t']
    score=checkString(l,score)

    l=[x.lower() for x in input("Arrange the letters to form a valid word:\nNDTVMOPEEEL\n")]
    lans=['d','e','v','e','l','o','p','m','e','n','t']
    score=checkString(l,score)

    l=[x.lower() for x in input("Arrange the letters to form a valid word:\nTHERARACC\n")]
    lans=['c','h','a','r','a','c','t','e','r']
    score=checkString(l,score)
    print("Net Score is",score,"\n") 
    score=0 
    round=input("Are you want to play next round [y]\n")
    if round=="y":
        pass
    else:
        print("\nThanks for playing\n\n Have a nice day\n")
        break
       
       

