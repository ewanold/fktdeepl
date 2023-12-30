from pathlib import Path
from htmlgen import *
from fodtgen import *
import deepl, io, getopt, sys, locale, warnings

###############################################################################

inputfile      = ""
outputfile     = ""
target_lang    = "DE"
file_type      = "html"
current_locale = ""
sum_input      = 0
sum_output     = 0
dry_run        = False
even_odd       = None

warnings.simplefilter("ignore")

USAGE = "fktdeepl -i <inputfile> [-o <outputfile>] [-l <lang>][-d] [-c]"

#current_locale, cp = locale.getlocale(locale.LC_CTYPE)
current_locale, cp = locale.getdefaultlocale()
print("Locale: " + current_locale)

#####################################################
# i18n section modeled with functions instead of gettext & Co.
#

def is_locale(s):
  return current_locale.find(s) >= 0


def infile_missing():
  if is_locale("RU"): return "Входной файл отсутствует"
  if is_locale("DE"): return "Eingabedatei fehlt"
  return                     "Input file missing"


def bad_filetype():
  if is_locale("RU"): return "Неправильный тип файла (html, fodt)"
  if is_locale("DE"): return "Falscher Dateityp (html, fodt)"
  return                     "Wrong file type (html, fodt)"


###############################################################################
# @brief Parses command line arguments and fills the global variables
# @param argv   Arguments from command line
#
def parse_opts(argv):
  global outputfile, inputfile, dry_run, even_odd, target_lang, file_type

  opts, args = getopt.getopt(argv,"dchi:o:l:t:")
  for opt, arg in opts:

    if opt == '-h':
      print (USAGE)
      sys.exit()

    elif opt == "-l":
      target_lang = arg

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
    print(bad_filetype())
    sys.exit(1)

  if(len(inputfile)) == 0:
    print(infile_missing())
    sys.exit(1)

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
  return "f5c84e42-f195-6b60-5f67-e13b97626693:fx"


###############################################################################
# @brief Cleans the original from spaces, newlines, etc.
# @param out     outputfile
#
def cleanup(s):
  s = s.strip()

  while s.find('  ') >= 0:
    s = s.replace('  ', ' ')

  while s.find(' \n') >= 0:
    s = s.replace(' \n', '\n')

  return s


###############################################################################
# @brief Translates the current block or returns origin as a test dummy
# @param item    original string
# @return translation from deepl
#
def translate(item):
  if dry_run:
    return item

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
  print (str(len(item)) + " => ",  end='', flush=True)

  result = translate(item)

  global sum_input, sum_output
  sum_input += len(item)
  sum_output += len(result)

  if dry_run:
    print ("(" + str(len(result)) + ")")

  else:
    print (len(result))

  table_row(output, item, result)


#
#
#def debugpr(s):
#  print(str(len(s)) + ' ' + s,  end=">\n", file=debug)


###############################################################################
# Main part

parse_opts(sys.argv[1:])

with io.open(outputfile, 'w', encoding='utf8') as output:
  #debug  = io.open("debugfile.txt", 'w', encoding='utf8')
  auth_key = deepl_key()
  translator = deepl.Translator(auth_key)

  print(inputfile + " => " + outputfile)
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
    print (str(sum_input) + " => (" + str(sum_output) + ")")
  else:
    print (str(sum_input) + " => " + str(sum_output))
