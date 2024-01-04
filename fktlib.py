###############################################################################
# @brief Library functions
#

import io, sys

def logger(s, end='\n', flush=False):
  print(s, end=end, flush=flush)


def abort(s):
  print(s)
  sys.exit(1)


def lorem_ipsum(n):
  lorem = """
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut 
labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo 
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor 
sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et 
justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy 
eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos 
et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus 
est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel 
llum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui 
blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem 
ipsum dolor sit amet.
"""

  li = lorem
  while n > len(li):
    li += lorem

  return li[0:n]


