# a dictinary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
#show the final result when quiz is completed

quiz = {
    "question1" : {
        "question" : "What is the capital city of Ethiopia?",
        "answer" : "Addis Ababa"
    },
    "question2" : {
        "question" : "What is the capital city of Sudan?",
        "answer" : "Cartoom"
    },
    "question3" : {
        "question" : "What is the capital city of Egypt?",
        "answer" : "Cario"
    }
}
#declare variable
score = 0
#LOOP
for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("You're Correct!")
        score += 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("You're Wrong!")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")
    
print("You got " + str(score) + " out of 3 questions correctly!")
print("Your percentage is " + str(int(score/3 * 100)) + "%")