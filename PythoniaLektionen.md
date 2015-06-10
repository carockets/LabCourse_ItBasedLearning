#Pyhtonia Lektionen
[TOC]

###Lektion 0 — ‘print’
####Einführung

Hallo und herzlich willkommen bei Pythonia. In der nächsten Stunde wirst du spielend die Grundlagen des Programmierens mit Python lernen. Du wirst sehen, dass es gar nicht so schwer ist mit einem Computer zu reden und ihm zu sagen, was er tun soll. Die Sprache, die wir hierfür benutzen heißt Python. Wenn du noch nie programmier haben solltest, so ist das überhaupt kein Problem. Wir werden dich Schritt für Schritt durch die Lektionen führen und dir zeigen, was du tun musst um am Ende Pythonia zurückzuerobern. Also lass uns gleich beginnen :)

Zuerst wirst du lernen, wie du Text auf dem Bilschrim anzeigen lassen kannst. Pyhton gibt es hierfür den Befehl ‘print’. Um “Hallo Welt” auf der Konsole auszugeben scheiben wir einfach:

```python
print “Hello World”
```
####Aufgaben
|Lernziel | Umsetzung |Zeitaufwand |
|---------|-----------|------------|
|Die Schüler lernen wie sich Texte im Programm ausgeben lassen| Lasse deinen Namen mit dem Text “Hallo, mein Name ist …” ausgeben |5 min|
####Lösungsbeispiel
```python
print “Hallo, mein Name ist …”
```

##Unit 1
###Lektion 1 — Variablen
####Einführung
Super, die erste Lektion hast du geschafft. Weiter gehts mit dem Thema Variablen, einem essentiellen Konstrukt beim Programmieren.
Variablen erfüllen bei der Programmierung genau den gleichen Zweck wie in der Mathematik — sie können verschiedene Werte annehmen, mit denen dann gerechnet wird. Eine Variable hat immer einen Namen und einen Wert. Wenn wir zum Beispiel eine Variable mit dem Namen ‘x’ erstellen wollen, die den Wert 5 hat, dann können wir schreiben 

```python
x = 5 
```

