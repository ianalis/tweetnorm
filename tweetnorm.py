import json

def is_oov(word, lexicon='/home/ianalis/instru/tweetnorm/aspell.json'):
    """Return True if word is out-of-vocabulary"""
    lexicon = json.load(open(lexicon))
    return word not in lexicon

def normalize(text):
    """Return normalized text"""
    for token in text.split():
        if token[0] not in ('@', '#'):
            is_oov(token)
    return text