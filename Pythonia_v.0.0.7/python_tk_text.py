#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import StringIO
from Tkinter import *
import pygame

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

# Text: Introduction and tasks

# GivenCode: given Code at the beginning
# SolutionCode: What we want them to programm

# StringBoolean: True if String Checking is needed for this lesson
# SolutionOutput: expected String

# AddedCodeBoolean: True if Variable value checking is needed for this lesson
# AddedCode: variable value checking code

Lesson_Number = 17
current_Lesson = 0
maxLessons = 17



Lesson0_0_Text = "Lektion 0: \n\nHerzlich willkommen zu unserem Pythonlerntutorial! \n\nImmer wenn du ein Abenteuer bestanden" \
           " hast wirst du mit einer Python Lektion belohnt und kannst so spielerisch Programmieren lernen.\n"\
           "Dabei wirst du Schritt für Schritt in eine der meist verwendeten Skriptsprachen, Python, eingeführt.\n\n"\
           "Zum Verstaendnis der Aufgaben werden die Befehle und vorgegebene Begriffe in spitze Klammern <Befehl> gesetzt.\n\n\nUm eine Lektion abzuschließen und zur nächsten zu kommen, " \
           "klicke auf 'Check Code' - Hast du den richtigen Code programmiert wird dir das Ergebnis ausgegeben und der 'Weiter' Knopf wird eingeblendet. " \
           "Wenn du du etwas falsches eingibst, wird dir eine Fehlermeldung angezeigt. \n\nDa wir im Moment keine Aufgabe gestellt haben, probiere es einfach mal aus und klicke auf 'Check Code'." \
	   "Python ist sehr sensitiv, wenn es um Leerzeichen und Groß- und Kleinschreibung geht! Achte auf Leerzeichen am Anfang, Einrückungen mit Tab und das dein Ergebnis exakt der Aufgabenstellung entspricht!\n\n\n\n\n\n\n\n\n\n"

Lesson0_0_GivenCode = "\n\n\n\n\n"
Lesson0_0_SolutionCode = ""

Lesson0_0_StringBoolean = False
Lesson0_0_SolutionOutput =""

Lesson0_0_AddedCodeBoolean = False
Lesson0_0_AddedCode = ""

Lesson0_0_Name = "Intro"


Lesson1_0_Text = "Lektion 1.0: \n\nWillkommen zu deiner ersten Lektion.\n\n Jedes Programm muss mit der Welt kommunizieren können, " \
                  "dazu gibt es in Python die Funktion <print> (ausdrucken/ausgeben). \n\n\nDas einfächste Beispiel " \
                  "hierfür ist sich 'Hello World' ausgeben zu lassen. Dazu muss der Befehl <print> und die gewünschte " \
                  "Ausgabe in Anführungszeichen <'Hello World'> eingegeben werden, da in diesem Fall die Ausgabe ein String (also eine Reihenfolge von Buchstaben) ist. \n\n\nAufgabe: \n\nGeben Sie folgenden Satz aus: \n" \
                  "'Python ist KEINE Schlange'.\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_0_GivenCode = "print 'Hello World'\n\n\n\n\n"
Lesson1_0_SolutionCode = "print 'Python ist KEINE Schlange'"

Lesson1_0_StringBoolean = True
Lesson1_0_SolutionOutput ="Python ist KEINE Schlange"

Lesson1_0_AddedCodeBoolean = False
Lesson1_0_AddedCode = ""
Lesson1_0_Name = "Print"

Lesson1_1_Text = "Lektion 1.1:\n\nUm Werte und Ergebnisse in einem Programm wieder verwenden zu können," \
                 " gibt es in Programmiersprachen Variablen. \nDiese haben einen Namen und können " \
                 "mit verschiedenen Arten von Werten belegt werden. Für den Namen können " \
                 "Groß- und Kleinbuchstaben, Ziffern und das Zeichen _ (Unterstrich) verwendet werden.\n" \
                 "Das erste Zeichen darf aber keine Ziffer sein und es dürfen keine " \
                 "reservierten Wörter der Programmiersprache verwendet werden. \n\n\n" \
                 "Wie in der Mathematik kann man mit diesen Variablen die Grundrechenarten " \
                 "Addition ( + ), Subtraktion ( - ), Multiplikation ( * ) und Division ( / ) ausführen.\n" \
                 "Dabei kann sowohl mit ganzen Zahlen (Integer) als auch mit Fließkomma Zahlen " \
                 "(Floats) gerechnet werden. Bei Floats wird wie im Englischen üblich der . (Punkt) " \
                 "statt dem Komma verwendet.\n\n\n\n" \
                 "Aufgabe: \n\nWeisen Sie der Variablen x die Differenz aus 14.56 - 7 zu " \
                 "und geben sie mit <print> das Ergebnis aus. Berechnen Sie ebenfalls für y das " \
                 "Produkt von 35 * 49 und fuer z den Quotienten von 50.4 / 3.6 und geben Sie " \
                 "jeweils in dieser Reihenfolge (x,y,z) das Ergebnis aus.\n\n\n\n\n\n\n"

Lesson1_1_GivenCode = "x = 3 + 1732\nprint x\n\n\n\n\n"
Lesson1_1_SolutionCode = "x = 14.56 - 7\nprint x\ny = 35 * 49\nprint y\nz = 50.4 / 3.6\nprint z"

Lesson1_1_StringBoolean = True
Lesson1_1_SolutionOutput ="7.56\n1715\n14.0"

Lesson1_1_AddedCodeBoolean = True
Lesson1_1_AddedCode =  \
    "\nif (x == (14.56 - 7):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable x hat einen falschen Wert')" \
    "\nif (y == 1715):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable y hat einen falschen Wert')" \
    "\nif (z == 14.0):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable z hat einen falschen Wert')"

Lesson1_1_Name = "Integer und Rechenzeichen"



Lesson1_2_Text = "Lektion 1.2 \n\nZusätzlich zu dem normalen Divisionsoperator < / > gibt es die ganzzahlige Division. Der Operator dazu ist der < // >. " \
                 "Mit diesem wird das ganzzahlige Ergebnis der Division berechnet. Zusätzlich gibt es den Modulo Operator < % > mit dem der Rest berechnet wird.\n\n\n" \
                 "Speziell in Python 2 liefert auch schon 7/5 das ganzzahlige Ergebnis 1, dies kann aber mit 7.0/5 oder 7/5.0 umgangen werden. \n\n" \
		 "Berechne den Wert von 7 geteilt durch 2 als ganzzahlige Divison, weise ihn der Variable 'GanzeZahl' zu und gebe ihn aus.  \n\n" \
                 "Berechne zusätzlich den Rest von 7 geteilt durch 5 mit Modulo, weise ihn der Variable 'mod' zu und gebe ihn aus.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_2_GivenCode = "GanzeZahl = 7.0 / 2\n\n\n\n\n"
Lesson1_2_SolutionCode = "mod = 7 % 5\nprint mod"

Lesson1_2_StringBoolean = True
Lesson1_2_SolutionOutput ="3\n2"

Lesson1_2_AddedCodeBoolean = True
Lesson1_2_AddedCode = \
    "\nif (GanzeZahl == 1.0:\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable GanzeZahl hat einen falschen Wert')" \
    "\nif (mod == 2:\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable mod hat einen falschen Wert')" \

Lesson1_2_Name = "Modulo 1"



