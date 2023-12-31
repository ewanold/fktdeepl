﻿###############################################################################
# @brief Generator for html file
#

html_linebreak                = "<br /><br />"

###############################################################################
# @brief Setuo for internal values of table generator in html
# @param title   document title
# @param date    creation date
# @param cols    table columns 2, 3
#
def table_setup_html(title, date, cols):
  return


###############################################################################
# @brief Writes header for translation table in HTML
# @param out    outputfile
# @param cls    number of columns 2, 3
#
def table_header_html(out, cols):
  out.write("""
<html>
<head>
<style>

.none
{
}

.translators
{
  font-weight: bold;
  font-size: 130%;
  background-color: #FFFF00;
}

.heading
{
  font-weight: bold;
  font-size: 130%;
  background-color: #ddddff;
  text-align: center;
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
# @param out       outputfile
# @param origin    origin in left column
# @param col3text  optional text for third column
# @param trans     translation in right column
#
def table_row_html(out, org, trans, _, even_odd):
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
# @brief Writes table separator for later input of translators names in HTML
# @param out     outputfile
# @param title   title for document navigator
#
def table_translators_html(out, title):
  out.write("  <tr>\n")
  out.write("   <td class='translators'>\n")
  out.write("<h3>" + title + "</h3>")
  out.write("</td>\n   <td class='translators'>\n")
  out.write("EL: <br>SL: ")
  out.write("</td>\n")
  out.write("  </tr>\n")


###############################################################################
# @brief Writes table separator to describe following content in html
# @param out     outputfile
# @param title   title for document navigator
#
def table_heading_html(out, title):
  out.write("  <tr>\n")
  out.write("   <td class='heading' colspan=2>\n")
  out.write(title)
  out.write("</td>\n")
  out.write("  </tr>\n")


###############################################################################
# @brief Writes an empty paragraph in HTML
# @param out     outputfile
#
def text_empty_para_html(out):
  out.write("  <p/>\n")


###############################################################################
# @brief returns linebreak in HTML
# @return  linebreak sequence
#
def text_linebreak_html():
  return "\n" + html_linebreak + html_linebreak + "\n"
