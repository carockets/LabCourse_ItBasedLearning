#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys
import StringIO
from Tkinter import *
from pygame.locals import *

########### GAME INITIALIZING ###########

root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(960,690))

def on_closing():
    # Empty communication_file and set it up to continue the Game
    comm_file2 = open("communication_file.txt","w")
    comm_file2.write("")
    comm_file2.close()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', on_closing)





########### VARIABLES ###########

Lesson0_0_Text = "Herzlich willkommen zu unserem Pythonlerntutorial! \n\nImmer wenn du ein Abenteuer bestanden" \
           " hast wirst du mit einer Python Lektion belohnt und kannst so spielerisch Programmieren lernen.\n"\
           "Dabei wirst du Schritt für Schritt in eine der meist verwendeten Skriptsprachen, Python, eingeführt.\n\n"\
           "Zum Verständnis der Aufgaben werden die Befehle und vorgegebene Begriffe in spitze Klammern <Befehl> gesetzt.\n\n\nUm eine Lektion abzuschließen und zur nächsten zu kommen, " \
           "klicke auf 'Check Code' - Hast du den richtigen Code programmiert wird dir das Ergebnis ausgegeben und der 'Weiter' Knopf wird eingeblendet. " \
           "Gibst du etwas falsches ein, wird dir eine Fehlermeldung angezeigt. \n\nDa wir im Moment keine Aufgabe gestellt haben, probiere es einfach mal aus und klicke auf 'Check Code'." \
           "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

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

Lesson_Number = 8
current_Lesson = 0
maxLessons = 8


comm_file = open("communication_file.txt","r")
communication = [x.strip('\n') for x in comm_file.readlines()]
comm_file.close()



if communication != []:
    current_Lesson = int(communication[0])


Lesson1_0_Text = "Lektion 1.0: \n\nWillkommen zu deiner ersten Lektion.\n\n Jedes Programm muss mit der Welt kommunizieren können, " \
                  "dazu gibt es in Python die Funktion <print> (ausdrucken/ausgeben). \n\n\nDas einfachste Beispiel " \
                  "hierfür ist sich 'Hello World' ausgeben zu lassen. Hierfür muss der Befehl <print> und die gewünschte " \
                  "Ausgabe in Anführungszeichen <'Hello World'> eingegeben werden, da in diesem Fall die Ausgabe ein String (also eine Reihenfolge von Buchstaben) ist. \n\n\nAufgabe: \n\nGeben Sie folgenden Satz aus: \n" \
                  "'Python ist KEINE Schlange'.\n\n\nPython ist sehr sensitiv wenn es um Leerzeichen und Groß- und Kleinschreibung geht! Achte darauf, dass dein Ergebnis exakt der Aufgabenstellung entspricht!\n\n\n\n\n\n\n\n\n\n\n"

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
                 "und geben sie mit <print> das Ergebnis aus. Berechnen Sie ebenfalls für y das " \
                 "Produkt von 35 * 49 und für z den Quotienten von 50.4 / 3.6 und geben Sie " \
                 "jeweils in dieser Reihenfolge (x,y,z) das Ergebnis aus.\n\n\n\n\n\n\n"

Lesson1_1_GivenCode = "x = 3 + 1732\nprint x"
Lesson1_1_SolutionCode = "x = 14.56 - 7\nprint x\ny = 35 * 49\nprint y\nz = 50.4 / 3.6\nprint z"

Lesson1_1_StringBoolean = True
Lesson1_1_SolutionOutput ="7.56\n1715\n14.0"

Lesson1_1_AddedCodeBoolean = True
boolean1 = False

Lesson1_1_AddedCode = "" \
    "\nif (x == (14.56 - 7):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable x hat einen falschen Wert')"\
    "\nif (y == 1715):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable y hat einen falschen Wert')" \
    "\nif (z == 14.0):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable z hat einen falschen Wert')"

Lesson1_1_Name = "Integer und Rechenzeichen"



