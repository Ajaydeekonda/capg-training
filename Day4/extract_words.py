# import re

# def extract_words(sentence):
#     return re.findall(r'\S+', sentence)

def extract(sentence):
    words = []
    word = ""
    for c in sentence:
        if c != ' ':
            word += c
        elif word:
            words.append(word)
            word = ""
            
    return words
            

sentence = "This  is@     an    example        sentence."
words = extract(sentence)
print(words)
