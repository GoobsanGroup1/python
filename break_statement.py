import this 
import sys
import random 






number =0
while True:
    print("I luv Candy", str(number))

    number += 1
    if number == 7:
        break




numTaken = [3,5,7,11,13]
print ("Avalible numbers are :")
for i in range (1,21):
    
    if i in  numTaken :
        continue
print(i)



ans=True
while ans:
    quations= input("Ask the magic 5 ball aquation: (press enter to quit):")
    Answers=random.randint(1,5)

    if Answers == "":
        sys.exite()
    elif  Answers== 1:
        print("its certain")
    elif Answers ==2:
        print("out look good:")
    elif Answers == 3:
        print ("you may realy on me")
    elif Answers == 4:
        print("Ask me again later")
    elif Answers ==5:
        print("replay hazy try again")
    else:
        print("you are not human")
