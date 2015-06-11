#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Tkinter import *
from pygame import *

########### GAME INITIALIZING ###########

root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(960,690))
import sys
import StringIO


########### VARIABLES ###########

#Lesson1_Intro = "Welcome to Lesson 1 of our Python Tutorial.\n\n\n\n First of we learn what variables are and how to use them. \
#After that we will learn about lists, for-loops and other stuff. After that you will be all set to start your own little python programming\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
Lesson0_0_Text = "Herzlich willkommen zu unserem Pythonlerntutorial! \n\nImmer wenn du ein Abenteuer bestanden" \
           " hast wirst du mit einer Python Lektion belohnt und kannst so spielerisch Programmieren lernen.\n"\
           "Dabei wirst du Schritt für Schritt in eine der meist verwendeten Skriptsprachen, Python, eingeführt.\n\n"\
           "Zum Verständnis der Aufgaben werden die Befehle und vorgegebene Begriffe in spitze Klammern <Befehl> gesetzt.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson0_0_GivenCode = ""
Lesson0_0_SolutionCode = ""

Lesson0_0_StringBoolean = False
Lesson0_0_SolutionOutput =""

Lesson0_0_AddedCodeBoolean = False
Lesson0_0_AddedCode = ""

Lesson0_0_Name = "Intro"

# Text: Introduction and tasks

# GivenCode: given Code at the beginning
# SolutionCode: What we want them to programm

# StringBoolean: True if String Checking is needed for this lesson
# SolutionOutput: expected String

# AddedCodeBoolean: True if Variable value checking is needed for this lesson
# AddedCode: variable value checking code

Lesson_Number = 0


Lesson1_0_Text = "Lektion 1.0: \n\nWillkommen zu deiner ersten Lektion.\n\n Jedes Programm muss mit der Welt kommunizieren können, " \
                  "dazu gibt es in Python die Funktion <print> (ausdrucken/ausgeben). \n\n\nDas einfachste Beispiel " \
                  "hierfür ist sich 'Hello World' ausgeben zu lassen. Hierfür muss der Befehl <print> und die gewünschte " \
                  "Ausgabe in Anführungszeichen Hello World eingegeben werden.\n\n\nAufgabe: \n\nGeben Sie folgenden Satz aus: \n" \
                  "'Python ist KEINE Schlange'.\n\n\nAchte auf Groß- und Kleinschreibung!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_0_GivenCode = "print 'Hello World'"
Lesson1_0_SolutionCode = "print 'Python ist KEINE Schlange'"

Lesson1_0_StringBoolean = True
Lesson1_0_SolutionOutput ="Python ist KEINE Schlange"

Lesson1_0_AddedCodeBoolean = False
Lesson1_0_AddedCode = ""
Lesson1_0_Name = "Print"
    # Test Lektion Added Code
    #"\nif (x == 6):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable x hat einen falschen Wert')" \
    #"\nif (y == 4):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable y hat einen falschen Wert')"

#####################

Lesson1_1_Text = "Lektion 1.1:\n\nUm Werte und Ergebnisse in einem Programm wieder verwenden zu können," \
                 " gibt es in Programmiersprachen Variablen. \nDiese haben einen Namen und können " \
                 "mit verschiedenen Arten von Werten belegt werden. Für den Namen können " \
                 "Groß- und Kleinbuchstaben, Ziffern und das Zeichen _ (Unterstrich) verwendet werden.\n" \
                 "Das erste Zeichen darf aber keine Ziffer sein und es dürfen keine " \
                 "reservierten Wörter der Programmiersprache verwendet werden. \n\n\n" \
                 "Wie in der Mathematik kann man mit diesen Variablen die Grundrechenarten " \
                 "Addition ( + ), Subtraktion ( - ), Multiplikation ( * ) und Division ( / )  verwenden.\n" \
                 "Dabei kann sowohl mit ganzen Zahlen (Integer) als auch mit Fließkomma Zahlen " \
                 "(Floats) gerechnet werden. Bei Floats wird wie im Englischen üblich der . (Punkt) " \
                 "statt dem Komma verwendet.\n\n\n\n" \
                 "Aufgabe: \n\nWeisen Sie der Variablen x die Differenz aus 14.56 - 7 zu " \
                 "und geben sie mit print das Ergebnis aus. Berechnen Sie ebenfalls für y das " \
                 "Produkt von 35 * 49 und für z den Quotienten von 50.4 / 3.6 und geben Sie " \
                 "jeweils in dieser Reihenfolge (x,y,z) das Ergebnis aus.\n\n\n\n\n\n\n"

