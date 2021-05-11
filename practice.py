import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def Translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        bestmatches = get_close_matches(w, data.keys())
        print(bestmatches)
        yn = input("Did you mean '%s' instead? Enter Y if yes, or N if no: " % bestmatches[0])
        if yn == 'Y':
            return data[bestmatches[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "Please enter Y or N."
    else:
        return "The word doesn't exist. Please double check it."


typein = input("Enter word: ")
word = Translate(typein)
if type(word) == list:
    for explanation in word:
        print(explanation)
else:
    print(word)
