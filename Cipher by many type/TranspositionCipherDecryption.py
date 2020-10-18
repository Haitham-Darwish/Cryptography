#!/usr/bin/env python3
'''
    Decrypt any English word encrypted Transposition cipher

    The program idea taken from (python_code_uncoder)
    and edited by Haitham Essam
'''
import math,pyperclip
from detectEnglish import isEnglish
d = dict()
def main(key, message, word=1, letter=80):
    
    '''
       Decrypt the transposition cipher
       
       Arg:
           key (int) the key that needed to decrpt the message
           message (str) the cipher message.
           
       Return:
           dictionary key is tuple of key and cipher message
           value is tuple of whether it encrypted with this
           key or not and the corresponding decrypted message.
   
    '''
    # Check if we have decrypt the message before
    if(key, message) in d:
        return d[(key, message)]
    else:
        plaintext = decrypt_message(int(key),message)
        
        # Check if the message in encrpted by this key
        if isEnglish(plaintext, wordPercentage = word ,letterPercentage=letter):
            d[(key, message)] = (True, plaintext)
        else:
            print("\nThe message is not ciphered by  Trasposition cipher" )
            d[(key, message)] = (False, plaintext)
    
        return d[(key, message)] 
        #print(plaintext + '|')
        #pyperclip.copy(plaintext)

def decrypt_message(key,message):
    numOfCols = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfCols * numOfRows) - len(message)
    plaintext = [''] * numOfCols
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfCols) or (col == numOfCols - 1 
           and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)               

 

if __name__ == '__main__':
    key=int(input("Please Enter the key"))
    message=input("Please Enter the message")
    main(key, message)
    