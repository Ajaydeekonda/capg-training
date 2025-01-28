def palindrome(word):
    # word_char = list(word)
    # s = 0
    # e = len(word) -1
    # while s < e:
    #     if word_char[s] != word_char[e]:
    #         return False
    #     s += 1
    #     e -=1
    # return True
    
    rev_word = word[::-1]
    if rev_word == word:
        return True
    return False

def main():
    word = input("Enter a word: ")
    if palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
main()


