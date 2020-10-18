#!/usr/bin/env python3
'''
    Decrypt by caesar cipher
    
    
'''
# used to copy the translated txt
import pyperclip
# used to check if the decrypted message is right 
from detectEnglish import isEnglish

# The letter that we will rotate in it to decrypt or encrypt
LETTERS = '!"#$%&\'()+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = dict()
def caesar(key, message, word=1, letter=80):
    '''
         Encrypt and decrypt by caesar cipher
         
         Args:
             int key the key that will be encrypted or decrypted by it 
             
        Return the cipher message and corresponding key as key in a dict
        and the value tuple contains true if encrypted by caesar or false 
        otherwise and the decrypted message
    '''
    
    if (key, message) in d:
        return d[(key, message)]
    else:
        message = message.upper()
        
        # The txt that will contain the encryption or decryption
        translated = ""
       
        # Encrypt or decrypt each character alone
        for  symbol in message:
            
            # if the character in the LETTERS encrypt or decrypt it
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - int(key)
    
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)
        
                translated = translated + LETTERS[num]
                
            else:
                # if not add it as it is
                translated = translated + symbol
            
        # if the mode is decryption check if the decryption is right or wrong
        if isEnglish(translated,word,letter):
            
            # make a copy for translation
            pyperclip.copy(translated)
            if key == 0:
               print("\nThe text is the plain text")
               d[(key, message)] = (True, translated.capitalize())
            else:
                d[(key, message)] = (True, translated.capitalize())
            
        
        else:
            print("\nThe message is not encrypted by "+ str(key) + 
                         " in caeser cipher \n try another one")
            d[(key, message)] =  (False, translated.capitalize())
        
        return d[(key, message)]
