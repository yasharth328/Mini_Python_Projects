import tkinter
from PIL import Image, ImageTk
import random

# Widget which represents the main window of the application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Simulator')

# Adding some empty space at the top
l0 = tkinter.Label(root, text="")
l0.pack()

# Adding a label with a different font and adding some formatting to it
l1 = tkinter.Label(root, text="Dice Simulator in Python", fg = "white", bg = "black", font = "Helvetica 14 bold italic")
l1.pack()

# Adding the images to the list dice
dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
# Simulating the dice with random numbers between 0 to 6 and generating image
# This will add a random dice when the app opens for the first time
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Construct a label widget for the image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# Packing the widget used for image in the parent widget 
label1.pack(expand=True)

# This function assigns a random dice to the image1 variable everytime the function runs
# It is called by button click
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # Updating image
    label1.configure(image=image1)
    label1.image = image1

# Adding button
# The command argument will use the rolling_dice function so that the function could be called everytime the user clicks the button 
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice, height = 1, width = 16)

# pack a widget in the parent widget
button.pack( expand=True)

# Calling the mainloop of Tk
# It keeps the window open
root.mainloop()