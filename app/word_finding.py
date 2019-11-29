from pandas import read_csv
from difflib import get_close_matches
from estnltk import Text

data = read_csv("sonaraamat2.csv")

word = input("Enter word: ")

def get_meaning(w):
    w = Text(w)
    w = word.tag_layer().morph_analysis["lemma"][0][0]
    w = w.lower()
    if any(data["Eesti sõna"].isin([w])):
        return data[data["Eesti sõna"] == w]
    elif len(get_close_matches(w, data["Eesti sõna"])) > 0:
        close_match = get_close_matches(w, data["Eesti sõna"])[0]
        print("Did you mean this instead?: Enter y if yes or n if no")
        print(close_match)
        choice = input()
        if choice == "y":
            return data[data["Eesti sõna"] == close_match]
        elif choice == "n":
            print("The word doesn't exist.")
        else:
            print("Sorry. We didn't understand your entry.")
    else:
        print("The word doesn't exist.")


meaning = get_meaning(word)

print("Meaning: " , meaning)
