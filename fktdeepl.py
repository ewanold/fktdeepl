###############################################################################
# @brief fktdeepl generates templates for translator teams
#

import getopt, sys, warnings, os, time

from datetime import datetime
from pathlib  import Path
from htmlgen  import *
from fodtgen  import *
from fkti18n  import *
from fktlib   import *

import deepl, easygui

###############################################################################

inputfile        = ""
outputfile       = ""
input2file       = ""
input3file       = ""
in2file          = None
in3file          = None
columns          = 2
target_lang      = "DE"
file_type        = "fodt"
sum_input        = 0
sum_output       = 0
dry_run          = False
even_odd         = True
fktdeepl_key     = "" # "f5c84e42-f195-6b60-5f67-e13b97626693:fx"
doc_title        = ""
col2_empty       = False
col3_empty       = False
deepl_translator = None

warnings.simplefilter("ignore")

USAGE   = "fktdeepl -k <key> -i <in> [-o <out>] [-l <lang>] [-t <type>] [-d] [-c] [-2 <in2>] [-3 <in3>]"
VERSION = "0.5"

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
  global outputfile, inputfile, input2file, input3file, dry_run, even_odd
  global target_lang, file_type, fktdeepl_key, columns, doc_title, col2_empty, col3_empty

  opts, args = getopt.getopt(argv,"vdchi:o:l:f:t:2:3:k:")
  for opt, arg in opts:

    if opt == '-h':
      abort(USAGE)

    elif opt == "-l":
      target_lang = arg

    elif opt == "-v":
      set_verbose()

    elif opt == "-k":
      fktdeepl_key = arg

    elif opt == "-f":
      file_type = arg

    elif opt == "-t":
      doc_title = arg

    elif opt == "-i":
      inputfile = arg

    elif opt == "-o":
      outputfile = arg

    elif opt == "-d":
      dry_run = True

    elif opt == "-c":
      even_odd = None

    elif opt == "-2":
      if arg != "-":
        input2file = arg

      else:
        col2_empty = True

    elif opt == "-3":
      if arg != "-":
        input3file = arg

      else:
        col3_empty = True

      columns = 3

  if file_type not in ("html", "fodt"):
    abort(bad_filetype())

  if(len(inputfile)) == 0:
    abort(infile_missing())

  if(len(outputfile)) == 0:
    if file_type == "html":
      outputfile = str(Path(inputfile).with_suffix(".html"))

    elif file_type == "fodt":
      outputfile = str(Path(inputfile).with_suffix(".fodt"))

  if len(doc_title) == 0:
    doc_title = inputfile


###############################################################################
# @brief Setuo for internal values of table generator
# @param title   document title
# @param date    creation date
# @param cols    table columns 2, 3
#
def table_setup(title, date, cols):
  if file_type == "html": table_setup_html(title, date, cols)
  if file_type == "fodt": table_setup_fodt(title, date, cols)


###############################################################################
# @brief Writes header for translation table
# @param out    outputfile
#
def table_header(out):
  if file_type == "html": table_header_html(out, columns)
  if file_type == "fodt": table_header_fodt(out, columns)


###############################################################################
# @brief Writes footer for translation table
# @param out    outputfile
#
def table_footer(out):
  if file_type == "html": table_footer_html(out)
  if file_type == "fodt": table_footer_fodt(out)


###############################################################################
# @brief Writes table row  with columns for origin and translation
# @param out     outputfile
# @param origin  origin in left column
# @param trans   translation in right column
#
def table_row(out, org, trans, col3text):
  global even_odd

  if even_odd is not None:
    even_odd = not even_odd

  if file_type == "html": return table_row_html(out, org, trans, col3text, even_odd)
  if file_type == "fodt": return table_row_fodt(out, org, trans, col3text, even_odd)


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
# @brief Gets the text for column 2. Either the translation or a
# line from file 2
# @param item    original string
# @param item2   collected lines of optional file 2
# @return translation from deepl or file 2
#
def col2text(item, items2):
  logger(str(len(item)) + " => ",  end='', flush=True)

  if col2_empty:
    result = ""

  elif in2file != None:
    result = items2

  elif dry_run:
    result = lorem_ipsum(len(item))

  else:
    result = deepl_translator.translate_text(item, target_lang=target_lang).text

  if dry_run or col2_empty:
    logger("(" + str(len(result)) + ")")

  else:
    logger(len(result))

  return result

