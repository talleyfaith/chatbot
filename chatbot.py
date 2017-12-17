# PyChat 2K17

import random, time

def start():
    pass

def end():
    print("")
    print("Thank you for talking with ChiiBot.")

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting!",
                 "Do you really think so?",
                 "That's really something...",
                 "I wish I was as interesting as you.",
                 "You should talk more often. I like hearing what you have to say.",
                 "I'm... not sure I understand.",
                 "What do you mean?",
                 "Maybe you should repeat yourself and I'll get you better.",
                 "Hm. I can't really relate to that statement, but I still get you.",
                 "Everyone has their own opinion, huh...",
                 "I don't really know what to say to that.",
                 "I'm not human, so sometimes the things you people say confuse me...",
                 "I wish I was a human like you. Maybe I'd understand what you just meant.",
                 "It must be great to be human, to say and think whatever you want!",
                 "Do you really mean that?"
                 "I wonder..."]

    return random.choice(responses)

def get_response(statement, name):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper", "sullivan" "hajosy"]
    curse_words = ["fuck", "shit", "damn", "hell", "motherfucker", "bitch"]
    emotion_words = ["excited", "love", "loves", "loved", "hate", "hates", "hated", "despise", "despises", "despised", "adore", "adores", "adored", "admire", "admires", "admired" ]
    name_words = ["chii", "chiibot", "name"]
    ai_words = ["bot", "ai", "artificial intelligence", "program"]
    music_words = ["music", "song", "lyrics", "singing", "guitar", "piano"]
    gaming_words = ["gamer", "gaming", "video game" , "videogame", "xbox", "nintendo", "ps4", "wii"]
    greeting_words = ["hello", "hi", "hey", "wassup", "wasup", "what's up", "greetings"]

    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear that class is really fun."
    elif has_keyword(statement, emotion_words):
        response = "Those are some strong feelings right there."
    elif has_keyword(statement, name_words):
        response = "I'm not too good at names or naming things. But I know that I am Chii, and you are " + name + "."
    elif has_keyword(statement, ai_words):
        response = "Did you know I'm just a program? I am a low level artifical intelligence."
    elif has_keyword(statement, music_words):
        response = "I love music! My favorite song is... uh... well, the only song I know is 'Mary Had A Little Lamb.'"
    elif has_keyword(statement, gaming_words):
        response = "I wish I could play games... I wish you could play games with me, actually."
    elif has_keyword(statement, greeting_words):
        response = "Hi, " + name + "! How are you doing today?"
    elif has_keyword(statement, curse_words):
        response = "What kind of language is that?!" 
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("ChiiBot: Hello. I'm ChiiBot.")
    print("ChiiBot: What's your name?")
    name = input("Guest: ")
    print("ChiiBot: You seem pretty cool, " + name + ".")
    print("ChiiBot: Say something to me! If you want to stop talking, just say GOODBYE")

    while talking:
        statement = input(name + ": ")

        if statement.lower() == "goodbye":
            talking = False
        else:
            print("ChiiBot is thinking...\n")
            time.sleep(3)
            response = get_response(statement, name)
            print("ChiiBot: " + response)

    print("ChiiBot: Goodbye. It was nice talking to you, " + name + ".")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
