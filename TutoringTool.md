#Ein universelles tutorial tool


[TOC]

Alternative Idee für das Praktikum IT-basiertes Lernen gestalten

## Idee
Mit Hilfe eines Datei-Inputs lassen sich Tutorien voll automatisch erstellen.
Folgendes Szenario: Die Schüler sollen Beispielsweise was über einen bestimmten Algorithmus lernen (z.B. Quicksort) Man schreibt hierfür ein Tutorial in einer Textdatei, welches über ein Webinterface in die Anwendung gebracht wird. Das Programm parst den Input und erstellt ein Interaktives Tutorial (oder Quiz mit Antwortmöglichkeiten zu fragen), welches dann von den Schülern bearbeitet werden kann (quasi generisches it-basiertes lernen)

## Mögliche Features
- Einmal erstellte Tutorien werden in einer Datenbank gespeichert und für die Nachwelt konserviert
- "Belohnungssystem" in form von virtuellen Badges geben (wie es sie auch beispielsweise auf Codeschool gibt, wenn man erfolgreich einen Kurs erstellt hat)
- Competitiver Charackter (man kann sehen wer wie viele Punkte erreicht hat => internes Ranking)
- Bewertung von Tutorials und somit Rückmeldung an Lehrer ob es was zu verbessern gibt
- Bilder/Videos können mit Hilfe von Weblinks eingebettet werden (oder man kann ein zip archiv hochladen, wo die Bilder mit drin sind -- wäre aber wahrscheinlich eher was für später)
- ...

## Vorteile (ggü eines Lernspiels)
- es ist modular aufgebaut
- es wäre viel einfacher die Aufgaben zu verteilen (z.B. einer schreibt Doku, einer implementiert das Web Interface und zwei schreiben den Parser)
- das Projekt könnte nach diesem Semester von anderen Gruppen erweitert werden (zum Beispiel durch einen browser editor, Fortschrittsanzeige für Teilnehmer, statistiken (wer hat wie viele Punkte wo erreicht)
- es gibt keinen unnötigen zusätzlichen Code den man erklären müsste (oder wo man sogar keine Zeit hat und den am ende eh keiner Versteht (der Quellcode vom Spiel wird wahrscheinlich eher umfangreich))
- keine komplizierten Grafiken notwendig
- Meilensteine wären relativ einfach festzulegen
	- Datenformat erstellt
	- Webschnittstelle Online
	- Parser läuft
	- Datenbank ready
	- ...
- wir bräuchten wesentlich (!) weniger externe Komponenten die sich vielleicht gegenseitig im Weg stehen (kein Pygame, kein Blender)
- die Rechnerausstattung an der Schule/Uni ist egal, da alles im web gehostet und im Browser läuft ([Heroku](https://devcenter.heroku.com/articles/getting-started-with-django) hostet kostenlos)

## Ideen zur technischen Umsetzung
- Webinterface: Django Framework (ein MVC auf Python basis) realisieren
- Backend: pures Python
- Datenbank: Sqlite3, MongoDB (kenne mich aber mit NoSql nicht aus)
- Für einen Parser gibt es möglicherweise Python Bibliotheken

## Noch zu klären
- Dateiformat konkretisieren (Markdown?  (gibt wahrscheinlich etliche Konverter nach Pdf oder Html gibt, um das ganze schön anzeigen lassen zu können))
- Was würden wir in der Unterrichtsstunde machen? (Hier sehe ich aktuell zwei Möglichkeiten -- entweder wir erstellen selbst ein Tutorial zu einem Thema aus dem Lehrplan oder wir zeigen ihnen wie sie selbst Tutorials erstellen können)


> Written with [StackEdit](https://stackedit.io/).