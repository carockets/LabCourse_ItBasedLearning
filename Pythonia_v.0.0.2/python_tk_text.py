from Tkinter import *
from pygame import mixer



root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(800,600))



# Global Variable for the textfield
global textfield
textfield = ""

# Get Input for checking things
def retrieve_input():
    global textfield
    textfield = txt.get(1.0,END)
    print textfield

def reset():
    # Clear Code
    txt.delete(1.0,'end')
    # Reset to initial state
    txt.insert(1.0,"var1 = ['A string is a list of characters']\nfor x in var1:\n\tif x == 'a':\n\t\tprint 'True for once'\n", END)



# Redundant as we programm "like a hacker". Black background and green font.
#def highlight():
#    lastline = txt.index("end-1c").split(".")[0]
#    tag = "odd"
#    for i in range(1, int(lastline)):
#        txt.tag_add(tag, "%s.0" % i, "%s.0" % (i+1))
#        tag = "even" if tag == "odd" else "odd"



Lesson1_Intro = "Welcome to Lesson 1 of our Python Tutorial. First of we learn what variables are and how to use them. \
After that we will learn about lists, for-loops and other stuff. "

Lesson1_Guide= ""
Lesson1_Control = ""


label1 = Label(root, text=Lesson1_Intro, anchor = NE,  justify=LEFT, wraplength= 175).grid(row=0, column=0, columnspan=4)
label2= Label(root, text="     ").grid(row=1, column=0)
button = Button(root, text='Retrieve Code', command=retrieve_input ).grid(row=1, column = 1)
label3= Label(root, text="        ").grid(row=1, column=2)
button1 = Button(root, text='Fill in' ).grid(row=1, column=3)
label4= Label(root, text="   ").grid(row=1, column=4)
button2 = Button (root, text='Reset Code', command=reset ).grid(row = 1, column = 5)


txt_frm = Frame(root).grid(row=0, column=2)


txt = Text(txt_frm, relief="sunken", width = 75, height = 35, bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=5, columnspan=3 ,sticky="nsew", pady=2)
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))
txt.pack_propagate(0)


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