Lesson1_2_Text = "Lektion 1.2 \n\nZusätzlich zu dem normalen Divisionsoperator < / > gibt es die ganzzahlige Division. Der Operator dazu ist der < // >. " \
                 "Mit diesem wird das ganzzahlige Ergebnis der Division berechnet. Zusätzlich gibt es den Modulo Operator < % > mit dem der Rest berechnet wird.\n\n\n" \
                 "Berechne den Wert von 7 geteilt durch 5 als ganzzahlige Divison, weise ihn der Variable 'GanzeZahl' zu und gebe ihn aus.  \n\n" \
                 "Zusätzlich berechne den Rest von 7 geteilt durch 5 mit Modulo, weise ihn der Variable 'mod' zu und gebe diese aus.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_2_GivenCode = "GanzeZahl = 7.2 / 2"
Lesson1_2_SolutionCode = "GanzeZahl = 7.0 // 5\nprint GanzeZahl\nmod = 7 % 5\nprint mod"

Lesson1_2_StringBoolean = True
Lesson1_2_SolutionOutput ="1.0\n2"

Lesson1_2_AddedCodeBoolean = True
Lesson1_2_AddedCode = \
    "\nif (GanzeZahl == 1.0):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable GanzeZahl hat einen falschen Wert')" \
    "\nif (mod == 2):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable mod hat einen falschen Wert')" \

Lesson1_2_Name = "Modulo 1"



Lesson1_3_Text = "Lektion 1.3 \n\nBevor wir nun richtig loslegen folgen noch ein paar einfache Rechenaufgaben. " \
                 "Brian wohnt 42km entfernt von Monty. Monty weiß, dass er für jeden Kilometer " \
                 "25 cent mit der Bahn zahlen muss. Zusätzlich benötigt er noch ungefähr 15 Euro um sich " \
                 "für die Reise ein Buch und eine Cola zu kaufen. Lege eine Variable mit dem Namen " \
                 "'fahrpreis' an und berechne wieviel Monty's Hin- und Rückreise (Kilometerpauschale + sonstige Ausgaben)" \
                 " kostet. Wir nehmen an, dass Monty das Buch und die Cola nur einmal kauft. \n" \
                 "Gebe den Wert der Variable auf dem Bildschirm aus. \n\n" \
                 "Monty zahlt grundsätzlich nur mit 5 Euro Scheinen.\n\n" \
                 "Wie viel Wechselgeld bekommt Monty zurück wenn er sich Fahrkarten kauft um Brian zweimal zu besuchen?" \
                 "Berechne den Wert mit Modulo (wie du es in der vorherigen Aufgabe gelernt hast) und weise ihn der Variable 'Wechselgeld' zu!\n" \
                 "Gebe anschließend die Variable 'Wechselgeld' mit <print> aus.\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_3_GivenCode = "fahrpreis = \nWechselgeld = "
Lesson1_3_SolutionCode = "fahrpreis = ((42 * 0.25) * 2) + 15\nprint(fahrpreis)\nWechselgeld = (fahrpreis *2)%5"

Lesson1_3_StringBoolean = True
Lesson1_3_SolutionOutput ="36.0\n1.0"

Lesson1_3_AddedCodeBoolean = True
Lesson1_3_AddedCode = \
    "\nif (fahrpreis == ((42 * 0.25) * 2) + 15):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable fahrpreis hat einen falschen Wert')" \
    "\nif (Wechselgeld == 1):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable Wechselgeld hat einen falschen Wert')" \

Lesson1_3_Name = "Modulo 2"



