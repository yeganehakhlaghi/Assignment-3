import random

subjects=["lion","cow","rabbit","pig","bee","crab","fish","horse","dog","panda","fox"]
#,[bacon,beef,chiken,duck,sausages,salmon,soap,pizza],[apple,banana,blackberry,cherry,coconut,grapefruit,kiwi,lemon]]

selectedWord=subjects[random.randint(0,len(subjects)-1)]
#print(selectedWord)

chance=7
user_true_char=[]
while "true":
    win=1
    for anyChar in selectedWord:
        if anyChar in user_true_char:
            print(anyChar,end='')
        else:
            print("_ ",end='') 
            win=0
    if win==1:
        print("\nYou won 🤩")
        break
    print("\nchanse = ",chance)
    #print("_ " * len(selectedWord))
    #print("Enter a letter")
    char=input("\nEnter a letter : ")
    if char in selectedWord:
        user_true_char.append(char)
        print("✅")
    else:
        print("❌")
        chance-=1
    
    if chance==0:
        print ("The answer is :" ,selectedWord)
        print("game over \nyou lose🙁 ")

        break

    