Das Zeichen ‘=’ ist in diesem Sinne als Zuweisung zu verstehen. Wir sagen also “der Variablen x wird der Wert 5 zugewiesen”. Name einer Variablet kann beliebig gewählt werden bis auf die so genannten reservierten wörter, die es in jeder Programmiersprache gibt. Diese  haben eine spezielle Bedeutung und dürfen nicht als Variablen Bezeichner verwendet werden, da es sonst zu Konflikten kommt. Eine Liste mit der reservierten Wörter in Python ist [hier](https://docs.python.org/2.5/ref/keywords.html) zu finden.

Bei der Programmierung können Variablen nicht nur die Werte von Zahlen haben, sondern zum Beispiel auch eine Zeichenkette (eng. string) symbolisieren. Die Werte, die eine Variable annehmen kann werden in so genannten **Datentypen** kategorisiert. Die folgende Tabelle beinhaltet die wichtigsten und Beispiele, wie sie in Python geschrieben werden.

|Datentyp | Code Beispiel |
|---------|-----------|
| Ganze Zahlen (Integer)| `x = 3, y = 42, z = -7` |
| Fließkommazahlen (Floats) | `i = 3.1415, j = -89.34279` |
| Zeichenketten (Strings) | `text = “Hello World”` |
| Boolsche Variablen (Boolean) | `wahr = true, falsch = false` |

Boolsche Variablen sind beim Programmieren sehr wichtig. Sie können nur die Werte `true` und `false` annehmen.

####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
|Eine Integer Variable anlegen und den Wert auf dem Bildschrim ausgeben lassen|Lege nun selbst eine Variable mit dem Namen ‘Zahl’ an, die den Wert 5 hat, und lasse anschließend, den Wert auf dem Bildschirm ausgeben |4 min|
|Variablen gegenseitig zuweisen |Lege eine zweite Variable mit dem Namen ‘pi’ an und gib ihr den Wert 3.1415. Anschließend weise der Variable ‘pi’ den Wert von ‘zahl’ zu |2 min|
|Variablen mit Zeichenketten anlegen| | 2 min|
|Boolsche Variablen anlegen | | 2 min|

####Lösungsbeispiel
```python
zahl = 5
print ‘zahl’

pi = 3.1415
zahl = pi
```

###Lektion 2 — Arithmetik
####Einführung
Nachdem du nun schon das Thema Variablen gemeistert hast, wird es für dich ein leichtes sein ein bisschen mit dem Computer zu rechnen.
Wenn ein Programm von einem Computer ausgeführt wird, dann wird vor allem viel gerechnet. Am meisten verwenden wir beim Programmieren die Addition, Subtraktion, Multiplikation und Division.

Die folgende Tablle zeigt Beispiele hierfür in Python:

|Operation | Code Beispiel |
|---------|-----------|
| Addition | `x = 3 + 7.2355, y = -89 + 1732` |
| Subtraktion | `i = 3.1415 - 14.56, j = -89.34279 - 7` |
| Multiplikation | `quadrat = 42 * 42` |
| Division | `haelfte = 100 / 2` |

Eine Operation, die du vielleicht noch nicht kennst ist die **modulo** Operation, welche bei einer ganzzahligen Division den Rest bestimmt. Sie ist sehr praktisch und wird beim Programmieren häufig eingesetzt. Der modulo Operator ist das Prozentzeichen `%`. Folgendes Beispiel dient der Veranschaulichung:
```python
# Die Varialble ‘rest’ bekommt den Wert 2, da beim Teilen von 7 durch 5 ein Rest von 2 bleibt
rest = 7 % 5

# Die Variable ‘teiler’ bekommt den Wert 0, da 14 ohne Rest durch 7 teilbar ist
teiler = 14 % 7
```

In Pyhton kann auch mit Zeichenketten ‘gerechnet’ werden. Um Beispielsweise zwei Texte zusammenzufügen können wir schreiben:
```python
text = “Hello “ + “World”	# ergibt “Hello World”
wiederhole = “drei” * 3		# ergibt “dreidreidrei”
```
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
|Eine einfache Rechenaufgabe lösen|Zum Einstieg löse bitte folgende einfache Aufgabe: Monty möchte demnächst seinen Freund Brian besuchen fahren und wissen, wie viel ihn das kostet. Brian wohnt 42km entfernt. Monty weiß, dass er für jeden Kilometer 25 cent mit der Bahn zahlen muss. Zusätzlich benötigt er noch ungefähr 15 Euro um sich für die Reise ein Buch und eine Cola zu kaufen. Lege eine Variable mit dem Namen 'fahrpreis' an und berechne wieviel Monty's Hin- und Rückreise kostet. Wir nehmen an, dass Monty das Buch und die Cola nur einmal kauft. Dann lasse den Wert der Variable auf dem Bildschirm ausgeben. |2 min|
|Rechnen mit Modulo| Monty zahlt grundsätzlich nur mit 5 Euro scheinen und er will auch kein Wechselgeld, somit kann er die Reise nur antreten, wenn sich der Fahrpreis mit 5 Euro scheinen bezahlen lässt -- notfalls kauft er so viele Fahrten bis er bei einem Betrag ist, der sich mit 5Euro Scheinen zahlen lässt. Finde mittels einer Modulo Rechnung heraus, wie oft Brian mit dem Besuch von Monty rechnen kann.|3 min|

####Lösungsbeispiel
```
fahrpreis = (42 * 0.25) * 2 + 15 // == 
print(fahrpreis)
anzahl_besuche = fahrpreis % 5 // == 1 --> Monty muss 5 Fahrten buchen
```

##Unit 2
###Lektion 3 — Kommentare
####Einführung
Mit den Rechenoperationen hast du nun eigentlich schon das wichtigste gelernt. An dieser Stelle wollen wir uns einem anderen, auch sehr wichtigem Thema annehmen -- Kommentaren.
Manchmal kann es sehr nützlich sein, im Code Erklärungen hinzuzufügen, damit andere Leute verstehen, was der Code tut oder was sich der Programmierer dabei gedacht hat. Dieser Text soll natürlich bei der Ausführung des Programmes vom Computer ignoriert werden. Kommentare werden in Python mit dem Symbol `#` eingeleitet. Sofern dieses Symbol auftaucht, wird der restliche Text in dieser Zeile vom Computer ignoriert. Als Beispiel hierfür kannst du dir nochmal das obige Code Beispiel anschauen.
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
||  ||

###Lektion 4 — Listen
####Einführung
Mit Kommentaren selbst kannst du natürlich nichts programmieren, deswegen nehmen wir uns jetzt wieder einem sehr essentiellem Thema an, und zwar Listen.
Listen sind besondere Datenstrukturen. In ihnen können mehrere Werte gespeichert werden. Der Zugriff auf diese Werte erfolgt mit einem Index (die Stelle in der Liste,  an der der Wert gespeichert ist — beginnend bei 0). Eine Liste wird mit `[]` definiert:

```python
liste = [0, 1, 2, 3]
```

Möchte man nun beispielsweise das dritte Element der Liste ausgeben, so schreibt man
```python
print liste[2]
```
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
|Die Schüler lernen eine Liste anzulege und auszugeben|Monty hat nun seine Fahrkarten gekauft und muss jetzt seinen Koffer packen. Er will folgende Dinge mitnehmen: Eine Hose, ein Hemd, eine Jacke, Socken, Schuhe und natürlich seine Zahnbürste. Lege eine Variable mit dem Namen 'gepaeck' an und füge sämtliche Gegenstände hinzu. Lasse anschließend die Liste auf dem Bildschirm ausgeben|3 min|

####Lösungsbeispiel
```python
gepack = [Hose, Hemd, Jacke, Socken, Schuhe, Zahnbürste]
print(gepaeck)
```
###Lektion 5 — Funtkionen mit Listen
####Einführung
Hoffentlich hast du gemerkt, dass Listen an sich gar nicht schwer sind. Natürlich wäre es ziemlich sinnlos, wenn wir nur Listen anlegen, aber nichts mit ihnen tun könnten. Deswegen lernst du jetzt Möglichkeiten, wie du mit Listen coole Dinge machen kannst. Für die Manipulation von Listen haben wir folgende Möglichkeiten:

| Funktion| Ergebnis|
|---|---|
|liste.len | gibt die Länge der liste zurück |
|liste.del(index) | löscht den angegebenen Index aus der liste |
|liste.append(x)| fügt x an die Liste an (alternativ kann man auch `+` verwenden)|
|liste.extend([8,69])| fügt mehrere elemente an die Liste an|
|liste.remove(x)| entfernt x aus der liste|
|liste.index(x)| gibt den index von x in der liste zurück|
|liste.insert(index, x)| fügt x in die liste am gegebenen index ein|
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
|Die Schüler lernen die Länge einer Liste zu ermitteln|Mit erschrecken stellt Monty fest, dass seine Reisegesellschaft nur 5 Kilo Freigepäck erlaubt. Lege eine Variable mit dem Namen 'gewicht' an, die das Gewicht von Monty's Gepäck speichert. Er weiß, dass im Durchschnitt alle seine Sachen 400 Gramm wiegen.|2 min|
|Die Schüler lernen ein Element aus einer Liste zu löschen|Gerade hat Monty beim letzten Blick in den Wetterbericht festgestellt, dass es sonnig und warm wird und er somit seine Jacke nicht brauchen wird. Entferne die Jacke wieder aus seinem Gepäck|1 min|
|Die Schüler lernen Elemente zu einer Liste hinzuzufügen|Brian ruft Monty kurz vor der Abfahrt an und fragt ihn ob er denn Lust hätte mit ihm schwimmen zu gehen. Nun muss Monty noch seine Badehose, Badelatschen und seine Taucherbrille mitnehmen. Füge diese Dinge zu seinem Reisegepäck hinzu|2 min|
|Die Schüler lernen den Index eines Elements aus einer Liste herauszufinden|Unterwegs fragt sich Monty ob der denn auch an seine Socken gedacht hat. Lege eine Variable mit dem Namen 'socken' an, welche den Index des Elements 'Socken' aus der Gepäck-Liste speichert|2 min|

####Lösungsbeispiel
```python
gewicht = gepaeck.len * 400
gepaeck.remove('Jacke')
gepaeck.append('Badehose')
gepaeck.append('Badelatschen')
gepaeck.append('Taucherbrille')
socken = gepaeck.index('Socken')
```

##Unit 3
###Lektion 6 — Kontrollstrukturen (Verzweigung)
####Einführung
Herzlichen Glückwunsch - du hast nun schon ein ganz schönes Stück Arbeit hinter dir! Zeit für eine kleine Verschnaufpause. Trink einen Schluck und Streck dich einmal, dann gehts weiter mit dem spannenden Themenkomplex der Kontrollstrukturen. Was das genau ist erfährst du jetzt:
In einem Programm möchte man oftmals in Abhängigkeit von einer bestimmten Bedingung weiter verfahren. Wir könnten zum Beispiel ein Programm schreiben, welches einen Fahrkartenautomaten simuliert. Wenn ein Kunde eine Fahrkarte kauft, so müssen wir entscheiden ob (und wieviel) Wechselgeld er bekommt. Wenn der Wert des eingeworfenen Geldes genau mit dem Wert der Fahrkarte übereinstimmt, so bekommt er kein Wechselgeld, wenn zuviel eingeworfen wurde, dann ja. In Python können wir diesen Sachverhalt mit `if` und `else` abbilden:

```python
if geldeinwurf > fahrpreis:
	Rückgabe = fahrpreis - geldeinwurf
else:
	rueckgabe = 0
```

Nach dem wort `if` (‘wenn’) folgt immer eine Bedingung die ausgewertet wird. Ist diese wahr (`true`) so wird der code ausgeführt, der direkt im anschluss folgt. Ist die Bedingung falsch (`false`), so wird der Teil hinter dem wort `else` (‘sonst’) ausgeführt.
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
||  ||

####Lösungsbeispiel

###Lektion 7 — Kontrollstrukturen (Schleifen)
####Einführung
Verzweigungen waren gar nicht so schwer, oder?
Oftmals möchte man jedoch auch Code wiederholt ausführen — hierfür verwenden Programmierer sogenannte Schleifen (engl. ‘loops’).

Im vorherigen Kapitel haben wir schon das Konstrukt der Liste kennengelernt. Angenommen wir haben eine Liste mit ganzzahligen werten und möchten zu jedem Wert 1 addieren, dann sähe das wie folgt aus:

```python
liste = [0, 1, 2, 3]

for zahl in liste		
	zahl = zahl + 1
```
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
||  ||

####Lösungsbeispiel

##Unit 4
###Lektion 8 — Funktionen
####Einführung
Wow, du kannst Stolz auf dich sein, dass du schon bis hierhin gekommen bist. Nun folgt der letzte Teil unserer Reise, an dem es um Funktionen geht -- quasi die Masterclass beim programmieren lernen.
Mit Hilfe von Funktionen lässt sich der Quellcode eines Programms strukturieren und wiederverwenden. Angenommen wir schreiben ein Programm, welches an mehreren Stellen die Summe von Werten in einer Liste bilden muss. Der dazugehörige Code wäre folgender:
```python
summe = 0
for x in liste
	summe = summe + x
```

Beim programmieren sollte man darauf achten, möglichst wenig Code mehrfach zu schreiben. Die Berechnung der Summe der Zahlen soll deswegen in eine Funktion geschrieben werden, die man dann an den entsprechenenden Stellen aufrufen kann, und die das Ergebnis der Summe zurück gibt:
```
def listensumme(liste)
	summe = 0
	for x in liste
		summe = summe + x
	return summe
```
Die Funktion `listensumme` können wir nun an den Stellen aufrufen, wo sie gebraucht wird.
```python
liste = [0, 1, 2, 3]
summe = listensumme(liste)		# summe = 6
```
Eine Funktion besteht immer aus einer **Definition**, **Parametern**, welche an die Funktion übergeben werden und einem optionalem Rückgabewert.
In unserem obigen Beispiel ist die Definition ist der Code, aus welchem die Funktion besteht. Die Parameter befinden in den Klammern dahinter. In unserem Fall handelt es sich um eine Liste mit Werten. 
Der Rückgabewert befindet sich hinter dem `return` statement gekennzeichnet.
####Aufgaben
|Lernziel | Umsetzung | Zeitaufwand |
|---------|-----------|------------|
||  ||

####Lösungsbeispiel