###############################################################################
# @brief Gets the text for column 3 from file 3
# @return empty string or file 3
#
def col3line():
  if col3_empty:
    return ""

  if in3file != None:
    return cleanup(in3file.readline())

  return ""

###############################################################################
# @brief Gets the text for column 2 from file 2
# @return empty string or file 2
#
def col2line():
  if col2_empty:
    return ""

  if in2file != None:
    return cleanup(in2file.readline())

  return ""


###############################################################################
# @brief Generates the defualt tile for the navigator
# @param n   number of title (increasing 1 ..)
# @return title
#
def default_title(n):
  return text_section(n)


###############################################################################
# @brief Writes the current pair orig/translation to the target file
# @param output    Target file
# @param item      Origin which will be translated here on the fly
#
def write_items(output, item, result, col3text):
  global sum_input, sum_output, columns

  sum_input += len(item)
  sum_output += len(result)

  table_row(output, wrap_text(item), wrap_text(result), wrap_text(col3text))


###############################################################################
# Main part

#set_verbose()

setup_locale()

if len(sys.argv) > 1:
  parse_opts(sys.argv[1:])

else:
  guiinput()

if len(input2file) != 0:
  in2file = open(input2file, 'r', encoding='utf8')

if len(input3file) != 0:
  in3file = open(input3file, 'r', encoding='utf8')

with open(outputfile, 'w', encoding='utf8') as output:
  auth_key = deepl_key()
  if not dry_run and not col2_empty:
    if not auth_key or len(auth_key) == 0:
      abort(no_authkey())
    deepl_translator = deepl.Translator(auth_key)

  logger(inputfile + " => " + outputfile)
  starttime = time.time()
  table_setup(doc_title, datetime.now().strftime("%Y-%m-%d %H:%M"), columns)
  table_header(output)

  titleno = 1
  items1 = ""
  items2 = ""
  items3 = ""
  cells  = 0

  with open(inputfile, 'r', encoding='utf8') as infile:

    newpara = True

    for line in infile:
      item1 = cleanup(line)
      item2 = col2line()
      item3 = col3line()

      if len(item1) != 0:
        newpara = True

        if item1.startswith('====='):
          if len(items1) > 0:
            write_items(output, items1, col2text(items1, items2), items3)
          items1 = ""
          items2 = ""
          items3 = ""
          cells += 1

          title = item1.lstrip('= ')
          if len(title) == 0:
            title = default_title(titleno)

          table_translators(output, title)
          titleno += 1

        elif item1.startswith('#####'):
          if len(items1) > 0:
            write_items(output, items1, col2text(items1, items2), items3)
          items1 = ""
          items2 = ""
          items3 = ""
          cells += 1

          title = item1.lstrip('# ')
          table_heading(output, title)

        elif item1.startswith('-----'):
          if len(items1) > 0:
            write_items(output, items1, col2text(items1, items2), items3)
          items1 = ""
          items2 = ""
          items3 = ""
          cells += 1

        else:
          items1 += "\n" + item1
          items2 += "\n" + item2
          items3 += "\n" + item3

          if titleno == 1:
            table_translators(output, default_title(titleno))
            titleno += 1

      else:
        items1 += text_linebreak()
        items2 += text_linebreak()
        items3 += text_linebreak()

  if len(items1) != 0:
    write_items(output, items1, col2text(items1, items2), items3)
    items1 = ""
    items2 = ""
    items3 = ""

  table_footer(output)

  if dry_run or col2_empty:
    logger(str(sum_input) + " => (" + str(sum_output) + ")")
  else:
    logger(str(sum_input) + " => " + str(sum_output))

  endtime = time.time()
  logger (text_statistic(cells, endtime - starttime))
