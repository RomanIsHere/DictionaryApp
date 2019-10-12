#The first app in the 10ProjectsPython
import json
import  difflib
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        match = input("You mean %s instead? " % get_close_matches(word,data.keys())[0]).lower()
        if match == "yes":
            return data[get_close_matches(word,data.keys())[0]]
        elif match == "no":
            return "Then the word doesn't exist."
        else:
            return "Please choose 'yes' or 'no' for your answear."
    else:
        return " The word doesn't exist."


word = input("Enter the word: ").lower()


print(translate(word))