Lesson1_4_Text = "Lektion 1.4: \n\nUm nicht nur mit Zahlen arbeiten zu können, sondern auch mit Texten gibt es auch Variablen " \
                 "für Zeichenketten (Strings). Die Zuweisung erfolgt dadurch, dass die Entsprechende Zeichenkette " \
                 "in 'String' (Anführungsstrichen) gesetzt wird. Für Zeichenketten gibt es Operationen + und *. " \
                 "Bei + werden die Inhalte zweier Stringvariablen aneinander gehängt, bei * kann die " \
                 "Stringvariable mit einer ganzen Zahl multipliziert werden. \n\n\n\nAufgabe:\n\n" \
                 "Geben sie in das Schriftfeld den Variablennamen <bunteblume> ein und  belegen Sie ihn " \
                 "indem sie den Wert 'Rot' und den Wert 'gelb' addieren. \n\nWeißen sie den Variablen <glueck> " \
                 "den Wert 'toi ' (Vergiss nicht das Leerzeichen nach 'toi'!)und <wunsch> den Wert 'fuer die Pruefung' zu. \n\nMutlipliziere <glueck> mit 3 und addiere dies zu <wunsch> " \
                 "hinzu und weisen sie das Ergebnis <glueckwunsch> zu. \n\n\n\n\n\n\n\n\n\n\n"

Lesson1_4_GivenCode = "blume = 'Gruen'\nprint blume\n\nHeyhey ='Hello '+'World'\nprint Heyhey\n\ncolours = 'red'*3\nprint colours"
Lesson1_4_SolutionCode = "bunteblume = 'Rot' + 'gelb'\nglueck = 'toi'\nwunsch = ' fuer die Pruefung'\nglueckwunsch= glueck'*3 + wunsch"

Lesson1_4_StringBoolean = True
Lesson1_4_SolutionOutput ="toi toi toi fuer die Pruefung"

Lesson1_4_AddedCodeBoolean = True
Lesson1_4_AddedCode = \
    "\nif (glueck == 'toi '):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (wunsch == 'fuer die Pruefung'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (glueckwunsch == 'toi toi toi fuer die Pruefung'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueckwunsch hat einen falschen Wert')" \
    "\nif (bunteblume == 'Rotgelb'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable bunteblume hat einen falschen Wert')"
    #"\nif (glueck == 'toi'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')"

Lesson1_4_Name = "String Variablen"



Lesson1_5_Text = "Lektion 1.5 \n\nMit den Rechenoperationen hast du nun eigentlich schon das wichtigste gelernt. An dieser Stelle wollen wir uns einem anderen, " \
                 "auch sehr wichtigem Thema annehmen -- Kommentaren. Manchmal kann es sehr nützlich sein, im Code Erklärungen hinzuzufügen, " \
                 "damit andere Leute verstehen, was der Code tut oder was sich der Programmierer dabei gedacht hat. Manchmal braucht der Programmierer selber bei über 1000 Zeilen Code auch einfach" \
                 "nur eine Gedächtnisstütze. \n\n\n\n" \
                 "Dieser Text soll natürlich bei der Ausführung des Programmes vom Computer ignoriert werden, auch wenn sich Befehle im Kommentar befinden. Kommentare werden in " \
                 "Python mit dem Symbol < # > eingeleitet. Sofern dieses Symbol auftaucht, wird der restliche Text in dieser Zeile vom Computer ignoriert. \n\n\n" \
                 "Die nächste Aufgabe ist einfach: Schreibe ein paar Kommentare in den Code-Bereich und drücke auf 'Check Code'\n\n\n\n\n\n\n\n\n\n\n\n"



Lesson1_5_GivenCode = "# print 'Das hier ist ein Kommentar und wird von Python ignoriert'"
Lesson1_5_SolutionCode = ""

Lesson1_5_StringBoolean = False
Lesson1_5_SolutionOutput =""

Lesson1_5_AddedCodeBoolean = False
Lesson1_5_AddedCode = ""

Lesson1_5_Name = "Kommentare"




