def count(strList):
    countDict = {}
    for word in strList:
        if word in countDict:
            countDict[word] += 1
        else:
            countDict[word] = 1
    return countDict




if __name__ == "__main__":
    sentence = input("Enter the sentence:")
    strList = list(map(str, sentence.split()))
    print(count(strList))
    