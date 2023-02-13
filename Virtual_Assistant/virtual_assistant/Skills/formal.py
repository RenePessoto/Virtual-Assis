import random
from my_users import Alpha_Prime
from greetings import current_time, greets

# INVOKES THE FUNCTION EVERYTIME YOU CALL THE ASSISTANT.

def initializing():

    initial = 'Initializing Cognition...\n \
        Starting all systems applications...\n \
        Installing and checking all drivers...\n \
        Caliberating and examining all the core processors...\n\
        Checking the internet connection...\n \
        Wait a moment \n All drivers are up and running \n systems have been activated...\n\
        Now I am online!!!'
    print (initial)
    return initial


def welcome():
    """
    this says the greetings randomly according time and
    get the weather of user's location if wished
    """
    pronouns = [
        'Sir',
        'Master',
        'Creator',
        'My Creator',
        Alpha_Prime.user_name,
    ]
    user = random.choice(pronouns)
    moment = current_time()
   

    part_one = [
        'Hi ',
        'Hello ',
        'Whats up! ',
        'Greetings ',
        'Namastê ',
        'Nice too see you!',
        'May I Help you?',
        'How Are You?',
    ]
    part_two = [
        "Hope you're having a great week",
        "Hope you're having a great day",
        "Hope you're doing well",
        "Hope you're doing good",
    ]

    first = random.choice(part_one)
    second = random.choice(part_two)

    greetings = f'\n{greets()}\n{first} {user}, {second}!\n'
    print(greetings)
    return greetings


def finalizing():
    final = [
        'OK dok',
        'see you soon',
        'wish something else?',
        'if you need me, you know where to look for',
        'glad to help',
    ]
    fnl = random.choice(final)
    print(fnl)
    print('finalizing...')
    return fnl