Lesson1_3_Text = "Lektion 1.3 \n\nBevor wir nun richtig loslegen folgen noch ein paar einfache Rechenaufgaben. " \
                 "Brian wohnt 42km entfernt von Monty. Monty weiß, dass er für jeden Kilometer " \
                 "mit der Bahn 25 Cent zahlen muss. Zusätzlich benötigt er noch ungefähr 15 Euro um sich " \
                 "für die Reise ein Buch und eine Cola zu kaufen. Lege eine Variable mit dem Namen " \
                 "'fahrpreis' an und berechne wieviel Monty's Hin- und Rückreise (Kilometerpauschale + sonstige Ausgaben)" \
                 " kostet. Wir nehmen an, dass Monty das Buch und die Cola nur einmal kauft, aber sich Hin- und Rückfahrttickets kauft. \n" \
                 "Gebe den Wert der Variable auf dem Bildschirm aus. \n\n" \
                 "Monty zahlt grundsätzlich nur mit 5 Euro Scheinen.\n\n" \
                 "Wie viel Wechselgeld bekommt Monty zurück wenn er sich Fahrkarten kauft um Brian zu besuchen? " \
                 "Weise das Wechselgeld der Variable 'Wechselgeld' zu!\n" \
                 "\nÜberlege hierzu wie man mit Modulo und anderen Rechenoperatoren das Wechselgeld ausrechnen kann ohne Veränderungen vornehmen zu müssen," \
                 "wenn sich der Fahrpreis ändert." \
                 "Gebe anschließend die Variable 'Wechselgeld' mit <print> aus.\n\n\n\n\n\n\n\n\n\n"

Lesson1_3_GivenCode = "fahrpreis = \nWechselgeld = \n\n\n\n\n"
Lesson1_3_SolutionCode = "fahrpreis = ((42 * 0.25) * 2) + 15\nprint(fahrpreis)\nWechselgeld = (fahrpreis *2)%5"

Lesson1_3_StringBoolean = True
Lesson1_3_SolutionOutput ="36.0\n4.0"

Lesson1_3_AddedCodeBoolean = True
Lesson1_3_AddedCode = \
    "\nif (fahrpreis == ((42 * 0.25) * 2) + 15):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable fahrpreis hat einen falschen Wert')" \
    "\nif (Wechselgeld == 4):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Wechselgeld hat einen falschen Wert')" \

Lesson1_3_Name = "Modulo 2"


########################################_2_Lektion_########################################


Lesson2_0_Text = "Lektion 2.0: \n\nUm nicht nur mit Zahlen arbeiten zu können, sondern auch mit Texten gibt es auch Variablen " \
                 "für Zeichenketten (Strings). Die Zuweisung erfolgt dadurch, dass die Entsprechende Zeichenkette " \
                 "in 'String' (Anführungsstrichen) gesetzt wird. Für Zeichenketten gibt es die Operationen + und *. " \
                 "Bei + werden die Inhalte zweier Stringvariablen aneinander gehängt, bei * kann die " \
                 "Stringvariable mit einer ganzen Zahl multipliziert werden. \n\n\n\nAufgabe:\n\n" \
                 "Geben sie in das Schriftfeld den Variablennamen <bunteblume> ein und  belegen Sie ihn " \
                 "indem sie den Wert 'Rot' und den Wert 'gelb' addieren. \n\nWeißen sie den Variablen <glueck> " \
                 "den Wert 'toi ' (Vergiss nicht das Leerzeichen nach 'toi'!)und <wunsch> den Wert 'fuer die Pruefung' zu. \n\nMutlipliziere <glueck> mit 3 und addiere dies zu <wunsch> " \
                 "hinzu und weisen sie das Ergebnis <glueckwunsch> zu. \n\n\n\n\n\n\n\n\n\n\n"

Lesson2_0_GivenCode = "Heyhey ='Hello '+'World'\ncolours = 'red'*3\n\n\n\n\n"
Lesson2_0_SolutionCode = "bunteblume = 'Rot' + 'gelb'\nglueck = 'toi'\nwunsch = ' fuer die Pruefung'\nglueckwunsch= glueck'*3 + wunsch"
Lesson2_0_StringBoolean = True
Lesson2_0_SolutionOutput ="toi toi toi fuer die Pruefung"

Lesson2_0_AddedCodeBoolean = True
Lesson2_0_AddedCode = \
    "\nif (glueck == 'toi '):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (wunsch == 'fuer die Pruefung'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')" \
    "\nif (glueckwunsch == 'toi toi toi fuer die Pruefung'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable glueckwunsch hat einen falschen Wert')" \
    "\nif (bunteblume == 'Rotgelb'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable bunteblume hat einen falschen Wert')"
    #"\nif (glueck == 'toi'):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')"

Lesson2_0_Name = "String Variablen"





Lesson2_1_Text = 	"Lektion 2.1: \n\nWir können auch Zahlen in einen String einfügen und dann ausgeben. Es funktioniert fast wie in der Lektion davor, bloß müssen wir noch "	\
			"an der Zahl eine kleine Veränderung vornehmen. \n\nUm eine Zahl mit dem <+> Operator an einen String anfügen zu können, wie wir das vorher mit " \
			"Strings und String gemacht haben, müssen wir die Zahl zu einem String formatieren. Ausgabe-technisch verändert sich an der Zahl nichts." \
			"\n\nLege eine Variable mit dem namen <Unsere_Zahl> an und belege sie mit dem Wert <1337>. Gebe diesen Wert aus. \n\nAnschließend lege einen String an mit dem Namen 'Unser_String' mit dem Inhalt:" \
			"'Dies ist eine String.' Gebe auch diesen aus. Nun gebe den String erneut aus, aber hänge <Unsere_Zahl> an ihn an. Um dies machen zu können musst du um den " \
			"Variablennamen der Zahl während du ihn an den String anhängst, den folgenden Befehl schreiben: <str(Zahl)>. \n\nFormatieren wir die Zahl nicht zu einem String bevor wir sie an " \
			"einen String anhängen, erhalten wir einen Fehler! Da wir <Unsere_Zahl> als Integer(als Zahl) behalten wollen und nicht permanent als String speichern wollen, weisen wir den Befehl <str(Zahl)> "\
			"nicht Unsere_Zahl zu, sondern benutzen ihn diesen nur temporär im <print> Befehl.\n\n\n\n\n"


Lesson2_1_GivenCode = "Rote_Blume = 'Rote'+'_'+'Blume'"
Lesson2_1_SolutionCode = "Unsere_Zahl = 1337\nprint Unsere_Zahl\nUnser_String ='Dies ist ein String.'\nprint Unser_String\nprint Unser_String + str(Unsere_Zahl)"

Lesson2_1_StringBoolean = True
Lesson2_1_SolutionOutput ="1337\nDies ist ein String.\nDies ist ein String.1337"
Lesson2_1_AddedCodeBoolean = False
Lesson2_1_AddedCode = \
    		"\nif (Unser_String == 'Dies ist ein String.'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Unser_String hat einen falschen Wert')"     		"\nif (Unsere_Zahl == 1337):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable glueck hat einen falschen Wert')"

Lesson2_1_Name = "String Varialben II"






Lesson2_2_Text = "Lektion 2.2: \n\nMit den Rechenoperationen hast du nun eigentlich schon das wichtigste gelernt. An dieser Stelle wollen wir uns einem anderen, " \
                 "auch sehr wichtigem Thema annehmen -- Kommentaren. Manchmal kann es sehr nützlich sein, im Code Erklärungen hinzuzufügen, " \
                 "damit andere Leute verstehen, was der Code macht oder was sich der Programmierer dabei gedacht hat. Manchmal braucht der Programmierer selber bei über 1000 Zeilen Code auch einfach" \
                 "nur eine Gedächtnisstütze. \n\n\n\n" \
                 "Dieser Text soll natürlich bei der Ausführung des Programmes vom Computer ignoriert werden, auch wenn sich Befehle im Kommentar befinden. Kommentare werden in " \
                 "Python mit dem Symbol < # > eingeleitet. Sofern dieses Symbol auftaucht, wird der restliche Text in dieser Zeile vom Computer ignoriert. \n\n\n" \
                 "Die nächste Aufgabe ist einfach: Schreibe ein paar Kommentare in den Code-Bereich und drücke auf 'Check Code'\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson2_2_GivenCode = "# print 'Das hier ist ein Kommentar und wird von Python ignoriert'\n\n\n\n\n"
