
###############################################################################
# @brief Writes header for translation table in HTML
# @param out    outputfile
#
def table_header_html(out):
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
def table_footer_html(out):
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
def table_row_html(out, org, trans, even_odd):
  if even_odd is None:
      bg = 'none'
      
  else:  
    if even_odd:
      bg = 'even'
      
    else:
      bg = 'odd'

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
def table_separator_html(out, title):
  out.write("  <tr>\n")
  out.write("   <td class='separator'>\n")
  out.write("<h3>" + title + "</h3>")
  out.write("</td>\n   <td class='separator'>\n")
  out.write("EL: <br>SL: ")
  out.write("</td>\n")
  out.write("  </tr>\n")


