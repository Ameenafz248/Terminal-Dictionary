#!/usr/bin/python3
from sys import exit, argv
import requests
import json
import textwrap
if len(argv) != 2:
    print('Invalid format. type "define <WORD>"')
    exit()
word = argv[1]
url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
try:
    details = requests.get(url + word, timeout=10)
    if (details.status_code == 404):
        print("The word was not found")
        exit()
    if (details.status_code != 200):
        print("Some error occured. Try again")
        exit()
except (requests.ConnectionError, requests.Timeout) as exception:
    print("Connection error. Please make sure you are connected to internet")
    exit()
obj = details.json()[0]
meanings = obj['meanings']
print()
print("\033[1m" + "Word : " + "\033[1;34m" + word)
phonetic = obj.get('phonetic')
if phonetic != None:
    print("\033[3;0m" + "      " + obj['phonetic'] + "\033[1m")
else:
    phonetics = obj.get('phonetics')
    if phonetics != None:
        for x in phonetics:
            text = x.get('text')
            if text != None:
                print("\033[3;0m" + "      " + text + "\033[1m")
                break
print()
for x in meanings:
    print("\033[3;31m" + x['partOfSpeech'] + "\033[0m" + "\033[1m")
    count = 0
    for y in x['definitions']:
        count += 1
        prefix = " " + str(count) + ". "
        width = 70
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=width, subsequent_indent=' ' *len(prefix))
        print(wrapper.fill(y['definition']))
        if y.get('example') != None:
            print("\033[2m" + "    \"{}\"".format(y['example']) + "\033[0m" + "\033[1m")      
        print()
exit()
