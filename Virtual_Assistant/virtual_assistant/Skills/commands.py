
def take_command(query):
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
                            