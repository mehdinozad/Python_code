quiz={
    "question1": {
        "question": "what is the capital of france?",
        "answer": "paris"
    },
    "question2": {
        "question": "what is the capital of iran?",
        "answer": "tehran"
    },
    "question3": {
        "question": "what is the capital of germany?",
        "answer": "berlin"
    },
    "question4": {
        "question": "what is the capital of italy?",
        "answer": "rome"
    },
    "question5": {
        "question": "what is the capital of japan?",
        "answer": "tokiyo"
    },
    "question6": {
        "question": "what is the capital of america?",
        "answer": "chicago"
    },
    "question7": {
        "question": "what is the capital of england?",
        "answer": "london"
    },
    "question8": {
        "question": "what is the capital of turkey?",
        "answer": "istanbul"
    },
}
score=0

for key, value in quiz.items():
    print(value['question'])
    answer=input("answer?")

    if answer.lower()==value['answer'.lower()]:
        print('correct')
        score=score+1
        print("your score is:" + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("the correct answer is:"+str(value['answer']))
        print("your score is:" + str(score))
        print("")
        print("")
print("you got "+str(score)+" out of 8 question correctlyparis")
print("your precentage is " +str(score/8*100)+"%")



