# Programmers: Shawn McDermott, 

''' Description:
        This program will allow you to save multiple strings
        into a GUI in order to be copied onto your clipboard
        at any time using a series of hotkeys.

        Hotkeys (for now): 
                (z + 0) - (z + 9) == copy
                (x + 0) - (x + 9) == paste
'''
import tkinter, pyperclip, keyboard

def copy_triggered():
        print('copy detected')

def paste_triggered():
        print('paste detected')

for i in range(10):
        copyCombo = 'z +' + str(i)
        keyboard.add_hotkey(copyCombo, copy_triggered)

for i in range(10):
        pasteCombo = 'x +' + str(i)
        keyboard.add_hotkey(pasteCombo, paste_triggered)

keyboard.wait() 

