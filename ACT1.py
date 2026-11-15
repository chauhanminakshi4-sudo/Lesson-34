# Import necessary libraries
from tkinter import *

# Make window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# keypress
def handler_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress to event handler_keypress()
window.bind("<Key>", handler_keypress)

# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

#Bind click event to handle_click()
button.bind("<Button-1>", handle_click)

#Start the GUI event loop 
window.mainloop()