Lesson2_2_SolutionCode = ""

Lesson2_2_StringBoolean = True
Lesson2_2_SolutionOutput =""

Lesson2_2_AddedCodeBoolean = False
Lesson2_2_AddedCode = ""

Lesson2_2_Name = "Kommentare"


########################################_3_Lektion_########################################



Lesson3_0_Text = "Lektion 3.0: \n\nMit Kommentaren selbst kannst du natürlich nichts programmieren, deswegen nehmen wir uns " \
                 "jetzt wieder einem sehr essentiellem Thema an, und zwar Listen. \n\n\nListen sind besondere Datenstrukturen. " \
                 "In ihnen können mehrere Werte gespeichert werden. Der Zugriff auf diese Werte erfolgt mit einem Index " \
                 "(die Stelle in der Liste, an der der Wert gespeichert ist — beginnend bei 0 !). \n\nEine Liste wird mit [] definiert." \
                 "Monty hat nun seine Fahrkarten gekauft und muss jetzt seinen Koffer packen. Er will folgende Dinge in dieser Reihenfolge mitnehmen: " \
                 "Eine Hose, ein Hemd, eine Jacke, Socken, Schuhe und natürlich seine Zahnbuerste. \n\n\n\nLege eine Variable mit dem Namen " \
                 "'gepaeck' an und füge sämtliche Gegenstände hinzu. Lasse anschließend die Liste auf dem Bildschirm ausgeben\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


Lesson3_0_GivenCode = "liste = [] # Da wir in der dritten Zeile die Liste gleich füllen,\n# können wir die erste Zeile auch weglassen\nliste = [0, 1, 2, 3]\nprint liste[2] # Die dritte (!) Stelle wird ausgegeben. \n\n\n\n\n"
Lesson3_0_SolutionCode = "gepaeck = ['Hose', 'Hemd', 'Jacke', 'Socken', 'Schuhe', 'Zahnbuerste']\nprint(gepaeck)"

Lesson3_0_StringBoolean = True
Lesson3_0_SolutionOutput ="[Hose, Hemd, Jacke, Socken, Schuhe, Zahnbuerste]"

Lesson3_0_AddedCodeBoolean = True
Lesson3_0_AddedCode = "" \
                      "\nif (gepaeck == ['Hose', 'Hemd', 'Jacke', 'Socken', 'Schuhe', 'Zahnbuerste']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"


Lesson3_0_Name = "Listen"




Lesson3_1_Text = "Lektion 3.1: \n\nHerzlichen Glückwunsch - du hast nun schon ein ganz schönes Stück Arbeit hinter dir! " \
	"Wir schreiten fort zu dem Themenkomplex der Kontrollstrukturen. Was das genau ist erfährst du jetzt: " \
	"In einem Programm möchte man oftmals in Abhängigkeit von einer bestimmten Bedingung unterschiedlich " \
	"verfahren. Dazu wird die Bedingung, die nach dem Befehl if (wenn) folgt, überprüft. " \
	"Ist diese wahr (True), so wird der Code ausgeführt, der direkt im Anschluss folgt. Um zu kennzeichnen, " \
	"dass der Code zu dem if-Block gehört wird er mit einem Tab eingerückt. Wenn der Code nicht mehr zu " \
	"dem if-Block gehört wird er nicht mehr eingedrückt.\n\n"\
	"Ist die Bedingung falsch (False), so wird  der Code nach else (‘sonst’) ausgeführt. Else selber wird nicht eingerückt " \
	"da es nicht zum if-Block gehört. Zwischen den if/else Blöcken darf nichts stehen dass nicht eingerückt ist, damit " \
	"Python weiß, dass das else zu dem if davor gehört. Nachdem der else-Block zuende ist, wird der Code wieder nicht eingerückt. " \
	"Monty möchte gerne noch ein Geschenk für Brian mitbringen. Er überlegt ob er " \
	"einen Strauss Blumen oder Schokolade kaufen soll. " \
	"Die Schokolade kostet 2 Euro und der Blumenstrauss 5 Euro. Finde mittels eines " \
	"if/else Konstrukts heraus ob Monty Blumen, Schokolade oder sogar beides kaufen kann. " \
	"\n\nEr würde lieber die Blumen als die Schokolade kaufen, deshalb teste zuerst ob er genug Geld " \
	"für die Blumen hat. Gebe auf dem Bildschirm die Gegenstände als String ('Blumenstrauss'/'Schokolade') aus, "\
	"die Monty kauft" \
	"Gebe danach aus wieviel Geld er noch übrig hat. Modifiziere das gegebene Beispiel. Monty hat 10Euro Taschengeld. "

Lesson3_1_GivenCode =   "\nblumenstrauss = 0 "\
			"\nschokolade = 0 "\
			"\ntaschengeld = 0 " \
			"\n" \
			"\n" \
			"\nif geldeinwurf > fahrpreis:"\
    			"\n\tRueckgabe = fahrpreis - geldeinwurf"\
			"\nelse: "\
    			"\n\trueckgabe = 0\n\n\n\n\n" \

Lesson3_1_SolutionCode = "if taschengeld > blumenstrauss:" \
				"\n\tprint 'Blumenstrauss' " \
				"\n\ttaschengeld = taschengeld - blumenstrauss" \
				"\nif taschengeld > schokolade " \
				"\n\tprint 'Schokolade' " \
				"\n\ttaschengeld = taschengeld - schokolade" \
				"\nprint taschengeld"

Lesson3_1_StringBoolean = True
Lesson3_1_SolutionOutput = "Blumenstrauss\nSchokolade\n3"

Lesson3_1_AddedCodeBoolean = True
Lesson3_1_AddedCode = 	"\nif (taschengeld == 3 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable taschengeld hat einen falschen Wert')" \
			"\nif (schokolade == 2 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable schokolade hat einen falschen Wert')" \
			"\nif (blumenstrauss == 5 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable blumenstrauss hat einen falschen Wert')"

Lesson3_1_Name = "if/else Konditionen"





########################################_4_Lektion_########################################

Lesson4_0_Text = "Lektion 4.0 \n\nWir haben in der letzten Lektion gelernt wie man mit Kontrollstrukturen im Programm je nach Situation" \
		" entscheiden kann. Bisher haben wir mit einem direkten Vergleich entschieden. Man kann jedoch auch " \
		"über sogennannte 'boolean' Variablen entscheiden lassen. \n\n\nDiese Variablen haben nur zwei mögliche Werte: "\
		" <True> und <False>. Wir können sie wie einen Vergleich einbauen, bloß dass wir die Variable vorher festgelegt haben " \
		"und wir keinen Vergleichsoperator mehr brauchen, da wir die Antwort ja schon festgelegt haben.\n\n" \
		"Dies kann nützlich sein wenn in einem vorhergegangenen if-else-Block bei dem if-Teil einer Variable 'True' zugewiesen hat "\
		"und beim else-Teil 'False'. \n\n\n"\
		" Belege eine Variable mit dem Namen 'Kondition' mit dem Wert <True> und schreibe einen if-else-Block in dem " \
		"falls die Variable mit <True> belegt wird der Satz 'Die Kondition ist wahr!' ausgegeben wird oder ansonsten der Satz: \n\n" \
		"'Kondition ist nicht wahr!'.\n\n\n\n\n\n\n\n\n\n\n"

