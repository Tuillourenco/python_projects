# App's Main Code Block.
# 1. Importing dependencies.
import tkinter
from PIL import Image, ImageTk
import random

# 2. Creating a GUI window.
#top level widgets which represents the main window of the Dice Rolling Simulator in python
from PIL.ImageTk import PhotoImage
root=tkinter.Tk()
root.geometry('400x400')
root.title("PythonGeeks-Roll the Dice")

# 3. Formatting a list of images to be displayed randomly.
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

#simulating the dice with random variables 1 to 6 and generate image using Python
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
#constructing a Label widget for image
label1=tkinter.Label(root,image=image1)
label1.image=image1

#packing a widget in the parent widget
label1.pack(expand=True)

# 4.Defining roll the dice function and creating buttons:
def rolling_dice():
   image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
   #update image based on dice roll
   label1.configure(image=image1)
   #keep a reference
   label1.image=image1

#adding buttons,and command will use rolling_dice function
button=tkinter.Button(root,text="Roll the dice",fg="green",command=rolling_dice)
#pack a widget in parent widget
button.pack(expand="True")

# 5. Main Function
# call the mainloop
root.mainloop()