from pathlib  import Path
from fkti18n import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
    LEFT  = 1
    RIGHT = 2
    NONE  = 3

USAGE = "fktsplit2 input left-tag right-tag"

if len(sys.argv) < 5:
  print USAGE
  sys.exit(1)

inputfile = sys.argv[1]
tagleft   = sys.argv[2]
tagright = sys.argv[3]
tagend  = sys.argv[4]

inpath = Path(inputfile)
leftfile  = inpath.parent + inpath.stem + "-left"  + inpath.suffix
rightfile = inpath.parent + inpath.stem + "-right" + inpath.suffix

column = Column.NONE
lineno = 0
sumleft = 0
sumright = 0

print(inputfile + " => " + leftfile + " + " + rightfile)

with open(inputfile, 'r', encoding='utf8') as infile:
  with open(leftfile, 'w', encoding='utf8') as outleft:
    with open(rightfile, 'w', encoding='utf8') as outright:

    for line in infile:
      lineno += 1
      item = line.strip()

      if item = tagleft:
        if column != Column.None:
          print(bad_state_for_left(lineno)
          sys.exit(1)

        column = Column.LEFT

      elif item = tagright
        if column != Column.LEFT:
          print(bad_state_for_right(lineno)
          sys.exit(1)

        column = Column.RIGHT

      elif item = tagend
        if column != Column.RIGHT:
          print(bad_state_for_end(lineno)
          sys.exit(1)

        column = Column.NONE

      if column = Column.LEFT
        outleft.write(item)
        print(inputfile + " => LEFT " + len(item))
        sumright += 1

      if column = Column.RIGHT
        outright.write(item)
        print(inputfile + " => RIGHT " + len(item))
        sumright += 1
