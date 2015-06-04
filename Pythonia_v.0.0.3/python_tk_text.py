import pygame
from Tkinter import *
from pygame import *

########### GAME INITIALIZING ###########

root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(800,600))
import sys
import StringIO





########### VARIABLES ###########

Lesson1_Intro = "Welcome to Lesson 1 of our Python Tutorial.\n\n\n\n First of we learn what variables are and how to use them. \
After that we will learn about lists, for-loops and other stuff. After that you will be all set to start your own little python programming\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_Guide= ""
Lesson1_Control = ""

# Global Variable for the textfield
global textfield
textfield = ""
cmdfield = "-----Kommandozeile-----"


########### FUNCTIONS ###########

# Get Input for checking things
def retrieve_input():
    global textfield
    textfield = txt.get(1.0,END)


def get_cmd():
    global cmdfield
    cmdfield = cmd.get(1.0,END)

def set_cmd():
    global cmdfield

    cmdfield = "-----Kommandozeile-----"

    cmd.configure(state='normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------",END)
    cmd.configure(state='disabled')


# Reset Code to original state
def reset():
    # Clear Code
    txt.delete(1.0,'end')
    # Insert original state
    txt.insert(1.0,"var1 = 'A string is a list of characters'\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'\n", END)



solution1 = "var1 = 'A string is a list of characters'\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'"

#solution1 = "his is t"

def checkEqualCode(string):
    bb = True
    cc = True
    # Delete following tabs, blanks and newlines
    while bb == True:
        a = string[len(string)-1]
        if a == " " or a == "\t" or a == "\n":
            string = string[0:len(string)-1]
        else:
            bb = False
    # Deleting leading newlines. Blanks and tabs would be errors of the programmer.
    while cc == True:
        a = string[0]
        if a == "\n":
            string = string[1:len(string)]
        else:
            cc = False

    if string == solution1:
        print "GREAT!"
    else:
        print "nope."

def checkRunCode():
    global cmdfield
    global textfield

    cmd.configure(state='normal')


    textfield= txt.get(1.0,END)

    # create file-like string to capture output
    codeOut = StringIO.StringIO()
    codeErr = StringIO.StringIO()

    code = textfield

    # capture output and errors
    sys.stdout = codeOut
    sys.stderr = codeErr

    exec code

    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    codeErrors = codeErr.getvalue()
    #print "error:\n%s\n" % codeErrors

    codeOutput = codeOut.getvalue()
    #print "output:\n%s" % codeOutput

    codeOut.close()
    codeErr.close()

    cmdfield = "------------------------------Kommandozeile------------------------------"
    if codeErrors == "":
        codeErrors = "No Errors found."
    cmdfield = cmdfield + "\n########## Found Errors ########## \n%s\n" % codeErrors
    cmdfield = cmdfield + "\n########## Results ########## \n%s \n\n" % codeOutput

    cmd.delete(1.0,'end')
    # Insert original state
    cmd.insert(1.0,cmdfield, END)
    cmd.configure(state='disabled')

#checkRunCode("var1 = 'A string is a list of characters'\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'")

def checkCode():
    retrieve_input()
    checkEqualCode(textfield)
    checkRunCode(textfield)


########### GUI ###########


w = Canvas(root, width=195, height=565)
w.grid(row=0, column =0, columnspan = 4, rowspan=2)
w.create_rectangle(0, 0, 200, 570, fill="white")


c = Canvas(root, width=5, height=565)
c.grid(row=0, column =5, rowspan = 2)
c.create_rectangle(0, 0, 200, 570, fill="grey")

label1 = Label(root, text=Lesson1_Intro,  justify=LEFT, wraplength= 175, bg ="white").grid(row=0, column =0, columnspan = 4, rowspan = 2)
#label2= Label(root, text="     ").grid(row=1, column=0)
button = Button(root, text='Check Code', command=checkRunCode ).grid(row=3, column = 1)
#label3= Label(root, text="        ").grid(row=1, column=2)
button1 = Button(root, text='Fill in', command = retrieve_input ).grid(row=3, column=3)
#label4= Label(root, text="  ").grid(row=2, column=5)
button2 = Button (root, text='Reset Code', command=reset ).grid(row =3, column = 6)


txt_frm = Frame(root,width=100, height=100).grid(row=0, column=6)
txt = Text(txt_frm,height = 25, width = 73,  bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=1 ,sticky="n")
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))

#commandozeile = Label(root, text="CommandoZeile", justify=LEFT, anchor = "n" , bg="red").grid(row=1, column=6)

cmd_frm = Frame(root).grid(row=1,column=6,sticky="nsew")
cmd = Text(cmd_frm, height = 10, width = 73, bg="white", fg="black")
cmd.config(font=("Courier", 10), undo=True, wrap='word')
cmd.grid(row = 1, column = 6, sticky="nw")
cmd.configure(state='disabled')

cmd.pack_propagate()
txt.pack_propagate()



######## Initialize ##############

reset()
set_cmd()

mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
mixer.music.load("flag.wav")
mixer.music.set_volume(0.1)
mixer.music.play()

#sound_flag.set_volume(0.2)
#sound_flag.play()


####### Main Loop #########

mainloop()