import deepl, io

inputfile   = "testfile2.txt"
outputfile  = "testfile2.html"
target_lang = "DE"

even_odd = False  # True/None
dry_run  = False

#####################################################

#
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
  font-size: 150%;
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
  display: inline-table;
  margin: 1em;
  border: solid 1px;
  border-collapse: collapse;
  font-family: ubuntu, sans-serif;
}

table th,
table td 
{
  border: solid 1px;
}

</style>
</head>
<body>

<table>
""")

#
#
def table_footer(out):
  out.write("""</table>
  </body>
  </html>
""")

#
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
       
  out.write("  <tr class='{0}'>\n".format(bg))
  out.write("   <td>")
  out.write(org)
  out.write("</td>\n   <td>")
  out.write(trans)
  out.write("</td>\n")
  out.write("  </tr>\n")


def table_separator(out, title):
  out.write("  <tr class='separator'>\n")
  out.write("   <td>")
  out.write(title)
  out.write("</td>\n   <td>")
  out.write("EL: <br>SL: ")
  out.write("</td>\n")
  out.write("  </tr>\n")

#####################################################

output = io.open(outputfile, 'w', encoding='utf8')
debug  = io.open("debugfile.txt", 'w', encoding='utf8')

def deepl_key():
  return "f5c84e42-f195-6b60-5f67-e13b97626693:fx"
  
auth_key = deepl_key()
translator = deepl.Translator(auth_key)

#
#
def cleanup(s):
  s = s.strip()
  
  while s.find('  ') >= 0:
    s = s.replace('  ', ' ')

  while s.find(' \n') >= 0:
    s = s.replace(' \n', '\n') 
    
  return s

#
#
def translate(item):
  if dry_run:
    return item
  else:  
    return translator.translate_text(item, target_lang=target_lang).text

#
#
def default_title(n):
  return "перевод {0}".format(n)

#
#
def write_items(output, item):
  print (str(len(item)) + " => ",  end='', flush=True)
  
  result = translate(item)
  
  if dry_run:
    print ("(" + str(len(result)) + ")")
    
  else:
    print (len(result))
  
  table_row(output, item, result)  


#
#
def debugpr(s):
  print(str(len(s)) + ' ' + s,  end=">\n", file=debug)


###############################################################################
 
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

output.close()
