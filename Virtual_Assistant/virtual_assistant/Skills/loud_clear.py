import builtins
import pyttsx3
import speech_recognition as sr
from my_users import Alpha_Prime
import webbrowser
from formal import welcome,finalizing
from my_users import Alpha_Prime
from greetings import current_time
import sys

def speak(user_command):
    # to be implemented to help with the speaker(male voice)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    engine.say(user_command)
    engine.runAndWait()


def listen():
    # can understant what the user says and process it accordingly
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source, duration=1)
        microphone.pause_threshold = 1.0
        print('Say something...')
        audio = microphone.listen(source)
        
        try:
            query = microphone.recognize_google(audio, language='en-US')
            print(f'{Alpha_Prime.user_name} said: {query}')
            
            if 'time' in query or 'hour' in query or 'today' in query:
                speak(current_time())
                return 'None'
            
            elif 'exit' in query or 'quit' in query:
                speak(finalizing())
                sys.exit()
            elif 'assis' in query:
                speak(welcome())
            #to open a browser:     
            elif 'open' in query:
                domain = query.lower().split('open')[1]
                if 'google' in domain:
                    speak('Opening Google for you.')
                    webbrowser.open_new_tab(f'https://www.google.com')
                elif 'wikipedia' in domain:
                    speak('The Wikipedia is open.')
                    webbrowser.open_new_tab(f'https://en.wikipedia.org/wiki/')
                elif 'youtube' in domain:
                    speak('Here is your YouTube.')
                    webbrowser.open_new_tab(f'https://www.youtube.com')
                elif 'chat gpt' in domain:
                    webbrowser.open_new_tab(f'https://chat.openai.com/chat')
                else:
                    speak(f'Searching for {domain}.')
                    webbrowser.open(f"https://www.google.com/search?q={domain}")
                          
            return query
        
        except sr.UnknownValueError:
            print("Don't get it!Say again, please")
            return 'Error: UnknownValueError'

        except  sr.RequestError:
            print('could not request results')
            return 'Error: RequestError'
        
# Keep the code running and listening until the user triggers it with the keyword "Alexa"
while True:
    result = listen()
    # Check if the keyword "Assis" was recognized
    if 'Assis' in result:
        print('Keyword "Assis" recognized, triggering assistant...')
        # Perform some action based on the recognition of the keyword "Assis"
        speak(welcome())
    elif 'Stop' in result:
        builtins.quit()
        
    # Check the result and take action based on it
    if result == 'None':
        pass
    elif 'Error' in result:
        print(result)
    else:
        print(f'Successfully recognized user command: {result}')
        