Lesson4_0_GivenCode =   "PythonistCool = True\n\nif PythonistCool:\n\tprint 'Stimmt!'\n\n\n\n"

Lesson4_0_SolutionCode = "Kondition = True" \
			"\nif Kondition:" \
			"\n\tprint 'Die Kondition ist wahr!'" \
			"\nelse:" \
			"\n\tprint 'Die Kondition ist nicht wahr!' "

Lesson4_0_StringBoolean = True
Lesson4_0_SolutionOutput = "Die  Kondition ist wahr!"

Lesson4_0_AddedCodeBoolean = True
Lesson4_0_AddedCode = 	"\nif Kondition == True ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Kondition hat einen falschen Wert')"

Lesson4_0_Name = "Boolean Werte"







Lesson4_1_Text = "Lektion 4.1: \n\nNachdem wir jetzt den Grundstein für komplexere Entscheidungsstrukturen und Listen" \
		 "gelegt haben, gehen wir jetzt dazu über Listen dynamisch im Code zu manipulieren basierend auf Entscheidungen die wir vorher treffen. " \
		 "Um zu einer bestehenden Liste etwas hinzuzufügen (anzuhängen) ist der folgende Befehl nötig:\n\n " \
		 "<listenname.append(something)>. 'something' kann zum Beispiel ein String sein oder eine Zahl.\n\n" \
		 "Um etwas aus einer Liste zu entfernen ist der folgende Befehl nötig: \n" \
		 "listenname.remove(something). \n\n\n" \
		 "Schreibe einen if-else-Block mit dem du auswertest, ob Sommer ist oder nicht. Wenn Sommer ist, will " \
		 "Monty zuerst (!) seine 'Badehose' und dann die 'Sonnenbrille' einpacken statt der 'Jeans'. Falls kein Sommer ist, nimmt er zuerst (!) einen 'Pullover' mit " \
		 "und dann die 'Jacke', aber kein 'Hemd'. Gehe davon aus, dass es Herbst ist, wenn Monty in den Urlaub fahren will. " \
		 "Nach dem if/else Konstrukt gebe die gepaeck-Liste mit <print> aus. "


Lesson4_1_GivenCode =   "Sommer = True \ngepaeck = ['Jeans', 'Hemd', 'Socken', 'Schuhe', 'Zahnbuerste']\n\n\n\n\n"

Lesson4_1_SolutionCode = "Sommer = False \ngepaeck = ['Jeans', 'Hemd', 'Socken', 'Schuhe', 'Zahnbuerste']\n\nif Sommer:" \
			 "\n\tgepaeck.append('Badehose') " \
			 "\n\tgepaeck.append('Sonnenbrille') " \
			 "\n\tgepaeck.remove('Jeans') " \
			 "\nelse: " \
			 "\n\tgepaeck.append('Pullover') " \
			 "\n\tgepaeck.append('Jacke') " \
			 "\n\tgepaeck.remove('Hemd')" \
			 "\n\tprint gepaeck"

Lesson4_1_StringBoolean = True
Lesson4_1_SolutionOutput = "['Jeans', 'Socken','Schuhe','Zahnbuerste','Pullover','Jacke']"

Lesson4_1_AddedCodeBoolean = True
Lesson4_1_AddedCode = 	"\nif gepaeck == ['Jeans', 'Socken','Schuhe','Zahnbuerste','Pullover','Jacke'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')" \

Lesson4_1_Name = "Listenmanipulation I"



########################################_5_Lektion_########################################



Lesson5_0_Text = "Lektion 5.0: \n\n" \
		"Verzweigungen und Listen waren gar nicht so schwer, oder? Oftmals möchte man jedoch auch Code wiederholt ausführen — " \
		"hierfür verwenden Programmierer sogenannte Schleifen (engl. ‘loops’). " \
		"Loops funktionieren vom Aufbau wie if/else-Blöcke. Alles was eine Ausführung des Loops ausführen soll, wird eingerückt." \
		"Angenommen wir haben eine Liste mit ganzzahligen werten und "\
		"möchten zu jedem Wert 1 addieren, dann sähe das wie folgt aus:"\
		"\n\n\nliste = [0, 1, 2, 3]" \
		"\nfor zahl in liste" \
		"\nzahl = zahl + 1"\
		"\nprint liste" \
		"\n\nMan kann dies etwa so verstehen: \nFÜR Element IN Liste: \n\tführe diesen Code aus\nDiesen nicht mehr\n\n" \
		"Monty ist nach stundenlanger Fahrt endlich bei Brian angekommen." \
		"Nun möchte er seinen Koffer auspacken. Lege eine leere Listen-Variable 'kleiderschrank' an " \
		"und füge ihr alle Gegenstände aus der Gepäck-Liste hinzu und lösche sie gleichzeitig aus der gepaeck liste mithilfe eines Loops. " \
		"Gebe nach dem Loop zuerst die (dann leere) Variable gepaeck aus.\n\n\n\n\n\n\n\n"


Lesson5_0_GivenCode =   "gepaeck = ['Jeans', 'Hemd', 'Socken', 'Schuhe', 'Zahnbuerste']\n\n\n\n\n"

Lesson5_0_SolutionCode = "gepaeck = ['Jeans', 'Hemd', 'Socken', 'Schuhe', 'Zahnbuerste']" \
			"\nfor x in gepaeck: " \
			"\n\tKleiderschrank.append(x) " \
			"\n\t gepaeck.remove(x) " \
			"\nprint gepaeck" \
			"\nprint kleiderschrank"

Lesson5_0_StringBoolean = True
Lesson5_0_SolutionOutput = ""

Lesson5_0_AddedCodeBoolean = True
Lesson5_0_AddedCode = 	"\nif gepaeck == [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover','Winterschuhe'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"
Lesson5_0_Name = "For-Schleife"



Lesson5_1_Text = 	"Lektion 5.1: \n\nWie wir schon am Anfang bei Listen gelernt haben, Listen fangen bei '0' zu zählen an. Denke daran bei dieser Aufgabe! \n\n\n\n" \
			"Um den Index (also die Stelle) eines Elements in einer Liste herauszufinden, gibt es in Python den folgenden Befehl: \n" \
			"<listenname.index(something)>. \n\n\nGebe den Index der 'Schuhe' aus mit <print>. Anschließend füge mit dem Befehl <listenname.insert(index,'something')> an die Index-Stelle der Schuhe "  \
			"einen 'Regenschirm' ein. \nAlle Elemente die darauf folgen werden im Index um 1 erhöht, da ein Index immer nur mit einer Zahl belegt sein kann. \n\n\nDann gebe mit einer for-Schleife jeweils die einzelnen gepackten Gegenstaende aus und mit nachfolgendem <print> gleich den Index des Gegenstandes." \
			"\n\n\n\nWenn du die Aufgabe abgeschlossen hast, kontrolliere den Index der Schuhe vor und nach dem Einfügen des Regenschirms am selben Index!\n\n\n\n\n\n\n"

Lesson5_1_GivenCode =   "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']\n\n\n\n\n"

Lesson5_1_SolutionCode = 	"print gepaeck[1]" \
				"\ngepaeck.insert(1,'Regenschirm')" \
				"\nfor x in gepaeck:" \
				"\n\tprint x " \
				"\n\tprint gepaeck.index(x)"


Lesson5_1_StringBoolean = True
Lesson5_1_SolutionOutput = "1\nSocken\n0\nRegenschirm\n1\nSchuhe\n2\nZahnbuerste\n3\nPullover\n4\nWinterschuhe\n5"

Lesson5_1_AddedCodeBoolean = True
Lesson5_1_AddedCode = 	"\nif gepaeck == [ 'Socken' ,'Regenschirm' ,'Schuhe', 'Zahnbuerste', 'Pullover','Winterschuhe'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')" \