Lesson1_6_Text = "Lektion 1.6 \n\nMit Kommentaren selbst kannst du natürlich nichts programmieren, deswegen nehmen wir uns " \
                 "jetzt wieder einem sehr essentiellem Thema an, und zwar Listen. \n\n\nListen sind besondere Datenstrukturen. " \
                 "In ihnen können mehrere Werte gespeichert werden. Der Zugriff auf diese Werte erfolgt mit einem Index " \
                 "(die Stelle in der Liste, an der der Wert gespeichert ist — beginnend bei 0 !). \n\nEine Liste wird mit [] definiert." \
                 "Monty hat nun seine Fahrkarten gekauft und muss jetzt seinen Koffer packen. Er will folgende Dinge mitnehmen: " \
                 "Eine Hose, ein Hemd, eine Jacke, Socken, Schuhe und natuerlich seine Zahnbuerste. \n\n\n\nLege eine Variable mit dem Namen " \
                 "'gepaeck' an und füge saemtliche Gegenstaende hinzu. Lasse anschließend die Liste auf dem Bildschirm ausgeben\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"



Lesson1_6_GivenCode = "liste = []\nliste = [0, 1, 2, 3]\nprint liste[2] # Die dritte (!) Stelle wird ausgegeben. "
Lesson1_6_SolutionCode = "gepaeck = [Hose, Hemd, Jacke, Socken, Schuhe, Zahnbuerste]\nprint(gepaeck)"

Lesson1_6_StringBoolean = True
Lesson1_6_SolutionOutput ="[Hose, Hemd, Jacke, Socken, Schuhe, Zahnbuerste]"

Lesson1_6_AddedCodeBoolean = True
Lesson1_6_AddedCode = "" \
                      "\nif (gepaeck == [Hose, Hemd, Jacke, Socken, Schuhe, Zahnbuerste]):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"


Lesson1_6_Name = "Listen"



Lesson1_7_Text = "Herzlichen Glückwunsch - du hast nun schon ein ganz schönes Stück Arbeit hinter dir!" \
	"Zeit für eine kleine Verschnaufpause. Trink einen Schluck und Streck dich einmal, " \
	"dann gehts weiter mit dem Themenkomplex der Kontrollstrukturen. Was das genau ist erfährst du jetzt: " \
	"In einem Programm möchte man oftmals in Abhängigkeit von einer bestimmten Bedingung unterschiedlich " \
	"verfahren. Dazu wird die Bedingung, die nach dem Befehl if (wenn) folgt, überprüft. " \
	"Ist diese wahr (true) ist, so wird der Code ausgeführt, der direkt im Anschluss folgt. " \
	"Ist die Bedingung falsch (false), so wird  der Code nach else (‘sonst’) ausgeführt. " \
	"Manchmal muss zwischen mehr als zwei Bedingungen unterschieden werden. Dazu wird der " \
	"Befehl elif verwendet bei dem eine weitere Bedingung gestellt wird. " \
	"Monty möchte gerne noch ein Geschenk für Brian mitbringen. Er überlegt ob er lieber " \
	"einen Strauß Blumen oder eine Tafel von Brians Lieblingsschokolade kaufen soll. " \
	"Die Tafel Schokolade kostet 2 Euro und der Blumenstrauss 5 Euro. Finde mittels eines " \
	"if/else Konstrukts heraus ob Monty Blumen, Schokolade oder sogar beides kaufen kann. " \
	"Er würde lieber die Blumen als die Schokolade kaufen, deshalb teste ob er genug Geld " \
	"für die Blumen hat zuerst. Gebe auf dem Bildschirm die Gegenstände als String ('Blumenstrauss'/'Schokolade' aus, "\
	"die Monty kauft" \
	"Gebe danach aus wieviel Geld er noch übrig hat. Modifiziere das gegebene Beispiel. Monty hat 10Euro Taschengeld. "

Lesson1_7_GivenCode =   "\n blumenstrauss = 0 "\
			"\n schokolade = 0 "\
			"\n taschengeld = 0 " \
			"\n" \
			"\n" \
			"if geldeinwurf > fahrpreis:"\
    			"\n\t Rueckgabe = fahrpreis - geldeinwurf"\
			"\n else: "\
    			"\n\t rueckgabe = 0" \

