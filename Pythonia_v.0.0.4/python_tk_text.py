import pygame
from Tkinter import *
from pygame import *
#from python_MainGame.py import loadImage

########### GAME INITIALIZING ###########

root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(800,600))


########### VARIABLES ###########

Lesson1_Intro = "Welcome to Lesson 1 of our Python Tutorial.\n\n\n\n First of we learn what variables are and how to use them. \
After that we will learn about lists, for-loops and other stuff. After that you will be all set to start your own little python programming\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

solution1 = "var1 = ['A string is a list of characters']\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'"

Lesson1_Guide= ""
Lesson1_Control = ""

# Global Variable for the textfield
global textfield
textfield = ""



########### FUNCTIONS ###########

# Get Input for checking things
def retrieve_input():
    global textfield
    textfield = txt.get(1.0,END)
    print textfield

# Reset Code to original state
def reset():
    # Clear Code
    txt.delete(1.0,'end')
    # Insert original state
    txt.insert(1.0,"var1 = ['A string is a list of characters']\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'\n", END)


# Doesnt work yet, work with tabs / empty spaces etc
def checkCode():
    if retrieve_input == solution1:
        print "GREAT!"
    else:
        print "nope."


########### GUI ###########


w = Canvas(root, width=195, height=565)
w.grid(row=0, column =0, columnspan = 4)
w.create_rectangle(0, 0, 200, 570, fill="white")


c = Canvas(root, width=5, height=565)
c.grid(row=0, column =5)
c.create_rectangle(0, 0, 200, 570, fill="grey")

label1 = Label(root, text=Lesson1_Intro,  justify=LEFT, wraplength= 175, bg ="white").grid(row=0, column =0, columnspan = 4)
#label2= Label(root, text="     ").grid(row=1, column=0)
button = Button(root, text='Retrieve Code', command=checkCode ).grid(row=1, column = 1)
#label3= Label(root, text="        ").grid(row=1, column=2)
button1 = Button(root, text='Fill in', command = retrieve_input ).grid(row=1, column=3)
#label4= Label(root, text="   ").grid(row=1, column=4)
button2 = Button (root, text='Reset Code', command=reset ).grid(row = 1, column = 6)


txt_frm = Frame(root).grid(row=0, column=6, rowspan = 3)
txt = Text(txt_frm, relief="sunken", width = 73, height = 35, bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=3 ,sticky="nsew", pady=2)
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))

txt.pack_propagate()



######## Initialize ##############

reset()

mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
mixer.music.load("flag.wav")
mixer.music.set_volume(0.1)
mixer.music.play()

#sound_flag.set_volume(0.2)
#sound_flag.play()


####### Main Loop #########

mainloop()