Lesson5_1_Name = "Listen - Index und Insert"





Lesson5_2_Text = "Lektion 5.2: \n\nIn dieser Aufgabe wollen wir nun kombinieren was wir bisher gelernt haben." \
		" Brian möchte Monty nun noch einige Gegenstände als Geschenk mitgeben, welche " \
		" jedoch möglicherweise nicht alle in seinen Koffer passen. \n\nSchreibe eine for-Schleife " \
		"und teile die Gegenstände so auf die Koffer auf, dass sich in keinem Koffer mehr als 5 Dinge befinden!\n\n\n" \
		"Packe mit einer for-Schleife in der ein if-Block ist, so lange Gegenstände in den ersten Koffer hinein bis dieser voll ist. \n" \
		"Dann beginne den zweiten Koffer zu packen und schließlich den dritten. Anschließend gebe den Inhalt " \
		"der Koffer in dieser Reihenfolge aus. \n\n\n" \
        "Um diese Aufgabe zu lösen musst du noch zwei weitere Befehle kennen:\n\n" \
        "1. Die Länge einer Liste können wir mit <len(listenname)> herausfinden. (Denke daran, letzter Index = Länge-1, da wir " \
        "bei Listen anfangen mit 0 zu zählen!" \
        "\n\n" \
        "2. Mit dem Vergleichsoperator <==> können wir Zahlen, Listen und andere Variablen vergleichen!\n\n\n\n\n\n\n\n"

Lesson5_2_GivenCode =  "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe', 'Schokolade', 'Buch', " \
            "\n'Kamera', 'Bonbons', 'Souvenirs', 'Kuchen', 'Taschenlampe']" \
            "\n4 == 5 # Dies ergibt 'False'" \
            "\n5 == 5 # Dies ergibt 'True'" \
            "\nkoffer_1 = []" \
            "\nkoffer_2 = []" \
            "\nkoffer_3 = []\n\n\n\n\n\n"

Lesson5_2_SolutionCode = "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe', 'Schokolade', "\
            "'Buch',  'Kamera', 'Bonbons', 'Souvenirs', 'Kuchen', 'Taschenlampe'] "\
            "koffer_1 = []" \
            "koffer_2 = []" \
            "koffer_3 = []" \
            "zaehler = 1" \
            "\nfor x in gepaeck: " \
                "if (len(koffer_1) == 5):" \
                    "if (len(koffer_2) == 5):" \
                        "koffer_3.append(x)" \
                    "else:" \
                        "koffer_2.append(x)" \
                "else:"\
                    "koffer_1.append(x)" \
            "print koffer_1" \
            "print koffer_2" \
            "print koffer_3"

Lesson5_2_StringBoolean = True
Lesson5_2_SolutionOutput = "['Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                            "\n['Schokolade', 'Buch',  'Kamera', 'Bonbons', 'Souvenirs']" \
                            "\n['Kuchen', 'Taschenlampe']"

Lesson5_2_AddedCodeBoolean = True
Lesson5_2_AddedCode =   "\nif koffer_1 == ['Winterschuhe', 'Pullover', 'Zahnbuerste', 'Schuhe', 'Socken']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable koffer_1 hat einen falschen Wert')" \
                        "\nif koffer_2 == ['Schokolade', 'Buch',  'Kamera', 'Bonbons', 'Souvenirs']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable koffer_2 hat einen falschen Wert')" \
                        "\nif koffer_3 == ['Kuchen', 'Taschenlampe']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable koffer_3 hat einen falschen Wert')"

Lesson5_2_Name = "Listen splitten"





Lesson5_3_Text =    "Lektion 5.3:\n\nUm noch etwas vertrauter mit dem Thema Listen zu werden, das sehr elementar und wichtig ist " \
		            "noch eine Aufgabe hierzu: \n\nDrehe den Inhalt einer gegebenen Liste um und speichere ihn in einer " \
		            "neuen variablen. Gebe diese am Ende mit print aus.\n\n\n(Denke darüber nach in welcher Reihenfolge eine for-Schleife " \
                    "die Liste durchgeht und an welcher Stelle (Index) du Variablen in eine neue Liste einfügen musst um die Variablen" \
                    "-Reihenfolge umzudrehen.)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_3_GivenCode =  "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "gepaeck_gedreht = []"

Lesson5_3_SolutionCode = "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "gepaeck_gedreht = []" \
                        "for x in gepaeck:"\
                            "gepaeck_gedreht.insert(0, x)" \
                        "print gepaeck_gedreht"

Lesson5_3_StringBoolean = True
Lesson5_3_SolutionOutput = "['Winterschuhe', 'Pullover', 'Zahnbuerste', 'Schuhe', 'Socken']" \

Lesson5_3_AddedCodeBoolean = True
Lesson5_3_AddedCode =  "\nif gepaeck == ['Winterschuhe', 'Pullover', 'Zahnbuerste', 'Schuhe', 'Socken']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"

Lesson5_3_Name = "Listen umdrehen"





Lesson5_4_Text = "Lektion 5.4:\n\nOftmals ist es sehr praktisch zu prüfen ob sich ein bestimmtes Element in einer Liste befindet, oder nicht. \n\n" \
                 "Dies können wir mit der Python-Funktion <in> prüfen -- zum Beispiel <'Schuhe' in gepaeck> ergibt True oder False, " \
                 "je nach dem ob sich das Element 'Schuhe' in der Liste gepaeck befindet. \n\n\nSchreibe ein Programm, " \
                 "welches die Schnittmenge von 2 Listen in einer neuen Liste speichert und diese auf dem Bildschirm ausgibt.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_4_GivenCode =  "gepaeck_1 = ['Socken', 'Schuhe', 'Zahnbürste', 'Pullover', 'Winterschuhe']" \
                        "\ngepaeck_2 = ['Buecher', 'Socken', 'Pullover', 'Schokolade', 'Schuhe']" \
                        "\nschnittmenge = []"

Lesson5_4_SolutionCode = "gepaeck_1 = ['Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "\ngepaeck_2 = ['Buecher', 'Socken', 'Pullover', 'Schokolade', 'Schuhe']" \
                        "\nfor x in gepaeck_1:"\
                            "\n\tif x in gepaeck_2:"\
                                "\n\t\tschnittmenge.append(x)" \
                        "\nprint schnittmenge"

Lesson5_4_StringBoolean = True
Lesson5_4SolutionOutput = "['Socken', 'Schuhe', 'Pullover']"

Lesson5_4_AddedCodeBoolean = True
Lesson5_4_AddedCode = "\nif gepaeck == ['Socken', 'Schuhe', 'Pullover']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"

Lesson5_4_Name = "Schnittmengen von Listen"





Lesson5_5_Text = "Lektion 5.5:\n\nManchmal ist es ganz nuetzlich, wenn man die Anzahl gewisser Zeichen in einem String zählen kann.\n" \
                 "String funktionieren eigentlich wie Listen. Wir können für jedes Zeichen etwas testen wenn wir wie bei den Listen " \
                 "mit einer for-Schleife <for x in String> statt jedem Element in einer Liste jeden einzelnen Buchstaben eines Strings 'einmal in die Hand nehmen'\n\n. Für Vergleiche mit Strings " \
                 "benutzen wir den Vergleichsoperator <'a' == 'b'> (der uns in diesem Fall 'False' herausgeben würde).\n\n\n "\
		        "Suche dazu die Anzahl der 'e' und die der 'l' in dem Satz: 'dies ist die letzte lektion, ich hoffe es hat euch gefallen!' \n\n" \
                 "Gebe am Ende erst 'Anzahl der e: ' (mit angehängter Anzahl) aus und dann dasselbe mit 'l'. \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_5_GivenCode = "Text ='dies ist die letzte lektion, ich hoffe es hat euch gefallen!'"\
		       "\nanzahl_e=0"\
		       "\nanzahl_l=0" \
               "\n\n\n\n\n" \
               "\nstring_anzahl_e = str(anzahl_e)" \
               "\nprint 'Anzahl der e:' + string_anzahl_e)\n\n"

