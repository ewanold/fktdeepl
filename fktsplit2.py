###############################################################################
# @brief Extract 2 columns from exported ODT files to TXT format
#

from pathlib import Path
from fkti18n import *
from fktlib  import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
    NONE  = 1
    LEFT  = 2
    RIGHT = 3
    END   = 4

USAGE = "fktsplit2 input left-tag center-tag right-tag"

#set_verbose()

setup_locale()

if len(sys.argv) < 5:
  abort(USAGE)

inputfile = sys.argv[1]
tagleft   = sys.argv[2]
tagright  = sys.argv[3]
tagend    = sys.argv[4]

inpath    = Path(inputfile) / ""
leftfile  = str(Path(inputfile).with_name(inpath.stem + "-left"  + inpath.suffix))
rightfile = str(Path(inputfile).with_name(inpath.stem + "-right" + inpath.suffix))

column   = Column.NONE
lineno   = 0
sumleft  = 0
sumright = 0

logger(inputfile + " => " + leftfile + " + " + rightfile)

with open(inputfile, 'r', encoding='utf8') as infile:
  with open(leftfile, 'w', encoding='utf8') as outleft:
    with open(rightfile, 'w', encoding='utf8') as outright:

      for line in infile:
        lineno += 1
        item = line.strip()

        ## Check statemachine

        skip = False

        if item.find(tagleft) >= 0:
          if column != Column.NONE and column != Column.END:
            abort(bad_state_for_left(lineno))

          column = Column.LEFT
          sumleft += 1
          # write_tag_rest(outxxx, item, tagend)
          skip = True

        elif item.find(tagright) >= 0:
          if column != Column.LEFT:
            abort(bad_state_for_right(lineno))

          column = Column.RIGHT
          sumright += 1
          write_tag_rest(outleft, item, tagright)
          skip = True

        elif item.find(tagend) >= 0:
          if column != Column.RIGHT:
            abort(bad_state_for_end(lineno))

          column = Column.END
          write_tag_rest(outright, item, tagend)
          skip = True
          outleft.write("\n-----\n")
          outright.write("\n-----\n")
          logger(inputfile + " => -----")

        ## Write line to correct file

        if not skip:
          if column == Column.LEFT:
            outleft.write(item + "  ")
            logger(inputfile + " => LEFT {0} {1}".format(lineno, len(item)))

          if column == Column.RIGHT:
            outright.write(item + " ")
            logger(inputfile + " => RIGHT {0} {1}".format(lineno, len(item)))

        else:
          if column == Column.LEFT:
            logger(inputfile + " => left switch {0}".format(lineno))

          if column == Column.RIGHT:
            logger(inputfile + " => right switch {0}".format(lineno))
          

if sumleft != sumright:
  abort(bad_column_sum())
