def palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return "palindrome"
    else:
        return "Not a palindrome"
    
if __name__ == "__main__":
    
    while True:
        word = input("Enter a word or Enter -1 to stop : ")
        if word == "-1":
            break
        print(palindrome(word)) 

      
            
        