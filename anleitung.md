# Hintergrund

Beim Übersetzen größerer Dokumente in einem Team mit Übersetzer und
Korrekturleser ist eine mögliche Anwendung das Hochladen eines Textes nach Google Docs. Der Korrekturleser kann dann laufend im
Kommentarbereich Vorschläge zur Verbesserung machen und alles mit
dem Übersetzer diskutieren.

Zu Beginn wird dazu eine Tabelle mit zwei Spalten angelegt: links wird das Original eingefügt, rechts entsteht die Übersetzung. Zur
besseren Übersicht unterteilt man an die Tabellenspalten an
sinnvollen Stellen und erhält dann in sich zusammengehörende
Tabellenzellen, bei denen später Original und Übersetzung immer nebenenander liegen, selbst wenn sich die Texte in der Länge stark unterscheiden.

Die erste Übersetzung kann erhalten, indem man die linke Tabellenzelle
in einen Online-Übersetzer einfügt und die Übersetzung dann in
die rechte Zelle einfügt.

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
