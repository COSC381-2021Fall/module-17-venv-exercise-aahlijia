import emoji
import pyjokes
import pyfiglet

response = input('Do you like python? y/n: ')
if response == 'y':
    print(emoji.emojize('Python is :thumbs_up:'))
    print(pyjokes.get_joke(language="en", category="all"))
else:
    print(emoji.emojize('Python is :thumbs_down:'))
    print(pyfiglet.figlet_format("LAME"))