Lesson1_1_GivenCode = "x = 3 + 1732\nprint x"
Lesson1_1_SolutionCode = "x = 14.56 - 7\nprint x\ny = 35 * 49\nprint y\nz = 50.4 / 3.6\nprint z"

Lesson1_1_StringBoolean = True
Lesson1_1_SolutionOutput ="7.56\n1715\n14.0"

Lesson1_1_AddedCodeBoolean = True
Lesson1_1_AddedCode =  \
    "\nif (x == (14.56 - 7):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable x hat einen falschen Wert')" \
    "\nif (y == 1715):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable y hat einen falschen Wert')" \
    "\nif (z == 14.0):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable z hat einen falschen Wert')"

Lesson1_1_Name = "Integer Variablen und Rechenzeichen"


Lesson1_2_Text = "Lektion 1.2: \n\nUm nicht nur mit Zahlen arbeiten zu können, sondern auch mit Texten gibt es auch Variablen " \
                 "für Zeichenketten (Strings). Die Zuweisung erfolgt dadurch, dass die Entsprechende Zeichenkette " \
                 "in 'String' (Anführungsstrichen) gesetzt wird. Für Zeichenketten gibt es Operationen + und *. " \
                 "Bei + werden die Inhalte zweier Stringvariablen aneinander gehängt, bei * kann die " \
                 "Stringvariable mit einer ganzen Zahl multipliziert werden. \n\n\n\nAufgabe:\n\n" \
                 "Geben sie in das Schriftfeld den Variablennamen <bunteblume> ein und  belegen Sie ihn " \
                 "indem sie den Wert 'Rot' und den Wert 'gelb' addieren. Weißen sie den Variablen <glück> " \
                 "den Wert 'toi ' (Vergiss nicht das Leerzeichen!)und <wunsch> den Wert 'für die Prüfung' zu und addieren sie zu 3*<glück> <wunsch> " \
                 "hinzu und weisen sie dies <glückwunsch> zu. \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_2_GivenCode = "blume = 'Gruen'\nprint blume\n\nHeyhey ='Hello '+'World'\nprint Heyhey\n\ncolours = 'red'*3\nprint colours"
Lesson1_2_SolutionCode = "bunteblume = 'Rot' + 'gelb'\nglueck = 'toi'\nwunsch = ' fuer die Pruefung'\nglueckwunsch= glück'*3 + wunsch"

Lesson1_2_StringBoolean = True
Lesson1_2_SolutionOutput ="toi toi toi fuer die Pruefung"

Lesson1_2_AddedCodeBoolean = True
Lesson1_2_AddedCode = \
    "\nif (glueck == 'toi '):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (wunsch == 'fuer die Pruefung'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (glueckwunsch == 'toi toi toi fuer die Pruefung'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueckwunsch hat einen falschen Wert')" \
    "\nif (bunteblume == 'Rotgelb'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable bunteblume hat einen falschen Wert')"
    #"\nif (glueck == 'toi'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')"

Lesson1_2_Name = "String Variablen"


global maxLessons
maxLessons = 3




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
    if Lesson_Number == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    if Lesson_Number == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    if Lesson_Number == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    if Lesson_Number == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    if Lesson_Number > 3:
        1+1 # Return to the game!




global Errorlist
Errorlist = []
global GlobalOutput
GlobalOutput = ""

# This function is completely generic
def checkStringCode(output_Solution):
    global Errorlist
    global GlobalOutput

    Errorlist=[]
    bb = True
    cc = True

    # GlobalOutput often has "\n" at the end.
    # To delete them to be able to check it against a solution we need this block:

    # Delete following tabs, blanks and newlines of the GlobalOutput
    while bb == True:
        a = GlobalOutput[len(GlobalOutput)-1]
        if a == " " or a == "\t" or a == "\n":
            GlobalOutput = GlobalOutput[0:len(GlobalOutput)-1]
        else:
            bb = False
    # Deleting leading newlines of the GlobalOutput
    while cc == True:
        a = GlobalOutput[0]
        if a == "\n":
            GlobalOutput = GlobalOutput[1:len(GlobalOutput)]
        else:
            cc = False


    # Check if user output == desired output
    if GlobalOutput == output_Solution:
        1+1 # all good
    else:
        Errorlist.append("Die Ausgabe ist nicht korrekt!")
        #Errorlist.append("Müsste sein: "+output_Solution)



