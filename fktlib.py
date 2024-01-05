###############################################################################
# @brief Library functions
#

import sys, locale

current_locale  = ""
quiet_mode      = True

def set_verbose():
  global quiet_mode
  quiet_mode = False


def is_locale(s):
  return current_locale.find(s) >= 0


def setup_locale(): 
  #current_locale, cp = locale.getlocale(locale.LC_CTYPE)
  cl, cp = locale.getdefaultlocale()
  current_locale = cl
  logger("Locale: " + current_locale)


def logger(s, end='\n', flush=False):
  if not quiet_mode:
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



###############################################################################
# @brief Cleans the original from spaces, newlines, etc.
# @param out     outputfile
#
def cleanup(s):
  BOM_CODEPOINTS = [u'\uFFFE', u'\uFEFF']    # decoded BOMs, strip if in input[0] (py3.3+)

  if s[0:1] in BOM_CODEPOINTS:
    s = s[1:]

  s = s.strip()

  while s.find('  ') >= 0:
    s = s.replace('  ', ' ')

  while s.find(' \n') >= 0:
    s = s.replace(' \n', '\n')

  s = s.replace("<", "&lt;")
  s = s.replace("&", "&amp;")
  
  return s


def write_tag_rest(out, item, tag):
  s = item.replace(tag, " ").strip()
  if len(s) > 0:
    out.write(s)