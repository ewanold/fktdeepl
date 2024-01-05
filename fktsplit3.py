###############################################################################
# @brief Extract 3 columns from exported ODT files to TXT format
#

from pathlib import Path
from fkti18n import *
from fktlib  import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
  NONE   = 1
  LEFT   = 2
  CENTER = 3
  RIGHT  = 4
  END    = 5

USAGE = "fktsplit3 input left-tag center-tag right-tag end-tag"

setup_locale()

if len(sys.argv) < 6:
  abort(USAGE)

inputfile = sys.argv[1]
tagleft   = sys.argv[2]
tagcenter = sys.argv[3]
tagright  = sys.argv[4]
tagend    = sys.argv[5]

inpath     = Path(inputfile)
leftfile   = str(Path(inputfile).with_name(inpath.stem + "-left"  + inpath.suffix))
centerfile = str(Path(inputfile).with_name(inpath.stem + "-center" + inpath.suffix))
rightfile  = str(Path(inputfile).with_name(inpath.stem + "-right" + inpath.suffix))

column    = Column.NONE
lineno    = 0
sumleft   = 0
sumcenter = 0
sumright  = 0

logger(inputfile + " => " + leftfile + " + " + centerfile + " + " + rightfile)
logger(inputfile + " => " + tagleft + " + " + tagcenter + " + " + tagright + " + " + tagend)

with open(inputfile, 'r', encoding='utf8') as infile:
  with open(leftfile, 'w', encoding='utf8') as outleft:
    with open(centerfile, 'w', encoding='utf8') as outcenter:
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
            # write_tag_rest(outxxxx, item, tagleft)
            skip = True

          elif item.find(tagcenter) >= 0:
            if column != Column.LEFT:
              abort(bad_state_for_center(lineno))

            column = Column.CENTER
            sumcenter += 1
            write_tag_rest(outleft, item, tagcenter)
            skip = True

          elif item.find(tagright) >= 0:
            if column != Column.CENTER:
              abort(bad_state_for_right(lineno))

            column = Column.RIGHT
            sumright += 1
            write_tag_rest(outcenter, item, tagright)
            skip = True

          elif item.find(tagend) >= 0:
            if column != Column.RIGHT:
              abort(bad_state_for_end(lineno))

            column = Column.END
            write_tag_rest(outright, item, tagend)
            skip = True
            outleft.write("\n-----\n")
            outcenter.write("\n-----\n")
            outright.write("\n-----\n")
            logger(inputfile + " => -----")

          ## Write line to correct file

          if not skip:
            if column == Column.LEFT:
              outleft.write(wrap_text(item + " "))
              logger(inputfile + " => LEFT {0} {1}".format(lineno, len(item)))

            if column == Column.CENTER:
              outcenter.write(wrap_text(item + " "))
              logger(inputfile + " => CENTER {0} {1}".format(lineno, len(item)))

            if column == Column.RIGHT:
               outright.write(wrap_text(item + " "))
               logger(inputfile + " => RIGHT {0} {1}".format(lineno, len(item)))

          else:
            if column == Column.LEFT:
              logger(inputfile + " => left tag {0}".format(lineno))

            if column == Column.CENTER:
              logger(inputfile + " => center tag {0}".format(lineno))

            if column == Column.RIGHT:
               logger(inputfile + " => right tag {0}".format(lineno))



if sumleft != sumright or sumleft != sumcenter:
  abort(bad_column_sum())