Lesson5_5_SolutionCode = "Text ='dies ist die letzte lektion, ich hoffe es hat euch gefallen!'"\
		          "anzahl_e=0"\
		          "anzahl_l=0"\
			  "for zeichen in Text:"\
				"if zeichen == 'e':"\
					"anzahl_e=anzahl_e+1"\
			  "print 'Anzahl der e: ', anzahl_e"\
			  "for zeichen in Text:"\
				"if zeichen == 'l':"\
					"anzahl_l=anzahl_l+1"\
			  "print 'Anzahl der l: ', anzahl_l"\

Lesson5_5_StringBoolean = True
Lesson5_5_SolutionOutput =  "Anzahl der e:  10" \
			                "\nAnzahl der l:  4"

Lesson5_5_AddedCodeBoolean = True
Lesson5_5_AddedCode = 	"\nif anzahl_e == 10 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable anzahl_e hat einen falschen Wert')" \
                        "\nif anzahl_l == 4 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable anzahl_l hat einen falschen Wert')"

Lesson5_5_Name = "Stringsuche"










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
    global Lesson0_0_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson1_3_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson2_2_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson4_0_GivenCode
    global Lesson4_1_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode
    # Clear Code
    txt.delete(1.0,'end')
    # Insert original state
    if current_Lesson == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    elif current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    elif current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    elif current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    elif current_Lesson == 4:
        txt.insert(1.0,Lesson1_3_GivenCode, END)
    elif current_Lesson == 5:
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    elif current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    elif current_Lesson == 7:
        txt.insert(1.0,Lesson2_2_GivenCode, END)
    elif current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    elif current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    elif current_Lesson == 10:
        txt.insert(1.0,Lesson4_0_GivenCode, END)
    elif current_Lesson == 11:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    elif current_Lesson == 12:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    elif current_Lesson == 13:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    elif current_Lesson == 14:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    elif current_Lesson == 15:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    elif current_Lesson == 16:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    elif current_Lesson == 17:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    elif current_Lesson > 17:
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
    global Lesson1_3_SolutionOutput
    global Lesson1_3_AddedCodeBoolean
    global Lesson1_3_AddedCode

    global Lesson2_0_StringBoolean
    global Lesson2_0_SolutionOutput#
    global Lesson2_0_AddedCodeBoolean
    global Lesson2_0_AddedCode

    global Lesson2_1_StringBoolean
    global Lesson2_1_SolutionOutput#
    global Lesson2_1_AddedCodeBoolean
    global Lesson2_1_AddedCode

    global Lesson2_2_StringBoolean
    global Lesson2_2_SolutionOutput#
    global Lesson2_2_AddedCodeBoolean
    global Lesson2_2_AddedCode

    global Lesson3_0_StringBoolean
    global Lesson3_0_SolutionOutput#
    global Lesson3_0_AddedCodeBoolean
    global Lesson3_0_AddedCode

    global Lesson3_1_StringBoolean
    global Lesson3_1_SolutionOutput#
    global Lesson3_1_AddedCodeBoolean
    global Lesson3_1_AddedCode

    global Lesson4_0_StringBoolean
    global Lesson4_0_SolutionOutput#
    global Lesson4_0_AddedCodeBoolean
    global Lesson4_0_AddedCode

    global Lesson4_1_StringBoolean
    global Lesson4_1_SolutionOutput#
    global Lesson4_1_AddedCodeBoolean
    global Lesson4_1_AddedCode

    global Lesson5_0_StringBoolean
    global Lesson5_0_SolutionOutput#
    global Lesson5_0_AddedCodeBoolean
    global Lesson5_0_AddedCode

    global Lesson5_1_StringBoolean
    global Lesson5_1_SolutionOutput#
    global Lesson5_1_AddedCodeBoolean
    global Lesson5_1_AddedCode

    global Lesson5_2_StringBoolean
    global Lesson5_2_SolutionOutput#
    global Lesson5_2_AddedCodeBoolean
    global Lesson5_2_AddedCode

    global Lesson5_3_StringBoolean
    global Lesson5_3_SolutionOutput#
    global Lesson5_3_AddedCodeBoolean
    global Lesson5_3_AddedCode

    global Lesson5_4_StringBoolean
    global Lesson5_4_SolutionOutput#
    global Lesson5_4_AddedCodeBoolean
    global Lesson5_4_AddedCode

    global Lesson5_5_StringBoolean
    global Lesson5_5_SolutionOutput#
    global Lesson5_5_AddedCodeBoolean
    global Lesson5_5_AddedCode

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
        StringBoolean = Lesson2_0_StringBoolean
        SolutionOutput = Lesson2_0_SolutionOutput
        AddedCodeBoolean = Lesson2_0_AddedCodeBoolean
        AddedCode = Lesson2_0_AddedCode

    if current_Lesson == 6:
        StringBoolean = Lesson2_1_StringBoolean
        SolutionOutput = Lesson2_1_SolutionOutput
        AddedCodeBoolean = Lesson2_1_AddedCodeBoolean
        AddedCode = Lesson2_1_AddedCode

    if current_Lesson == 7:
        StringBoolean = Lesson2_2_StringBoolean
        SolutionOutput = Lesson2_2_SolutionOutput
        AddedCodeBoolean = Lesson2_2_AddedCodeBoolean
        AddedCode = Lesson2_2_AddedCode

    if current_Lesson == 8:
        StringBoolean = Lesson3_0_StringBoolean
        SolutionOutput = Lesson3_0_SolutionOutput
        AddedCodeBoolean = Lesson3_0_AddedCodeBoolean
        AddedCode = Lesson3_0_AddedCode

    if current_Lesson == 9:
        StringBoolean = Lesson3_1_StringBoolean
        SolutionOutput = Lesson3_1_SolutionOutput
        AddedCodeBoolean = Lesson3_1_AddedCodeBoolean
        AddedCode = Lesson3_1_AddedCode

    if current_Lesson == 10:
        StringBoolean = Lesson4_0_StringBoolean
        SolutionOutput = Lesson4_0_SolutionOutput
        AddedCodeBoolean = Lesson4_0_AddedCodeBoolean
        AddedCode = Lesson4_0_AddedCode

    if current_Lesson == 11:
        StringBoolean = Lesson4_1_StringBoolean
        SolutionOutput = Lesson4_1_SolutionOutput
        AddedCodeBoolean = Lesson4_1_AddedCodeBoolean
        AddedCode = Lesson4_1_AddedCode

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
    global current_Lesson
    global Lesson_Number
    global maxLessons
    global button1
    global button
    global current_Lesson
    global Lesson0_0_Text
    global Lesson1_0_Text
    global Lesson1_1_Text
    global Lesson1_2_Text
    global Lesson1_3_Text
    global Lesson2_0_Text
    global Lesson2_1_Text
    global Lesson2_2_Text
    global Lesson3_0_Text
    global Lesson3_1_Text
    global Lesson4_0_Text
    global Lesson4_1_Text
    global Lesson5_0_Text
    global Lesson5_1_Text
    global Lesson5_2_Text
    global Lesson5_3_Text
    global Lesson5_4_Text
    global Lesson5_5_Text
    global Lesson0_0_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson1_3_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson2_2_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson4_0_GivenCode
    global Lesson4_1_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode


    global booleanboohja
    booleanboohja = False

    current_Lesson +=   1
    Lesson_Number+= 1


    if current_Lesson == 5:
        on_closing()
    elif current_Lesson == 7:
        on_closing()
    elif current_Lesson == 10:
        on_closing()
    elif current_Lesson == 12:
        on_closing()
    elif current_Lesson == 18:
        on_closing()


    if current_Lesson > maxLessons:
        current_Lesson = maxLessons

    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons


    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=30, column = 1)


    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

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
        label1.config(text= Lesson2_0_Text)
    if current_Lesson == 6:
        label1.config(text= Lesson2_1_Text)
    if current_Lesson == 7:
        label1.config(text= Lesson2_2_Text)
    if current_Lesson == 8:
        label1.config(text= Lesson3_0_Text)
    if current_Lesson == 9:
        label1.config(text= Lesson3_1_Text)
    if current_Lesson == 10:
        label1.config(text= Lesson4_0_Text)
    if current_Lesson == 11:
        label1.config(text= Lesson4_1_Text)
    if current_Lesson == 12:
        label1.config(text= Lesson5_0_Text)
    if current_Lesson == 13:
        label1.config(text= Lesson5_1_Text)
    if current_Lesson == 14:
        label1.config(text= Lesson5_2_Text)
    if current_Lesson == 15:
        label1.config(text= Lesson5_3_Text)
    if current_Lesson == 16:
        label1.config(text= Lesson5_4_Text)
    if current_Lesson == 17:
        label1.config(text= Lesson5_5_Text)
    if current_Lesson > 17:
        1+1 # Return to the game!

    # Change Code
    txt.delete(1.0,'end')

    if current_Lesson == 0:
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    elif current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    elif current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    elif current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    elif current_Lesson == 4:
        txt.insert(1.0,Lesson1_3_GivenCode, END)
    elif current_Lesson == 5:
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    elif current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    elif current_Lesson == 7:
        txt.insert(1.0,Lesson2_2_GivenCode, END)
    elif current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    elif current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    elif current_Lesson == 10:
        txt.insert(1.0,Lesson4_0_GivenCode, END)
    elif current_Lesson == 11:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    elif current_Lesson == 12:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    elif current_Lesson == 13:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    elif current_Lesson == 14:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    elif current_Lesson == 15:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    elif current_Lesson == 16:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    elif current_Lesson == 17:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    elif current_Lesson > 17:
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

    current_Lesson = 4
    deletebuttons()

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
    global Lesson2_0_Text
    global Lesson2_0_GivenCode

    deletebuttons()

    current_Lesson = 5
    label1.config(text= Lesson2_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson2_0_GivenCode, END)

    reinstate_buttons()

