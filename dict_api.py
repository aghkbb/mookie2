import requests
from PyDictionary import PyDictionary

def get_meaning(word):
    dictionary=PyDictionary()
    result = dictionary.meaning(word)
    if result:
        return dictionary.meaning(word).get("Noun")[0]
    else:
        return None

if __name__ == "__main__":
    print(get_meaning("trumpet"))