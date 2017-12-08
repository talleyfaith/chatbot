# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Hello. I'm [Name of Chatbot].")
    print("Say something to me!")

    while talking:
        statement = input(">> ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
