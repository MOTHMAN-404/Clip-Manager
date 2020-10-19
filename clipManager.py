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
import pyautogui as py

# When a copy hotkey is pressed
def copy_triggered():
        print('copy detected')

# When a paste hotkey is pressed
def paste_triggered():
        print('paste detected')

# Main function
def main():
        for i in range(10):            
                copyCombo = 'z +' + str(i)     # Copy hotkeys 0-9
                pasteCombo = 'x +' + str(i)    # Paste hotkeys 0-9
                keyboard.add_hotkey(copyCombo, copy_triggered) # When combo is detected
                keyboard.add_hotkey(pasteCombo, paste_triggered) # Call the triggered functions
        
        keyboard.wait('esc') #Ends program when escape is pressed

# Calls main function when the program starts
if __name__ == "__main__":
        main()
