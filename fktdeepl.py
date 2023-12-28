import deepl,io

inputfile = "testfile1.txt"
outputfile = "testfile1.html"

columns = 2
target_lang="DE"

even_odd = True  # True/None
dry_run = True

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
def table_row(out, org, trans, cls):
  out.write("  <tr class='{0}'>\n".format(cls))
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
  out.write("EL: ")
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
def debugpr(s):
  print(str(len(s)) + ' ' + s,  end=">\n", file=debug)
 
table_header(output)
table_separator(output, "перевод {0}".format(1));
title = 2

with open(inputfile,'r',encoding='utf8') as file:
  for line in file:
    item = cleanup(line)
    
    if even_odd is None:
      bg = 'none'
      
    else:  
      if even_odd:
        bg = 'even'
     
      else:
        bg = 'odd'
      even_odd = not even_odd
       
    if len(item) != 0:
      print (str(len(item)) + " => ",  end='', flush=True)
      result = translate(item)

      if dry_run:
        print ("(" + str(len(result)) + ")")
      else:
        print (len(result))

      table_row(output, item, result, bg)  

table_footer(output)

output.close()
