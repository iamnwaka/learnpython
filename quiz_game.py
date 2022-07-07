print('Welcome to my Quiz!')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()

print("okay! let's play :)")
score = 0

question1 = input("What year did Nigeria gained thier independence? ")
if question1.lower() == "1960":
    print("correct!")
    score += 1
else:
    print('incorrect!')
    
question2 = input("How many ethnic group do we have in nigeria? ")
if question2.lower() == "250":
    print("correct!")
    score += 1
else:
    print('incorrect!')
    
question3 = input("What does the eagle represent in the Nigerian coat of arm? ")
if question3 == "Strength":
    print("correct!")
    score += 1
else:
    print('incorrect!')
    
question4 = input("Which city in Nigeria was the first federal capital territory of Nigeria? ")
if question4 == "Calabar":
    print("correct!")
    score += 1
else:
    print('incorrect!')
    
question5 = input("What name is given to the men’s senior national football team of Nigeria? ")
if question5 == "Super Eagles":
    print("correct!")
    score += 1
else:
    print('incorrect!')
    
print("you got " + str(score) + " Questions Correct!")
print("you got " + str((score/4) * 100) + "%.")