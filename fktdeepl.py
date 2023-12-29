import deepl, io, getopt, sys, locale, warnings
from pathlib import Path

###############################################################################

inputfile      = ""
outputfile     = ""
target_lang    = "DE"
current_locale = ""
sum_input      = 0
sum_output     = 0
even_odd       = None
dry_run        = False

warnings.simplefilter("ignore")

USAGE = "fktdeepl -i <inputfile> [-o <outputfile>] [-l <lang>][-d] [-c]"

#current_locale, cp = locale.getlocale(locale.LC_CTYPE)
current_locale, cp = locale.getdefaultlocale()
print("Locale: " + current_locale)

def is_locale(s):
  return current_locale.find(s) >= 0

#####################################################
# i18n section modeled with functions instead of gettext & Co.
#

def is_locale(s):
  return current_locale.find(s) >= 0


def infile_missing(): 
  if   is_locale("RU"): return u"Входной файл отсутствует"
  elif is_locale("DE"): return u"Eingabedatei fehlt"
  return                       u"Input file missing"
  
 
###############################################################################
# @brief Parses command line arguments and fills the global variables
# @param argv   Arguments from command line
#
def parse_opts(argv):
  global outputfile, inputfile, dry_run, even_odd, target_lang
  
  opts, args = getopt.getopt(argv,"dchi:o:l:")
  for opt, arg in opts:

    if opt == '-h':
      print (USAGE)
      sys.exit()
      
    elif opt == "-l":
      target_lang = arg
      
    elif opt == "-i":
      inputfile = arg
      
    elif opt == "-o":
      outputfile = arg
        
    elif opt == "-d":
      dry_run = True
        
    elif opt == "-c":
      even_odd = True
  
  if(len(inputfile)) == 0:
     print(infile_missing())
     sys.exit(1)
     
  if(len(outputfile)) == 0:
    outputfile = str(Path(inputfile).with_suffix(".html"))


###############################################################################
# @brief Writes header for translation table in HTML
# @param out    outputfile
#
def table_header(out):
  out.write("""
<html>
<head>
<style>

.none 
{
}

.separator 
{
  font-weight: bold;
  font-size: 130%;
  background-color: #FFFF00;
}

.even 
{
  background-color: #eeeeee;
}

.odd 
{
  background-color: #ffffff;
}

table 
{
  margin: 1em;
  border: solid 1pt;
  border-collapse: collapse;
  font-family: ubuntu, sans-serif;
}

table tr,
table th,
table td 
{
  margin: 1em;
  border: solid 1pt;
}

</style>
</head>
<body>

<table>
""")


###############################################################################
# @brief Writes footer for translation table in HTML
# @param out    outputfile
#
def table_footer(out):
  out.write("""</table>
  </body>
  </html>
""")


###############################################################################
# @brief Writes table row  with columns for origin and translation in HTML
# @param out     outputfile
# @param origin  origin in left column
# @param trans   translation in right column
#
def table_row(out, org, trans):
  global even_odd
  
  if even_odd is None:
      bg = 'none'
      
  else:  
    if even_odd:
      bg = 'even'
      
    else:
      bg = 'odd'

    even_odd = not even_odd
       
  out.write("  <tr>\n")
  out.write("   <td class='{0}'>\n".format(bg))
  out.write(org)
  out.write("</td>\n   <td class='{0}'>\n".format(bg))
  out.write(trans)
  out.write("</td>\n")
  out.write("  </tr>\n")


###############################################################################
# @brief Writes table separator later input of translators names in HTML
# @param out     outputfile
# @param title   title for document navigator
#
def table_separator(out, title):
  out.write("  <tr>\n")
  out.write("   <td class='separator'>\n")
  out.write("<h3>" + title + "</h3>")
  out.write("</td>\n   <td class='separator'>\n")
  out.write("EL: <br>SL: ")
  out.write("</td>\n")
  out.write("  </tr>\n")


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
def default_title(n):
  return "перевод {0}".format(n)


###############################################################################
# @brief Writes the current pair orig/translation to the target file
# @param output    Target file
# @param item      Origin which will be translated here on the fly 
def write_items(output, item):
  print (str(len(item)) + " => ",  end='', flush=True)
  
  result = translate(item)
  
  global sum_input, sum_output
  sum_input += len(item);
  sum_output += len(result);

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

output = io.open(outputfile, 'w', encoding='utf8')
#debug  = io.open("debugfile.txt", 'w', encoding='utf8')
auth_key = deepl_key()
translator = deepl.Translator(auth_key)

print(inputfile + " => " + outputfile)
table_header(output)



with open(inputfile,'r',encoding='utf8') as file:
  titleno = 1
  items = ""
   
  for line in file:
    item = cleanup(line)

    if len(item) != 0:

      if item.startswith('====='):
        if len(items) > 0: 
          write_items(output, items)
        items = ""
        
        title = item.lstrip('= ')
        if len(title) == 0:
          title = default_title(titleno)
  
        table_separator(output, title)
        titleno += 1
  
      elif item.startswith('-----'):
        if len(items) > 0: 
          write_items(output, items)
        items = ""
          
      else:
        items += "\n" + item

        if titleno == 1:
          table_separator(output, default_title(titleno))
          titleno += 1
          

table_footer(output)
if dry_run:
  print (str(sum_input) + " => (" + str(sum_output) + ")")
  
else:
  print (str(sum_input) + " => " + str(sum_output))


output.close()
