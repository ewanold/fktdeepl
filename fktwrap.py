###############################################################################
# @brief Wrap txt file to lines with max 80 characters.
#

import sys, os
from fktlib  import abort, wrap_text


USAGE = "fktwrap txt-file"


if len(sys.argv) < 2:
  abort(USAGE)

txtfile = sys.argv[1]

with open(txtfile, mode='r', encoding='utf8') as file:
  all_of_it = file.read()

bakfile = txtfile + ".bak"

if os.path.exists(bakfile):
  os.remove(bakfile)

os.rename(txtfile, bakfile)

with open(txtfile, mode='r', encoding='utf8') as file:
  lines = all_of_it.split("\n")
  for line in lines:
    file.write(wrap_text(line) + "\n")