def lesson6():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson2_1_Text
    global Lesson2_1_GivenCode

    current_Lesson = 6
    deletebuttons()

    label1.config(text= Lesson2_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson2_1_GivenCode, END)

    reinstate_buttons()


def lesson7():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson2_2_Text
    global Lesson2_2_GivenCode

    deletebuttons()

    current_Lesson = 7
    label1.config(text= Lesson2_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson2_2_GivenCode, END)


    reinstate_buttons()



def lesson8():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson3_0_Text
    global Lesson3_0_GivenCode

    deletebuttons()

    current_Lesson = 8
    label1.config(text= Lesson3_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson3_0_GivenCode, END)

    reinstate_buttons()


def lesson9():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson3_1_Text
    global Lesson3_1_GivenCode

    deletebuttons()

    current_Lesson = 9
    label1.config(text= Lesson3_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson3_1_GivenCode, END)

    reinstate_buttons()


def lesson10():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson4_0_Text
    global Lesson4_0_GivenCode

    deletebuttons()

    current_Lesson = 10
    label1.config(text= Lesson4_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson4_0_GivenCode, END)

    reinstate_buttons()



def lesson11():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson4_1_Text
    global Lesson4_1_GivenCode

    deletebuttons()

    current_Lesson = 11
    label1.config(text= Lesson4_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson4_1_GivenCode, END)

    reinstate_buttons()




def lesson12():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_0_Text
    global Lesson5_0_GivenCode

    deletebuttons()

    current_Lesson = 12
    label1.config(text= Lesson5_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_0_GivenCode, END)

    reinstate_buttons()



def lesson13():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_1_Text
    global Lesson5_1_GivenCode

    deletebuttons()

    current_Lesson = 13
    label1.config(text= Lesson5_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_1_GivenCode, END)

    reinstate_buttons()


def lesson14():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_2_Text
    global Lesson5_2_GivenCode

    deletebuttons()

    current_Lesson = 14
    label1.config(text= Lesson5_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_2_GivenCode, END)

    reinstate_buttons()


def lesson15():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_3_Text
    global Lesson5_3_GivenCode

    deletebuttons()

    current_Lesson = 15
    label1.config(text= Lesson5_3_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_3_GivenCode, END)

    reinstate_buttons()



def lesson16():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_4_Text
    global Lesson5_4_GivenCode

    deletebuttons()

    current_Lesson = 16
    label1.config(text= Lesson5_4_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_4_GivenCode, END)

    reinstate_buttons()


