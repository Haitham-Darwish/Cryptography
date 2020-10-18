#!/usr/bin/env python3
'''
    Decrypt any English word encrypted by Reverse,
    Caesar or Transposition cipher

    The program idea taken from (python_code_uncoder)
    and edited by Haitham Essam
    
'''

import sys
import os
import time
from detectEnglish import isEnglish
from CaesarCipher import caesar
# we will use ailasing as we have main in our main function
from TranspositionCipherDecryption import main as mainTrans


    
    
def main(message, outputFile=''):
    '''
        Get the decrypted message
        
        Args:
            message str:
                encrypted message or the file that contain the decrypted message
            
            outputFile str:
                The file that we will write the decrypted message in it.
    '''
    
    # if True then not entered a file
    # if False then entered a file 
    # then open file and enter the decrypted message in it
    flag = True
    
    # Check if entered a file or the actual message
    if message.endswith(".txt"):
        while True:
                
            try:    
                with open(message) as file:
                    message = file.read()
                flag = False
                
                if outputFile == '':
                    outputFile = input('Enter the decryption file name: ')
                if __name__=="__main__":
                    if os.path.exists(outputFile):
                        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' 
                              % outputFile)
                        response = input('>>>')
                        if not response.lower().startswith('c'):
                            return False
                        #sys.exit()
                break
            except FileNotFoundError:
                print("This file doesnot exist, please try again ")
                message = input("Enter the file name: ")
    
    startTime = time.time()
    def write_in_file(message):
        '''
            Write the decryption in the file
        '''
        
        # if get error then the user doesn't enter file name
        try:
            outputFileObj = open(outputFile,'w')
            outputFileObj.write(message)
            outputFileObj.close()
            
        except:
            pass
    
    LETTERS = '!"#$%&\'()+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    
    #Reverse CIPHER
        
    # Check if encrypted by Reverse Cipher   
    if isEnglish(message[::-1]):
        if(flag):
            print("\nThe message is ciphered by  Reverse cipher "
              + "and the decryption is %s" % message[::-1]  )
        else:
            write_in_file(message[::-1])
        print(f"It took {round(time.time() - startTime, 2)} seconds to decrypt")
        return True
        #sys.exit()
    else:
        print("\nThe message is not ciphered by  Reverse cipher" )
        
    #Caesar cipher
    
    # Decrypt by checking all possible keys
    for key in range(len(LETTERS)):
    
        # Check if encrypted by Caesar Cipher
        if(caesar(key, message)[0]):
            print("\nThe message is encrypted by caeser cipher")
            if(flag):
                print(" and the decrypted message is %s and  the key is %s"
                                            % (caesar(key, message)[1], key)
                     + "\n\nWe have detected the way of ciphering so the"
                     + " program will be exited \nQuiting....." )
            else:
               write_in_file(caesar(key, message)[1])
            
            print(f"It took {round(time.time() - startTime, 2)} "
                             + "seconds to decrypt")
            return True
            #sys.exit(0)
      
        
    # Trasposition Cipher
    # Decrypt by checking all possible keys
    for key in range(1, len(LETTERS)):
        
        # Check if encrypted by Trasposition Cipher
        if(mainTrans(key, message)[0]):
            print("\nThe message is ciphered by  "
                  + "Trasposition cipher and the key is ", key, end="")
            if(flag):
                 print("and the decryption is %s" % mainTrans(key, message)[1])
            else:
                # Save it in the file
                write_in_file(mainTrans(key, message)[1])
        
            print(f"\nIt took {round(time.time() - startTime, 2)} "
                             + "seconds to decrypt")
            return True
            #sys.exit()
    
    
    # Product Cipher caesar first
    # Decrypt by checking all possible keys
    for key in range(1, len(LETTERS)):
        # In case if both have different keys
        for key2 in range(len(LETTERS)):
            # Check if encrypted by Trasposition Cipher
            c=caesar(key2, message,word=1,letter=10)[1]
            if(mainTrans(key, c)[0]):
                print("\nThe message is ciphered by  "
                      + "Trasposition then Caesar ciphers and there keys are ",
                      key,key2, end="")
                if(flag):
                     print("and the decryption is %s" % mainTrans(key, c)[1])
                else:
                    # Save it in the file
                    write_in_file(mainTrans(key, c)[1])
                            
                print("\n\nWe have detected the way of ciphering."+
                      "So, the program will be exit. \nQuiting....." )
                print(f"\nIt took {round(time.time() - startTime, 2)} "
                                 + "seconds to decrypt")
                return True
                #sys.exit()
    
    # Product Cipher Transposition first
    # Decrypt by checking all possible keys
    for key in range(len(LETTERS)):
        # In case if both have different keys
        for key2 in range(1, len(LETTERS)):
            # Check if encrypted by Caesar Cipher
            c=mainTrans(key2, message,word=1,letter=10)[1]
            if(caesar(key, c)[0]):
                print("\nThe message is encrypted by Caesar then Trasposition"+
                      "ciphers and there keys are %s %s"%(key, key2))
                if(flag):
                    print(" and the decrypted message is %s" % (caesar(key, c)[1]))
                else:
                   write_in_file(caesar(key, c)[1])
                
                print("\n\nWe have detected the way of ciphering."+
                      "So, the program will exit. \nQuiting....." )
                print(f"It took {round(time.time() - startTime, 2)} "
                                 + "seconds to decrypt")
                return True
                #sys.exit()
      
    
if __name__=="__main__":
    message = input("Enter the message: ")
    main(message)
    