Lesson1_7_SolutionCode = "if taschengeld > blumenstrauss:" \
				"\n\t print 'Blumenstrauss' " \
				"\n\t taschengeld = taschengeld - blumenstrauss" \
				"\n if taschengeld > schokolade " \
				"\n\t print 'Schokolade' " \
				"\n\t taschengeld = taschengeld - schokolade" \
				"\n print taschengeld"

Lesson1_7_StringBoolean = True
Lesson1_7_SolutionOutput = "Blumenstrauss\nSchokolade\n3"

Lesson1_7_AddedCodeBoolean = True
Lesson1_7_AddedCode = 	"\nif (taschengeld == 3 ):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable (taschengeld hat einen falschen Wert')" \
			"\nif (schokolade == 2 ):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable (schokolade hat einen falschen Wert')" \
			"\nif (blumenstrauss == 5 ):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable (blumenstrauss hat einen falschen Wert')"

Lesson1_7_Name = "if/else Konditionen"






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
    global current_Lesson
    # Clear Code
    txt.delete(1.0,'end')
    # Insert original state
    if current_Lesson == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    if current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    if current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    if current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    if current_Lesson == 4:
        txt.insert(1.0,Lesson1_3_GivenCode, END)
    if current_Lesson == 5:
        txt.insert(1.0,Lesson1_4_GivenCode, END)
    if current_Lesson == 6:
        txt.insert(1.0,Lesson1_5_GivenCode, END)
    if current_Lesson == 7:
        txt.insert(1.0,Lesson1_6_GivenCode, END)
    if current_Lesson > 5:
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
        if not GlobalOutput == "" :
            a = GlobalOutput[len(GlobalOutput)-1]
            if a == " " or a == "\t" or a == "\n":
                GlobalOutput = GlobalOutput[0:len(GlobalOutput)-1]
            else:
                bb = False
    # Deleting leading newlines of the GlobalOutput
    while cc == True:
        if not GlobalOutput == "" :
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

    print "checkingRunCode"
    global cmdfield
    global textfield
    global Errorlist
    global GlobalOutput
    global Lesson_Number
    global button1

    global Lesson1_0_StringBoolean
    global Lesson1_0_SolutionOutput#
    global Lesson1_0_AddedCodeBoolean
    global Lesson1_0_AddedCode

    global Lesson1_1_StringBoolean
    global Lesson1_1_SolutionOutput#
    global Lesson1_1_AddedCodeBoolean
    global Lesson1_1_AddedCode

    global Lesson1_2_StringBoolean
    global Lesson1_2_SolutionOutput#
    global Lesson1_2_AddedCodeBoolean
    global Lesson1_2_AddedCode

    global Lesson1_3_StringBoolean
    global Lesson1_3_SolutionOutput#
    global Lesson1_3_AddedCodeBoolean
    global Lesson1_3_AddedCode

    global Lesson1_4_StringBoolean
    global Lesson1_4_SolutionOutput#
    global Lesson1_4_AddedCodeBoolean
    global Lesson1_4_AddedCode

    global Lesson1_5_StringBoolean
    global Lesson1_5_SolutionOutput#
    global Lesson1_5_AddedCodeBoolean
    global Lesson1_5_AddedCode

    global Lesson1_6_StringBoolean
    global Lesson1_6_SolutionOutput#
    global Lesson1_6_AddedCodeBoolean
    global Lesson1_6_AddedCode

    StringBoolean = ""
    SolutionOutput = ""

    AddedCodeBoolean = ""
    AddedCode = ""

    if current_Lesson == 0:
        StringBoolean = Lesson0_0_StringBoolean
        SolutionOutput = Lesson0_0_SolutionOutput
        AddedCodeBoolean = Lesson0_0_AddedCodeBoolean
        AddedCode = Lesson0_0_AddedCode

    if current_Lesson == 1:
        StringBoolean = Lesson1_0_StringBoolean
        SolutionOutput = Lesson1_0_SolutionOutput
        AddedCodeBoolean = Lesson1_0_AddedCodeBoolean
        AddedCode = Lesson1_0_AddedCode

    if current_Lesson == 2:
        StringBoolean = Lesson1_1_StringBoolean
        SolutionOutput = Lesson1_1_SolutionOutput
        AddedCodeBoolean = Lesson1_1_AddedCodeBoolean
        AddedCode = Lesson1_1_AddedCode

    if current_Lesson == 3:
        StringBoolean = Lesson1_2_StringBoolean
        SolutionOutput = Lesson1_2_SolutionOutput
        AddedCodeBoolean = Lesson1_2_AddedCodeBoolean
        AddedCode = Lesson1_2_AddedCode

    if current_Lesson == 4:
        StringBoolean = Lesson1_3_StringBoolean
        SolutionOutput = Lesson1_3_SolutionOutput
        AddedCodeBoolean = Lesson1_3_AddedCodeBoolean
        AddedCode = Lesson1_3_AddedCode

    if current_Lesson == 5:
        StringBoolean = Lesson1_4_StringBoolean
        SolutionOutput = Lesson1_4_SolutionOutput
        AddedCodeBoolean = Lesson1_4_AddedCodeBoolean
        AddedCode = Lesson1_4_AddedCode

    if current_Lesson == 6:
        StringBoolean = Lesson1_5_StringBoolean
        SolutionOutput = Lesson1_5_SolutionOutput
        AddedCodeBoolean = Lesson1_5_AddedCodeBoolean
        AddedCode = Lesson1_5_AddedCode

    if current_Lesson == 7:
        StringBoolean = Lesson1_6_StringBoolean
        SolutionOutput = Lesson1_6_SolutionOutput
        AddedCodeBoolean = Lesson1_6_AddedCodeBoolean
        AddedCode = Lesson1_6_AddedCode

    print "Attributes taken"
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

    codeOutput = ""
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
        if current_Lesson == Lesson_Number:
            Lesson_Number += 1
        button.destroy()
        if (button1.winfo_exists() == 0):
            button1 = Button(root, text='Weiter', command = nextLesson )
            button1.grid(row=30, column=3)

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
    global button
    global current_Lesson

    global booleanboohja
    booleanboohja = False

    current_Lesson +=   1

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=30, column = 1)


    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons
    # Change Text
    if current_Lesson == 0:
        label1.config(text=Lesson0_0_Text)
    if current_Lesson == 1:
        label1.config(text= Lesson1_0_Text)
    if current_Lesson == 2:
        label1.config(text= Lesson1_1_Text)
    if current_Lesson == 3:
        label1.config(text= Lesson1_2_Text)
    if current_Lesson == 4:
        label1.config(text= Lesson1_3_Text)
    if current_Lesson == 5:
        label1.config(text= Lesson1_4_Text)
    if current_Lesson == 6:
        label1.config(text= Lesson1_5_Text)
    if current_Lesson == 7:
        label1.config(text= Lesson1_6_Text)
    if current_Lesson > 7:
        1+1 # Return to the game!

    # Change Code
    txt.delete(1.0,'end')

    if current_Lesson == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    if current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    if current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    if current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    if current_Lesson == 4:
        txt.insert(1.0,Lesson1_3_GivenCode, END)
    if current_Lesson == 5:
        txt.insert(1.0,Lesson1_4_GivenCode, END)
    if current_Lesson == 6:
        txt.insert(1.0,Lesson1_5_GivenCode, END)
    if current_Lesson == 7:
        txt.insert(1.0,Lesson1_6_GivenCode, END)
    if current_Lesson > 5:
        1+1 # Return to the game!

    button1.destroy()


