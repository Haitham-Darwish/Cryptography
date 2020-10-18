# -*- coding: utf-8 -*-
#!/usr/bin/ev python3
"""
Created on Fri Oct  2 05:49:10 2020

@author: Haitham Essam
"""

from tkinter import *
from tkinter import filedialog
from CipherDecryption import main
 
root = Tk()
root.title("Text Decryption")
root.iconbitmap("Screenshots\crypto.ico")
root.geometry("400x400")
def get_file():
    root.filename = filedialog.askopenfilename(initialdir="",
                        title="Select File",
                        filetypes=(("Text Files","*.txt"),
                                   ("All File","*.*")))
    
    if output.get() != "":
        main(root.filename, output.get())
    else:    
        with open(root.filename) as file:
            main(file.read())
   
label = Label(root, text="Enter the output file name", font=('Helvetica',15),fg='#065478')     
label_note = Label(root, text="*Note if the file is already exist we will overwrite it",
                   font=('Helvetica',9,('bold','italic')),fg='red')     
output = Entry(root,font=('Helvetica',13), border=4 )
file_btn = Button(root, text="Choose a file", command=get_file,
                  font=('Helvetica'), padx=2, pady=5)

label.place(relx=0.5, rely=.3, anchor="center")
label_note.place(relx=0.28, rely=1, anchor="sw")
output.place(relx=.5, rely=.4, anchor="center")
file_btn.place(relx=.5, rely=.6, anchor="center")

root.mainloop()
