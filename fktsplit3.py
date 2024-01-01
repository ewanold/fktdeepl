from pathlib  import Path
from fkti18n import *

import io, getopt, sys, warnings

from enum import Enum

# class syntax

class Column(Enum):
    LEFT   = 1
    CENTER = 2
    RIGHT  = 3
    NONE   = 4
    
USAGE = "fktsplit3 input left-tag center-tag right-tag"

if len(sys.argv) < 6
  print USAGE 
  sys.exit(1)

inputfile = sys.argv[1]  
tagleft   = sys.argv[2]    
tagcenter = sys.argv[3]  
tagright  = sys.argv[4]  
tagend    = sys.argv[5] 

inpath     = Path(inputfile)
leftfile   = inpath.parent + inpath.stem + "-left"   + inpath.suffix
centerfile = inpath.parent + inpath.stem + "-center" + inpath.suffix
rightfile  = inpath.parent + inpath.stem + "-right"  + inpath.suffix

column    = Column.NONE
lineno    = 0
sumleft   = 0
sumcenter = 0
sumright  = 0

print(inputfile + " => " + leftfile + " + " + centerfile + " + " + rightfile)

with open(inputfile, 'r', encoding='utf8') as infile:
  with open(leftfile, 'w', encoding='utf8') as outleft:
    with open(centerfile, 'w', encoding='utf8') as outcenter:
      with open(rightfile, 'w', encoding='utf8') as outright:

     for line in infile:
       lineno += 1
       item = line.strip()
   
       if item = tagleft:
         if column != Column.NONE:
           print(bad_state_for_left(lineno)
           sys.exit(1)
        
         column = Column.LEFT
           
       if item = tagcenter:
         if column != Column.LEFT:
           print(bad_state_for_center(lineno)
           sys.exit(1)
        
         column = Column.CENTER
           
       elif item = tagright
         if column != Column.CENTER:
           print(bad_state_for_right(lineno)
           sys.exit(1)
        
         column = Column.RIGHT
 
       elif item = tagend
         if column != Column.RIGHT:
           print(bad_state_for_right(lineno)
           sys.exit(1)
        
         column = Column.NONE
         
       if column = Column.LEFT
         outleft.write(item)       
         print(inputfile + " => LEFT " + len(item))
         sumright += 1
  
       if column = Column.CENTER
         outcenter.write(item)       
         print(inputfile + " => CENTER " + len(item))
         sumcenter += 1

      if column = Column.RIGHT
         outright.write(item)       
         print(inputfile + " => RIGHT " + len(item))
         sumright += 1
         
 