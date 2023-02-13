import webbrowser
from loud_clear import speak

def open_site(phrase):
    domain = phrase.lower().split('open')[1]
    if 'google' in domain:
        speak('Opening Google for you.')
        webbrowser.open_new_tab(f'https://www.google.com')
    elif 'wikipedia' in domain:
        speak('The Wikipedia is open.')
        webbrowser.open_new_tab(f'https://en.wikipedia.org/wiki/')
    elif 'youtube' in domain:
        speak('Here is your YouTube.')
        webbrowser.open_new_tab(f'https://www.youtube.com')
    else:
        speak(f'Searching for {domain}.')
        webbrowser.open(f"https://www.google.com/search?q={domain}")

def get_it(phrase):
    key_word = 'search for'
    answer = [x for x in phrase.split(key_word)[1] if x not in phrase]
    webbrowser.open_new_tab(f"https://www.google.com/search?q={answer}")
    webbrowser.open_new_tab(f'https://pt.wikipedia.org/wiki/{answer}')
    
def website_opener(query):
    domain = query.split('open')[1]
    try:
        url = (f'https://www.'+{domain}+'.com')
        webbrowser.open_new_tab(url)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    ...