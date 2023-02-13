import datetime
import random

# THE WAY TO GIVE TO THE USER TIME AND DATE
def current_time():
    """this func returns the date to the user"""
    today = datetime.datetime.now().strftime('%A, ' '%d ' '%B ' '%Y')
    hour = datetime.datetime.now().strftime('%H:' '%M:' '%S')
    period = f'Today is: {today} exactly at {hour}'
    return period

def greets():
    """greeting function according to the time"""
    this_moment = datetime.datetime.now()
    this_moment.hour

    if this_moment.hour < 12:
        morning = [
            'GOOD MORNING!!!!!',
            'SUNSHINE ON YOUR FACE!',
            'TIME TO WAKE UP!!',
            'OW! YOU REALLY NEED A COFFEE OR MORE!!!',
            'LETS GO TO THE BEACH. RIGHT NOW!',
            'DAY OFF?',
        ]
        greet = random.choice(morning)
        return greet
    elif this_moment.hour > 12 and this_moment.hour < 18:
        noon = [
            'GOOD AFTERNOON',
            'LETS TAKE A BREAK?',
            'HAVE YOU ALREADY GOT LUNCH?',
            'ANOTHER COFFEE?',
        ]
        greet = random.choice(noon)
        return greet
    else:
        night = [
            'GOOD NIGHT.',
            'TIME TO GO TO BED!',
            'zzzzz',
            'HOW WAS YOUR DAY?',
            'ENOUGH COFFEE!',
        ]
        greet = random.choice(night)
        return greet