def lesson17():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_5_Text
    global Lesson5_5_GivenCode

    deletebuttons()

    current_Lesson = 17
    label1.config(text= Lesson5_5_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_5_GivenCode, END)

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
    global buttonlesson8
    global buttonlesson9
    global buttonlesson10
    global buttonlesson11
    global buttonlesson12
    global buttonlesson13
    global buttonlesson13
    global buttonlesson14
    global buttonlesson15
    global buttonlesson16
    global buttonlesson17

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
    if Lesson_Number >= 8:
        buttonlesson8.destroy()
    if Lesson_Number >= 9:
        buttonlesson9.destroy()
    if Lesson_Number >= 10:
        buttonlesson10.destroy()
    if Lesson_Number >= 11:
        buttonlesson11.destroy()
    if Lesson_Number >= 12:
        buttonlesson12.destroy()
    if Lesson_Number >= 13:
        buttonlesson13.destroy()
    if Lesson_Number >= 14:
        buttonlesson14.destroy()
    if Lesson_Number >= 15:
        buttonlesson15.destroy()
    if Lesson_Number >= 16:
        buttonlesson16.destroy()
    if Lesson_Number >= 17:
        buttonlesson17.destroy()




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
    global buttonlesson8
    global buttonlesson9
    global buttonlesson10
    global buttonlesson11
    global buttonlesson12
    global buttonlesson13
    global buttonlesson14
    global buttonlesson15
    global buttonlesson16
    global buttonlesson17
    global Lesson0_0_Name
    global Lesson1_0_Name
    global Lesson1_1_Name
    global Lesson1_2_Name
    global Lesson2_0_Name
    global Lesson2_1_Name
    global Lesson2_2_Name
    global Lesson3_0_Name
    global Lesson3_1_Name
    global Lesson4_0_Name
    global Lesson4_1_Name
    global Lesson5_0_Name
    global Lesson5_1_Name
    global Lesson5_2_Name
    global Lesson5_3_Name
    global Lesson5_4_Name
    global Lesson5_5_Name

    if Lesson_Number >= 0:
        buttonlesson0 = Button(root, text='L.0 %r' %Lesson0_0_Name, command=lesson0 )
        buttonlesson0.grid(row=0, column = 0)

    if Lesson_Number >= 1:
        buttonlesson1 = Button(root, text='L.1 %r' %Lesson1_0_Name, command=lesson1 )
        buttonlesson1.grid(row=1, column = 0)

    if Lesson_Number >= 2:
        buttonlesson2 = Button(root, text='L.1.1 %r' %Lesson1_1_Name, command=lesson2 )
        buttonlesson2.grid(row=2, column = 0)

    if Lesson_Number >= 3:
        buttonlesson3 = Button(root, text='L.1.2 %r' %Lesson1_2_Name, command=lesson3 )
        buttonlesson3.grid(row=3, column = 0)

    if Lesson_Number >= 4:
        buttonlesson4 = Button(root, text='L.1.3 %r' %Lesson1_3_Name, command=lesson4 )
        buttonlesson4.grid(row=4, column = 0)

    if Lesson_Number >= 5:
        buttonlesson5 = Button(root, text='L.2.0 %r' %Lesson2_0_Name, command=lesson5 )
        buttonlesson5.grid(row=5, column = 0)

    if Lesson_Number >= 6:
        buttonlesson6 = Button(root, text='L.2.1 %r' %Lesson2_1_Name, command=lesson6 )
        buttonlesson6.grid(row=6, column = 0)

    if Lesson_Number >= 7:
        buttonlesson7 = Button(root, text='L.2.2 %r' %Lesson2_2_Name, command=lesson7 )
        buttonlesson7.grid(row=7, column = 0)

    if Lesson_Number >= 8:
        buttonlesson8 = Button(root, text='L.3.0 %r' %Lesson3_0_Name, command=lesson8 )
        buttonlesson8.grid(row=8, column = 0)

    if Lesson_Number >= 9:
        buttonlesson9 = Button(root, text='L.3.1 %r' %Lesson3_1_Name, command=lesson9 )
        buttonlesson9.grid(row=9, column = 0)

    if Lesson_Number >= 10:
        buttonlesson10 = Button(root, text='L.4.0 %r' %Lesson4_0_Name, command=lesson10 )
        buttonlesson10.grid(row=10, column = 0)

    if Lesson_Number >= 11:
        buttonlesson11 = Button(root, text='L.4.1 %r' %Lesson4_1_Name, command=lesson11)
        buttonlesson11.grid(row=11, column = 0)

    if Lesson_Number >= 12:
        buttonlesson12 = Button(root, text='L.5.0 %r' %Lesson5_0_Name, command=lesson12)
        buttonlesson12.grid(row=12, column = 0)

    if Lesson_Number >= 13:
        buttonlesson13 = Button(root, text='L.5.1 %r' %Lesson5_1_Name, command=lesson13)
        buttonlesson13.grid(row=13, column = 0)

    if Lesson_Number >= 14:
        buttonlesson14 = Button(root, text='L.5.2 %r' %Lesson5_2_Name, command=lesson14)
        buttonlesson14.grid(row=14, column = 0)

    if Lesson_Number >= 15:
        buttonlesson15 = Button(root, text='L.5.3 %r' %Lesson5_3_Name, command=lesson15 )
        buttonlesson15.grid(row=15, column = 0)

    if Lesson_Number >= 16:
        buttonlesson16 = Button(root, text='L.5.4 %r' %Lesson5_4_Name, command=lesson16 )
        buttonlesson16.grid(row=16, column = 0)

    if Lesson_Number >= 17:
        buttonlesson17 = Button(root, text='L.5.5 %r' %Lesson5_5_Name, command=lesson17 )
        buttonlesson17.grid(row=17, column = 0)

    # list all lessons

def get_current_and_achieved_Lesson_number():
    global current_Lesson
    global Lesson_Number
    global maxLessons
    global Lesson0_0_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson1_3_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson2_2_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson4_0_GivenCode
    global Lesson4_1_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode
    global Lesson0_0_Text
    global Lesson1_0_Text
    global Lesson1_1_Text
    global Lesson1_2_Text
    global Lesson1_3_Text
    global Lesson2_0_Text
    global Lesson2_1_Text
    global Lesson2_2_Text
    global Lesson3_0_Text
    global Lesson3_1_Text
    global Lesson4_0_Text
    global Lesson4_1_Text
    global Lesson5_0_Text
    global Lesson5_1_Text
    global Lesson5_2_Text
    global Lesson5_3_Text
    global Lesson5_4_Text
    global Lesson5_5_Text
    global txt
    global label1



    comm_file = open("communication_file.txt","r")
    communication = [x.strip('\n') for x in comm_file.readlines()]
    comm_file.close()

    if communication != []:
        current_Lesson = int(communication[0])
        Lesson_Number = current_Lesson

    if current_Lesson > maxLessons:
        current_Lesson = maxLessons

    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons

    print current_Lesson
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
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    if current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    if current_Lesson == 7:
        txt.insert(1.0,Lesson2_2_GivenCode, END)
    if current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    if current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    if current_Lesson == 10:
        txt.insert(1.0,Lesson4_0_GivenCode, END)
    if current_Lesson == 11:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    if current_Lesson == 12:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    if current_Lesson == 13:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    if current_Lesson == 14:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    if current_Lesson == 15:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    if current_Lesson == 16:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    if current_Lesson == 17:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    if current_Lesson > 17:
        1+1 # Return to the game!


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
        label1.config(text= Lesson2_0_Text)
    if current_Lesson == 6:
        label1.config(text= Lesson2_1_Text)
    if current_Lesson == 7:
        label1.config(text= Lesson2_2_Text)
    if current_Lesson == 8:
        label1.config(text= Lesson3_0_Text)
    if current_Lesson == 9:
        label1.config(text= Lesson3_1_Text)
    if current_Lesson == 10:
        label1.config(text= Lesson4_0_Text)
    if current_Lesson == 11:
        label1.config(text= Lesson4_1_Text)
    if current_Lesson == 12:
        label1.config(text= Lesson5_0_Text)
    if current_Lesson == 13:
        label1.config(text= Lesson5_1_Text)
    if current_Lesson == 14:
        label1.config(text= Lesson5_2_Text)
    if current_Lesson == 15:
        label1.config(text= Lesson5_3_Text)
    if current_Lesson == 16:
        label1.config(text= Lesson5_4_Text)
    if current_Lesson == 17:
        label1.config(text= Lesson5_5_Text)
    if current_Lesson > 17:
        1+1 # Return to the game!



########### GUI ###########



#5,8,10,12,18,



texter = ""

w = Canvas(root, width=300, height=650)
w.grid(row=0, column =0, columnspan = 4, rowspan=30)
w.create_rectangle(0, 0, 305, 655, fill="white")

c = Canvas(root, width=5, height=650)
c.grid(row=0, column =5, rowspan = 30) # 0-29
c.create_rectangle(0, 0, 200, 655, fill="grey")


label1 = Label(root, text=texter ,  justify=LEFT, wraplength= 250, bg ="white")
label1.grid(row=0, column =0, columnspan = 4, rowspan = 30) # 0-29

button = Button(root, text='Check Code', command=checkRunCode)
button.grid(row=30, column = 1)
button1 = Button(root, text='Weiter', command = nextLesson)
button1.grid(row=30, column=3)
button2 = Button(root, text ='Archive', command = archive)
button2.grid(row=30, column = 2)
button3 = Button (root, text='Reset Code', command=reset)
button3.grid(row =30, column = 6)



txt_frm = Frame(root,width=100, height=100).grid(row=0, column=6)
txt = Text(txt_frm,height = 27, width = 80,  bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=1, rowspan = 29 ,sticky="n") # 0-28
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))
txt.pack_propagate()


cmd_frm = Frame(root).grid(row=29,column=6,sticky="nsew")
cmd = Text(cmd_frm, height = 13, width = 80, bg="white", fg="black")
cmd.config(font=("Courier", 10), undo=True, wrap='word')
cmd.grid(row = 29, column = 6, sticky="nw")
cmd.configure(state='disabled')
cmd.pack_propagate()


get_current_and_achieved_Lesson_number()

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