global buttonlesson0
global buttonlesson1
global buttonlesson2
global buttonlesson3
global buttonlesson4
global buttonlesson5
global buttonlesson6
global buttonlesson7

def reinstate_buttons():
    global button
    global button2
    global button3

    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=30, column = 1)
    button2 = Button(root, text ='Archive', command = archive )
    button2.grid(row=30, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =30, column = 6)


def lesson0():
    global button
    global button1
    global button2
    global button3
    global current_Lesson
    global Lesson0_0_Text
    global Lesson0_0_GivenCode

    deletebuttons()

    current_Lesson = 0

    label1.config(text= Lesson0_0_Text)
    txt.delete(1.0,END)
    txt.insert(1.0,Lesson0_0_GivenCode, END)

    reinstate_buttons()


def lesson1():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_0_Text
    global Lesson1_0_GivenCode

    current_Lesson = 1
    deletebuttons()

    label1.config(text= Lesson1_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_0_GivenCode, END)

    reinstate_buttons()


def lesson2():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_1_Text
    global Lesson1_1_GivenCode

    current_Lesson = 2
    deletebuttons()

    label1.config(text= Lesson1_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_1_GivenCode, END)

    reinstate_buttons()


def lesson3():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_2_Text
    global Lesson1_2_GivenCode

    current_Lesson = 3
    deletebuttons()

    label1.config(text= Lesson1_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_2_GivenCode, END)

    reinstate_buttons()


