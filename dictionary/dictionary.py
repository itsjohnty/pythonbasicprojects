import json
from difflib import get_close_matches
data=json.load(open("data.json"))


def search(word):
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide=input("Enter y for yes and n for no: ")
        if(decide=="y"):
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return("Word does not exist")

    else:
        return("Word does not exist")

word=input("Enter the word to be searched: ")
word=word.lower()
output=search(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
