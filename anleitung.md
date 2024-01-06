# Hintergrund

Beim Übersetzen größerer Dokumente in einem Team mit Übersetzer und
Korrekturleser ist eine mögliche Anwendung das Hochladen eines Textes
nach Google Docs. Der Korrekturleser kann dann laufend im
Kommentarbereich Vorschläge zur Verbesserung machen und alles mit
dem Übersetzer diskutieren.

Zu Beginn wird dazu eine Tabelle mit zwei Spalten angelegt: links wird
das Original eingefügt, rechts entsteht die Übersetzung. Zur
besseren Übersicht unterteilt man an die Tabellenspalten an
sinnvollen Stellen und erhält dann in sich zusammengehörende
Tabellenzellen, bei denen später Original und Übersetzung immer nebenenander
liegen, selbst wenn sich die Texte in der Länge stark unterscheiden.

Die erste Übersetzung kann man einfach erhalten, indem man die linke
Tabellenzelle in einen Online-Übersetzer einfügt und die Übersetzung
dann in die rechte Zelle einfügt.

Da diese Vorgehensweise relativ viel Vorarbeit erfordert, bis das
Team untereinander aktiv werden kann, bietet sich die Anwendung eines
Tools wie fktdeepl an.

# fktdeepl

fktdeepl nimmt die Datei mit dem originalen Text,
holt sich die Übersetzung von deepl.com und erzeugt eine Datei für
LibreOffice. Diese Datei kann man dann in Google Docs importieren
und online im Team arbeiten.

Zuvor sollte man das Orignal aufbereiten und sinnvolle Trennstellen
für die späteren Tabellenzeilen einfügen. Weiterhin kann es sinnvoll
sein, besondere Tabellenzeilen mit Titel für wichtige Abschnitte
einzufügen. Ausserdem gibt es eine Variante, die Tabellenzeilen für
die Navigation einfügt und auch Platz zum späteren Eintragen der Namen
bereitstellt.

Im Originaldokument fügt man mit einem einfachen Editor (notepad.exe,
gedit oder ähnlich) Zeilen ein, die am linken Rand folgende besondere
Zeichen enthalten:

- 5 Minus -----  
  Schliesst eine Tabellenreihe ab.
- 5 Rauten #####  [text]  
  Erzeugt eine mehrspaltige Reihe und nimmt den dahinter stehenden
  Text als Überschrift für die folgenden Zeilen.
- 5 Gleich ==== [text]  
  Erzeugen eine farbige mehrspaltige Unterteilung zum Eintragen
  der Namen aller beteiligten. Der optinal dahinter stehende Text
  wird als Titel und erscheint später im Navigationsbereich.

Im einfachsten Fall erzeugt man dann mit folgendem Aufruf eine mit Deepl übersetzte FODT-Datei nach Deutsch:

```bash
fktdeepl  textfile.txt  -k <key>
```

# fktwrap

Wenn man übliche Office-Dokumente in das TXT-Format exportiert, erhält man
typischerweise sehr lange Textzeilen. Das Einfügen der obigen Zeilenmarkierung ist
dann mühsam. fktwrap bricht überlange Zeilen auf ca. 80 Zeichen je Zeile durch.

Aufruf:

```bash
fktwrap  txt-file.txt
```

# fktsplit2

Wenn man bestehende 2-spaltig übersetzte Dokumente in gleich aufgeteilte
Dokumente für die Übersetzung in eine andere Sprache erzeugen will, kann man
mit fktsplit2 die exportierte TXT-Datei in 2 Dateien für die 2 enthaltenen
Tabellenspalten auftrennen.

Damit der Export und die Auftrennung funktioniert, muss man 3 weitere Spalten
vor und nach den eigentlichen Textspalten im
ursprünglichen Dokument einfügen und jede der neuen Zellen mit Kennungen füllen.
Das Einfügen von Tabellenspalten ist über entsprechende Funktionen der Textverarbeitung
einfach.

Dann markiert man die komplette linke neue Spalte und fügt eindeutige und sonst nirgends
vorhandene Textsequenzen wie z.B. '####links####' ein.
Mit der mittleren neuen Spalte verfährt man gleich und fügt z.B. '####rechts####' ein,
in die rechte neue Spalte fügt man z.B. '####ende####' ein.

Das aufbereitete Dokument exportiert man als TXT-Datei und ruft folgendes Kommando auf:

```bash
fktsplit2  file.txt   "####links####"  "####rechts####"  "####ende####"
```

# fktsplit3

fktsplit3 dient zum Auftrennen von 3-spaltigen Übersetzungsdokumenten wenn z.B. eine
zusätzliche Spalten für Übersetzungsreferenzen verwendet wird.

Man verfährt wie bei fktsplit2, fügt aber eine weitere Hilfsspalte ein und füllt diese
mit einer weiteren eindeutigen Markierung.

```bash
fktsplit3  file.txt   "####links####"  "####mitte####"  "####rechts####"  "####ende####"
```