# Execute Code
def checkRunCode():
    global cmdfield
    global textfield
    global Errorlist
    global GlobalOutput
    global Lesson_Number
    global button1

    SolutionCode = ""

    StringBoolean = ""
    SolutionOutput = ""

    AddedCodeBoolean = ""
    AddedCode = ""

    if Lesson_Number == 0:
        SolutionCode = Lesson0_0_SolutionCode
        StringBoolean = Lesson0_0_StringBoolean
        SolutionOutput = Lesson0_0_SolutionOutput
        AddedCodeBoolean = Lesson0_0_AddedCodeBoolean
        AddedCode = Lesson0_0_AddedCode

    if Lesson_Number == 1:
        SolutionCode = Lesson1_0_SolutionCode
        StringBoolean = Lesson1_0_StringBoolean
        SolutionOutput = Lesson1_0_SolutionOutput
        AddedCodeBoolean = Lesson1_0_AddedCodeBoolean
        AddedCode = Lesson1_0_AddedCode

    if Lesson_Number == 2:
        SolutionCode = Lesson1_1_SolutionCode
        StringBoolean = Lesson1_1_StringBoolean
        SolutionOutput = Lesson1_1_SolutionOutput
        AddedCodeBoolean = Lesson1_1_AddedCodeBoolean
        AddedCode = Lesson1_1_AddedCode

    if Lesson_Number == 3:
        SolutionCode = Lesson1_2_SolutionCode
        StringBoolean = Lesson1_2_StringBoolean
        SolutionOutput = Lesson1_2_SolutionOutput
        AddedCodeBoolean = Lesson1_2_AddedCodeBoolean
        AddedCode = Lesson1_2_AddedCode


    Errorlist=[]

    cmd.configure(state='normal')

    textfield= txt.get(1.0,END)

    # create file-like string to capture output
    codeOut = StringIO.StringIO()
    codeErr = StringIO.StringIO()

    code = textfield

    # capture output and errors
    sys.stdout = codeOut
    sys.stderr = codeErr

    try:
        exec code
    except:
        print "Unexpected error:", sys.exc_info()[0]


    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    codeErrors = codeErr.getvalue()
    codeOutput = codeOut.getvalue()

    # For String checking
    GlobalOutput = codeOutput

    codeOut.close()
    codeErr.close()


    cmdfield = "------------------------------Kommandozeile------------------------------\n"

    errorValue = ""
    # Display negative Results (errors)
    if codeErrors == "":
        # code is executable without errors
        if StringBoolean:
            checkStringCode(SolutionOutput)
        if AddedCodeBoolean:
            addCode(AddedCode)
        if Errorlist == []:
            # code is executable and no variable value errors
            1+1
        else:
            # Errors found during variable value check
            for x in Errorlist:
                errorValue = errorValue + x + "\n"

            cmdfield = cmdfield + "### Fehler! #### \n%s\n" % errorValue
    else:
        # Errors found during execution
        cmdfield = cmdfield + "### Fehler! ### \n%s\n" % codeErrors


    message = ""
    # Display positive results
    if codeErrors == "" and errorValue == "":
        message = "Gut gemacht! Klicke auf 'Weiter' um die nächste Aufgabe zu beginnen!"
        if (button1.winfo_exists() == 0):
            button1 = Button(root, text='Weiter', command = nextLesson )
            button1.grid(row=3, column=3)

    cmdfield = cmdfield + "### Ausgabe #### \n%s\n" % codeOutput
    cmdfield = cmdfield + "\n" + message


    cmd.delete(1.0,'end')
    # Insert original state
    cmd.insert(1.0,cmdfield, END)
    cmd.configure(state='disabled')



# check variable values
def addCode(addedCode):
    global cmdfield
    global textfield
    global Errorlist


    textfield= txt.get(1.0,END)

    textfield = textfield + addedCode


    codeOut2 = StringIO.StringIO()
    codeErr2 = StringIO.StringIO()

    code = textfield

    sys.stdout2 = codeOut2
    sys.stderr2 = codeErr2

    try:
        exec code
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sys.stdout2 = sys.__stdout__
    sys.stderr2 = sys.__stderr__

    # not needed? all errors were reported earlier
    #codeErrors2 = codeErr2.getvalue()
    #codeOutput2 = codeOut2.getvalue()

    codeOut2.close()
    codeErr2.close()


def nextLesson():
    global Lesson_Number
    global button1

    Lesson_Number += 1

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons
    # Change Text
    if Lesson_Number == 0:
        label1.config(text=Lesson0_0_Text)
    if Lesson_Number == 1:
        label1.config(text= Lesson1_0_Text)
    if Lesson_Number == 2:
        label1.config(text= Lesson1_1_Text)
    if Lesson_Number == 3:
        label1.config(text= Lesson1_2_Text)
    if Lesson_Number > 3:
        1+1 # Return to the game!

    # Change Code
    txt.delete(1.0,'end')

    if Lesson_Number == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    if Lesson_Number == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    if Lesson_Number == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    if Lesson_Number == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    if Lesson_Number > 3:
        1+1 # Return to the game!

    button1.destroy()


