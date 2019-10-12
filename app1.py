#The first app in the 10ProjectsPython
import json

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist."

word = input("Enter the word: ").lower()


print(translate(word))