def lesson4():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_3_Text
    global Lesson1_3_GivenCode

    deletebuttons()

    current_Lesson = 4
    label1.config(text= Lesson1_3_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_3_GivenCode, END)


    reinstate_buttons()

def lesson5():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_4_Text
    global Lesson1_4_GivenCode

    current_Lesson = 5
    deletebuttons()

    label1.config(text= Lesson1_4_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_4_GivenCode, END)

    reinstate_buttons()


def lesson6():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_5_Text
    global Lesson1_5_GivenCode

    deletebuttons()

    current_Lesson = 6
    label1.config(text= Lesson1_5_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_5_GivenCode, END)


    reinstate_buttons()



def lesson7():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_6_Text
    global Lesson1_6_GivenCode

    deletebuttons()

    current_Lesson = 7
    label1.config(text= Lesson1_6_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_6_GivenCode, END)

    reinstate_buttons()


def deletebuttons():
    global Lesson_Number
    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3
    global buttonlesson4
    global buttonlesson5
    global buttonlesson6
    global buttonlesson7

    if Lesson_Number >= 0:
        buttonlesson0.destroy()
    if Lesson_Number >= 1:
        buttonlesson1.destroy()
    if Lesson_Number >= 2:
        buttonlesson2.destroy()
    if Lesson_Number >= 3:
        buttonlesson3.destroy()
    if Lesson_Number >= 4:
        buttonlesson4.destroy()
    if Lesson_Number >= 5:
        buttonlesson5.destroy()
    if Lesson_Number >= 6:
        buttonlesson6.destroy()
    if Lesson_Number >= 7:
        buttonlesson7.destroy()