global buttonlesson0
global buttonlesson1
global buttonlesson2
global buttonlesson3

def lesson0():
    global Lesson_Number
    global button
    global button1
    global button2
    global button3

    deletebuttons()

    label1.config(text= Lesson0_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson0_0_GivenCode, END)

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    Lesson_Number = 0

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=3, column = 1)
    button1 = Button(root, text='Weiter', command = nextLesson )
    button1.grid(row=3, column=3)
    button2 = Button(root, text ='Archive', command = archive )
    button2.grid(row=3, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =3, column = 6)


def lesson1():
    global Lesson_Number
    global button
    global button1
    global button2
    global button3

    deletebuttons()

    label1.config(text= Lesson1_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_0_GivenCode, END)

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    Lesson_Number = 1

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=3, column = 1)
    button2 = Button(root, text ='Archive', command = archive )
    button2.grid(row=3, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =3, column = 6)





def lesson2():
    global Lesson_Number
    global button
    global button1
    global button2
    global button3

    deletebuttons()

    label1.config(text= Lesson1_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_1_GivenCode, END)

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    Lesson_Number = 2

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=3, column = 1)
    button2 = Button(root, text ='Archive', command = archive )
    button2.grid(row=3, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =3, column = 6)


def lesson3():
    global Lesson_Number
    global button
    global button1
    global button2
    global button3

    deletebuttons()

    label1.config(text= Lesson1_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_2_GivenCode, END)

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    Lesson_Number = 3

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=3, column = 1)
    button2 = Button(root, text ='Archive', command = archive )
    button2.grid(row=3, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =3, column = 6)

def deletebuttons():

    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3

    buttonlesson0.destroy()
    buttonlesson1.destroy()
    buttonlesson2.destroy()
    buttonlesson3.destroy()

def archive():
    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3

    # Clear Console
    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.configure(state='disabled')
    # Clear Code field
    txt.delete(1.0,END)
    txt.insert(1.0,"", END)

    # Add to label
    label1.configure(text="")

    button.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()

    global buttonlesson0
    buttonlesson0 = Button(root, text='Lektion 0', command=lesson0 )
    buttonlesson0.grid(row=0, column = 0)

    global buttonlesson1
    buttonlesson1 = Button(root, text='Lektion 1.0', command=lesson1 )
    buttonlesson1.grid(row=0, column = 1)

    global buttonlesson2
    buttonlesson2 = Button(root, text='Lektion 1.1', command=lesson2 )
    buttonlesson2.grid(row=0, column = 2)

    global buttonlesson3
    buttonlesson3 = Button(root, text='Lektion 1.2', command=lesson3 )
    buttonlesson3.grid(row=0, column = 3)


    # list all lessons

########### GUI ###########



w = Canvas(root, width=300, height=650)
w.grid(row=0, column =0, columnspan = 4, rowspan=2)
w.create_rectangle(0, 0, 305, 655, fill="white")


c = Canvas(root, width=5, height=650)
c.grid(row=0, column =5, rowspan = 2)
c.create_rectangle(0, 0, 200, 655, fill="grey")

texter = ""


label1 = Label(root, text=texter ,  justify=LEFT, wraplength= 250, bg ="white")
label1.grid(row=0, column =0, columnspan = 4, rowspan = 2) # Needs to be in a seperate line as we configurate it later on again.
button = Button(root, text='Check Code', command=checkRunCode )
button.grid(row=3, column = 1)
button1 = Button(root, text='Weiter', command = nextLesson )
button1.grid(row=3, column=3)
button2 = Button(root, text ='Archive', command = archive )
button2.grid(row=3, column = 2)
button3 = Button (root, text='Reset Code', command=reset )
button3.grid(row =3, column = 6)

if Lesson_Number == 0:
    label1.config(text=Lesson0_0_Text)
if Lesson_Number == 1:
    label1.config(text= Lesson1_0_Text)
if Lesson_Number == 2:
    label1.config(text= Lesson1_1_Text)
if Lesson_Number == 3:
    label1.config(text= Lesson1_2_Text)


txt_frm = Frame(root,width=100, height=100).grid(row=0, column=6)
txt = Text(txt_frm,height = 27, width = 80,  bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=1 ,sticky="n")
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))

#commandozeile = Label(root, text="CommandoZeile", justify=LEFT, anchor = "n" , bg="red").grid(row=1, column=6)

cmd_frm = Frame(root).grid(row=1,column=6,sticky="nsew")
cmd = Text(cmd_frm, height = 13, width = 80, bg="white", fg="black")
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
#mixer.music.play()

#sound_flag.set_volume(0.2)
#sound_flag.play()


####### Main Loop #########

mainloop()