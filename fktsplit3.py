from pathlib  import Path
from fkti18n import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
    NONE   = 1
    LEFT   = 2
    CENTER = 3
    RIGHT  = 4
    END    = 5

USAGE = "fktsplit3 input left-tag center-tag right-tag"

if len(sys.argv) < 6:
  print(USAGE)
  sys.exit(1)

inputfile = sys.argv[1]
tagleft   = sys.argv[2]
tagcenter = sys.argv[3]
tagright  = sys.argv[4]
tagend    = sys.argv[5]

inpath     = Path(inputfile)
leftfile   = str(inpath.parent) + "\\" + inpath.stem + "-left"   + inpath.suffix
centerfile = str(inpath.parent) + "\\" + inpath.stem + "-center" + inpath.suffix
rightfile  = str(inpath.parent) + "\\" + inpath.stem + "-right"  + inpath.suffix

column    = Column.NONE
lineno    = 0
sumleft   = 0
sumcenter = 0
sumright  = 0

print(inputfile + " => " + leftfile + " + " + centerfile + " + " + rightfile)
print(inputfile + " => " + tagleft + " + " + tagcenter + " + " + tagright + " + " + tagend)

with open(inputfile, 'r', encoding='utf8') as infile:
  with open(leftfile, 'w', encoding='utf8') as outleft:
    with open(centerfile, 'w', encoding='utf8') as outcenter:
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

          elif item == tagcenter:
            if column != Column.LEFT:
              print(bad_state_for_center(lineno))
              sys.exit(1)

            column = Column.CENTER
            sumcenter += 1
            skip = True

          elif item == tagright:
            if column != Column.CENTER:
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
              outcenter.write("\n-----\n")
              outright.write("\n-----\n")
              print(inputfile + " => -----")

            if column == Column.LEFT:
              outleft.write(item + " ")
              print(inputfile + " => LEFT {0} {1}".format(lineno, len(item)))

            if column == Column.CENTER:
              outcenter.write(item + " ")
              print(inputfile + " => CENTER {0} {1}".format(lineno, len(item)))

            if column == Column.RIGHT:
               outright.write(item + " ")
               print(inputfile + " => RIGHT {0} {1}".format(lineno, len(item)))

if sumleft != sumright or sumleft != sumcenter:
  print(bad_column_sum())