from pathlib  import Path
from fkti18n import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
    NONE  = 1
    LEFT  = 2
    RIGHT = 3
    END   = 4

USAGE = "fktsplit2 input left-tag right-tag"

if len(sys.argv) < 5:
  print(USAGE)
  sys.exit(1)

inputfile = sys.argv[1]
tagleft   = sys.argv[2]
tagright = sys.argv[3]
tagend  = sys.argv[4]

inpath = Path(inputfile) / ""
leftfile  = str(inpath.parent) + "\\" + inpath.stem + "-left"  + inpath.suffix
rightfile = str(inpath.parent) + "\\" + inpath.stem + "-right" + inpath.suffix

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

        ## Check statemachine

        skip = False

        if item == tagleft:
          if column != Column.NONE and column != Column.END:
            print(bad_state_for_left(lineno))
            sys.exit(1)

          column = Column.LEFT
          sumleft += 1
          skip = True

        elif item == tagright:
          if column != Column.LEFT:
            print(bad_state_for_right(lineno))
            sys.exit(1)

          column = Column.RIGHT
          sumright += 1
          skip = True

        elif item == tagend:
          if column != Column.RIGHT:
            print(bad_state_for_end(lineno))
            sys.exit(1)

          column = Column.END
          skip = True

        ## Write line to correct file

        if not skip:
          if column == Column.END:
            outleft.write("\n-----\n")
            outright.write("\n-----\n")
            print(inputfile + " => -----")

          if column == Column.LEFT:
            outleft.write(item + "  ")
            print(inputfile + " => LEFT {0} {1}".format(lineno, len(item)))

          if column == Column.RIGHT:
            outright.write(item + " ")
            print(inputfile + " => RIGHT {0} {1}".format(lineno, len(item)))

if sumleft != sumright:
  print(bad_column_sum())
