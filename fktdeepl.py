from pathlib import Path
from htmlgen import *
from fodtgen import *
from fkti18n import *
from fktlib  import *

import deepl, io, getopt, sys, warnings, os
import easygui

###############################################################################

inputfile      = ""
outputfile     = ""
target_lang    = "DE"
file_type      = "fodt"
sum_input      = 0
sum_output     = 0
dry_run        = False
even_odd       = None
fktdeepl_key   = "" # "f5c84e42-f195-6b60-5f67-e13b97626693:fx"

warnings.simplefilter("ignore")

USAGE   = "fktdeepl -k <key> -i <in> [-o <out>] [-l <lang>] [-t <type>] [-d] [-c] [-2 <in2>] [-3 <in3>]"
VERSION = "0.4"

#####################################################
# @brief Shows grafical dialogs to enter needed data
#
def guiinput():
  global inputfile , outputfile
  
  inputfile = easygui.fileopenbox(msg=enter_inputfile(),
                                  title="fktdeepl",
                                  default='*',
                                  filetypes=[ ["*.txt", "TXT files"  ], ["*.*", "All files"] ],
                                  multiple=False)

  if inputfile == None:
    sys.exit(0)
    
  if(len(inputfile)) == 0:
    abort(infile_missing())

# more options to input

  if(len(outputfile)) == 0:
    if file_type == "html":
      outputfile = str(Path(inputfile).with_suffix(".html"))

    elif file_type == "fodt":
      outputfile = str(Path(inputfile).with_suffix(".fodt"))

  
###############################################################################
# @brief Parses command line arguments and Shows grafical dialogs to enter needed data
# @param argv   Arguments from command line
#
def parse_opts(argv):
  global outputfile, inputfile, dry_run, even_odd, target_lang, file_type, fktdeepl_key

  opts, args = getopt.getopt(argv,"dchi:o:l:t:")
  for opt, arg in opts:

    if opt == '-h':
      abort(USAGE)

    elif opt == "-l":
      target_lang = arg

    elif opt == "-k":
      fktdeepl_key = arg

    elif opt == "-t":
      file_type = arg

    elif opt == "-i":
      inputfile = arg

    elif opt == "-o":
      outputfile = arg

    elif opt == "-d":
      dry_run = True

    elif opt == "-c":
      even_odd = True

  if file_type not in ("html", "fodt"):
    abort(bad_filetype())

  if(len(inputfile)) == 0:
    abort(infile_missing())

  if(len(outputfile)) == 0:
    if file_type == "html":
      outputfile = str(Path(inputfile).with_suffix(".html"))
    elif file_type == "fodt":
      outputfile = str(Path(inputfile).with_suffix(".fodt"))


###############################################################################
# @brief Writes header for translation table
# @param out    outputfile
#
def table_header(out):
  if file_type == "html":   return table_header_html(out)
  elif file_type == "fodt": return table_header_fodt(out)


###############################################################################
# @brief Writes footer for translation table
# @param out    outputfile
#
def table_footer(out):
  if file_type == "html":   return table_footer_html(out)
  elif file_type == "fodt": return table_footer_fodt(out)


###############################################################################
# @brief Writes table row  with columns for origin and translation
# @param out     outputfile
# @param origin  origin in left column
# @param trans   translation in right column
#
def table_row(out, org, trans):
  global even_odd

  if even_odd is not None:
    even_odd = not even_odd

  if file_type == "html": return table_row_html(out, org, trans, even_odd)
  if file_type == "fodt": return table_row_fodt(out, org, trans, even_odd)


###############################################################################
# @brief Writes table separator for later input of translators names
# @param out     outputfile
# @param title   title for document navigator
#
def table_translators(out, title):
  if file_type == "html": return table_translators_html(out, title)
  if file_type == "fodt": return table_translators_fodt(out, title)


###############################################################################
# @brief Writes table separator to describe following content
# @param out     outputfile
# @param title   title for document navigator
#
def table_heading(out, title):
  if file_type == "html": return table_heading_html(out, title)
  if file_type == "fodt": return table_heading_fodt(out, title)


###############################################################################
# @brief Writes an empty paragraph
# @param out     outputfile
#
def text_empty_para(out):
  if file_type == "html": return text_empty_para_html(out)
  if file_type == "fodt": return text_empty_para_fodt(out)


###############################################################################
# @brief returns linebreak
# @return  linebreak sequence
#
def text_linebreak():
  if file_type == "html": return text_linebreak_html()
  if file_type == "fodt": return text_linebreak_fodt()


###############################################################################
# @brief Retrieves the api key for deepl from known sources
# @return api key
#
def deepl_key():
  global fktdeepl_key

  if len(fktdeepl_key) == 0:
    fktdeepl_key = os.environ.get('FKTDEEPL_KEY')

  return fktdeepl_key 


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

  return s


###############################################################################
# @brief Translates the current block or returns a test dummy
# @param item    original string
# @return translation from deepl
#
def translate(item):
  if dry_run:
    return lorem_ipsum(len(item))

  else:
    return translator.translate_text(item, target_lang=target_lang).text


###############################################################################
# @brief Generates the defualt tile for the navigator
# @param n   number of title (increasing 1 ..)
# @return title
#
def default_title(n):
  return "перевод {0}".format(n)


###############################################################################
# @brief Writes the current pair orig/translation to the target file
# @param output    Target file
# @param item      Origin which will be translated here on the fly
#
def write_items(output, item):
  logger(str(len(item)) + " => ",  end='', flush=True)

  result = translate(item)

  global sum_input, sum_output
  sum_input += len(item)
  sum_output += len(result)

  if dry_run:
    logger("(" + str(len(result)) + ")")

  else:
    logger(len(result))

  table_row(output, item, result)


#
#
#def debugpr(s):
#  logger(str(len(s)) + ' ' + s,  end=">\n", file=debug)

#debug  = io.open("debugfile.txt", 'w', encoding='utf8')

###############################################################################
# Main part

if len(sys.argv) > 1:
  parse_opts(sys.argv[1:])
else:  
  guiinput()

with io.open(outputfile, 'w', encoding='utf8') as output:
  auth_key = deepl_key()
  translator = deepl.Translator(auth_key)

  logger(inputfile + " => " + outputfile)
  table_header(output)

  with open(inputfile, 'r', encoding='utf8') as infile:
    titleno = 1
    items = ""

    newpara = True
    
    for line in infile:
      item = cleanup(line)

      if len(item) != 0:
        newpara = True

        if item.startswith('====='):
          if len(items) > 0:
            write_items(output, items)
          items = ""

          title = item.lstrip('= ')
          if len(title) == 0:
            title = default_title(titleno)

          table_translators(output, title)
          titleno += 1

        elif item.startswith('#####'):
          if len(items) > 0:
            write_items(output, items)
          items = ""

          title = item.lstrip('# ')
          table_heading(output, title)

        elif item.startswith('-----'):
          if len(items) > 0:
            write_items(output, items)
          items = ""

        else:
          items += "\n" + item

          if titleno == 1:
            table_translators(output, default_title(titleno))
            titleno += 1

      else:
          items += text_linebreak()

  if len(items) != 0:
    write_items(output, items)

  table_footer(output)

  if dry_run:
    logger(str(sum_input) + " => (" + str(sum_output) + ")")
  else:
    logger(str(sum_input) + " => " + str(sum_output))
