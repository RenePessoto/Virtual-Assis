from  .Skills import commands, loud_clear


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
                
            take_command(query)
                
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
        speak(listen())
    elif 'Stop' in result:
        builtins.quit()
        
    # Check the result and take action based on it
    if result == 'None':
        pass
    elif 'Error' in result:
        print(result)
    else:
        print(f'Successfully recognized user command: {result}')
        