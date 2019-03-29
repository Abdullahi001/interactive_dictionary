import json

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "This word does not exist. Please double check."

word = input('Enter word: ')

print(translate(word))