def archive():

    # Clear Console
    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.configure(state='disabled')
    # Clear Code field
    txt.delete(1.0,END)
    txt.insert(1.0,"", END)

    # Add to label
    label1.configure(text="")

    global button
    global button1
    global button2
    global button3
    button.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()

    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3
    global buttonlesson4
    global buttonlesson5
    global buttonlesson6
    global buttonlesson7
    global Lesson0_0_Name
    global Lesson1_0_Name
    global Lesson2_0_Name
    global Lesson3_0_Name
    global Lesson4_0_Name
    global Lesson5_0_Name


    if Lesson_Number >= 0:
        global buttonlesson0
        buttonlesson0 = Button(root, text='L.0 %r' %Lesson0_0_Name, command=lesson0 )
        buttonlesson0.grid(row=0, column = 0)

    if Lesson_Number >= 1:
        global buttonlesson1
        buttonlesson1 = Button(root, text='L.1 %r' %Lesson1_0_Name, command=lesson1 )
        buttonlesson1.grid(row=1, column = 0)

    if Lesson_Number >= 2:
        global buttonlesson2
        buttonlesson2 = Button(root, text='L.1.1 %r' %Lesson1_1_Name, command=lesson2 )
        buttonlesson2.grid(row=2, column = 0)

    if Lesson_Number >= 3:
        global buttonlesson3
        buttonlesson3 = Button(root, text='L.1.2 %r' %Lesson1_2_Name, command=lesson3 )
        buttonlesson3.grid(row=3, column = 0)

    if Lesson_Number >= 4:
        global buttonlesson4
        buttonlesson4 = Button(root, text='L.1.3 %r' %Lesson1_3_Name, command=lesson4 )
        buttonlesson4.grid(row=4, column = 0)

    if Lesson_Number >= 5:
        global buttonlesson5
        buttonlesson5 = Button(root, text='L.1.4 %r' %Lesson1_4_Name, command=lesson5 )
        buttonlesson5.grid(row=5, column = 0)

    if Lesson_Number >= 6:
        global buttonlesson6
        buttonlesson6 = Button(root, text='L.1.5 %r' %Lesson1_5_Name, command=lesson6 )
        buttonlesson6.grid(row=6, column = 0)

    if Lesson_Number >= 7:
        global buttonlesson7
        buttonlesson7 = Button(root, text='L.1.7 %r' %Lesson1_6_Name, command=lesson7 )
        buttonlesson7.grid(row=7, column = 0)

    # list all lessons

########### GUI ###########


texter = ""

w = Canvas(root, width=300, height=650)
w.grid(row=0, column =0, columnspan = 4, rowspan=30)
w.create_rectangle(0, 0, 305, 655, fill="white")

c = Canvas(root, width=5, height=650)
c.grid(row=0, column =5, rowspan = 30) # 0-29
c.create_rectangle(0, 0, 200, 655, fill="grey")


label1 = Label(root, text=texter ,  justify=LEFT, wraplength= 250, bg ="white")
label1.grid(row=0, column =0, columnspan = 4, rowspan = 30) # 0-29

button = Button(root, text='Check Code', command=checkRunCode )
button.grid(row=30, column = 1)
button1 = Button(root, text='Weiter', command = nextLesson )
button1.grid(row=30, column=3)
button2 = Button(root, text ='Archive', command = archive )
button2.grid(row=30, column = 2)
button3 = Button (root, text='Reset Code', command=reset )
button3.grid(row =30, column = 6)

if current_Lesson == 0:
    label1.config(text=Lesson0_0_Text)
if current_Lesson == 1:
    label1.config(text= Lesson1_0_Text)
if current_Lesson == 2:
    label1.config(text= Lesson1_1_Text)
if current_Lesson == 3:
    label1.config(text= Lesson1_2_Text)
if current_Lesson == 4:
    label1.config(text= Lesson1_3_Text)
if current_Lesson == 5:
    label1.config(text= Lesson1_4_Text)
if current_Lesson == 6:
    label1.config(text= Lesson1_5_Text)
if current_Lesson == 7:
    label1.config(text= Lesson1_6_Text)

txt_frm = Frame(root,width=100, height=100).grid(row=0, column=6)
txt = Text(txt_frm,height = 27, width = 80,  bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=1, rowspan = 29 ,sticky="n") # 0-28
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))
txt.pack_propagate()

cmd_frm = Frame(root).grid(row=1,column=6,sticky="nsew")
cmd = Text(cmd_frm, height = 13, width = 80, bg="white", fg="black")
cmd.config(font=("Courier", 10), undo=True, wrap='word')
cmd.grid(row = 29, column = 6, sticky="nw")
cmd.configure(state='disabled')
cmd.pack_propagate()



######## Initialize ##############

reset()
set_cmd()

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("sounds/flag.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#sound_flag.set_volume(0.2)
#sound_flag.play()


# Kein Weiter Button in the first lesson - press "Check Code" first
button1.destroy()
####### Main Loop #########



mainloop()




