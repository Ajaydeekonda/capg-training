def stringAnalyser(string):
    vowels = 0
    consonants = 0
    digits = 0
    special = 0
    rev_str = string[::-1]
    for char in string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    
    return vowels, consonants, digits, special, rev_str

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowels, consonants, digits, special, rev_str = stringAnalyser(string)
    print(f"Vowels: {vowels}, Consonants:{consonants}, digits:{digits}, specialCharacters:{special}, reverse:{rev_str}")