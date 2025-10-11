print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

text = "Tohm is great!"
print(text.lower())
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
Score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    Score += 1
else:
    print("InCorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    Score += 1
else:
    print("InCorrect!")

answer = input("What des RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    Score += 1
else:
    print("InCorrect!")

print("You got " + str(Score) + " questions correct out of 3!")
print("You got " + str((Score/4) * 100) + "%.")

