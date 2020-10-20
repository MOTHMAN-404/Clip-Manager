# Programmers: Shawn McDermott, 

''' Description:
        This program will allow you to save multiple strings
        into a GUI in order to be copied onto your clipboard
        at any time using a series of hotkeys.

        Hotkeys (for now): 
                (z + 0) - (z + 9) == copy
                (x + 0) - (x + 9) == paste
'''
import pyperclip, keyboard, time
import pyautogui as py
from tkinter import Tk, Label, mainloop 
from tkinter.ttk import Frame

# Creates empty GUI
class GUI:
        def __init__(self, master):
                self.master = master
                self.label = Label(self.master, text='Hey bitch boi, yea you')
                self.label.pack()

# When a copy hotkey is pressed
def copy_triggered():
        py.hotkey('ctrl', 'c') # Copy highlighted text
        time.sleep(.01)        # Wait .01 sec
        text = pyperclip.paste() # Pass copied text into text
        print(text) # Test to ensure it's working - delete later
        #updateGUI(text) 
        #       --  need to add function to update the gui with added text
        

# When a paste hotkey is pressed
def paste_triggered():
        print('paste detected')
        # Need to make the GUI first to add this functionality 
        # Should take the text from corresponding row of the GUI
        # And paste it into the text-field

# Creates the hotkeys
def createHotkeys():
        for i in range(10):            
                copyCombo = 'Home +' + str(i)     # Copy hotkeys 0-9
                pasteCombo = 'Insert +' + str(i)    # Paste hotkeys 0-9
                keyboard.add_hotkey(copyCombo, copy_triggered) # When combo is detected
                keyboard.add_hotkey(pasteCombo, paste_triggered) # Call the triggered functions

def makeWindow():
        #root = Tk()
        #root.geometry('500x600')
        #gui = GUI(root)

# Main function
def main():
        createHotkeys()
        #root.mainloop()
        keyboard.wait('esc') #Ends program when escape is pressed

# Calls main function when the program starts
if __name__ == "__main__":
        main()
