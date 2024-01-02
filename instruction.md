# Background

When translating larger documents in a team with translators and
proofreader, one possible application is uploading a text to Google Docs. The proofreader can then make suggestions for improvement in the
suggestions for improvement in the comments section and discuss everything with
with the translator.

To begin with, a table with two columns is created: the original is inserted on the left and the translation is created on the right. For a
the columns in the table are subdivided at appropriate
columns at sensible points and then obtain table cells that belong together
table cells, in which the original and translation are always next to each other, even if the texts are very different in length.

The first translation can be obtained by entering the left-hand table cell
into an online translator and then pasting the translation into
the right-hand cell.

As this procedure requires a relatively large amount of preparatory work before the
team can become active among themselves, it is advisable to use a tool
tool such as fktdeepl.

# fktdeepl

fktdeepl takes the file with the original text,
gets the translation from deepl.com and generates a file for
LibreOffice. This file can then be imported into Google Docs
and work online in a team.

Beforehand, you should prepare the original and insert meaningful separators
for the subsequent table rows. It can also be useful
be useful to insert special table rows with titles for important
sections. There is also a variant that inserts table rows for
for navigation and also provides space to enter the names of the sections later.

In the original document, use a simple editor (notepad.exe, gedit or similar) to insert lines that contain the following special
characters in the left margin:

- 5 Minus -----  
  Concludes a table row.
- 5 diamonds ##### [text]
  Creates a multi-column row and uses the text behind it as a
  text as a heading for the following rows.
- 5 equals ==== [text]
  Creates a coloured multi-column subdivision for entering the names
  the names of all participants. The optional text behind it 
  becomes the title and appears later in the navigation area.

Translated with DeepL.com (free version)