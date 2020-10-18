# Detect English module
# To use type this code:
# from detectEnglish import isEnglish
# There must be a dictionary.txt in the same directory 
# with all English words word per line
# isEnglish(sometring)
# you can downlad this from https://inventwithpython.com/dictionary.txt

UPPERCASELETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERCASELETTER + UPPERCASELETTER.lower() + '\t\n'
def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
        
    dictionaryFile.close()
    return englishWords

ENGLISH_WORD = loadDictionary()
def getEnglishCount(message):
    message = message.upper()
    message = removeNoneLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORD:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNoneLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message , wordPercentage = 20 , letterPercentage = 85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNoneLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    letterMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and letterMatch
    