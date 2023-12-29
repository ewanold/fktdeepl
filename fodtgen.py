
###############################################################################
# @brief Writes header for translation table in fodt
# @param out    outputfile
#
def table_header_fodt(out):
  out.write("""
""")


###############################################################################
# @brief Writes footer for translation table in fodt
# @param out    outputfile
#
def table_footer_fodt(out):
  out.write("""</table>
  </body>
  </fodt>
""")


###############################################################################
# @brief Writes table row  with columns for origin and translation in fodt
# @param out     outputfile
# @param origin  origin in left column
# @param trans   translation in right column
#
def table_row_fodt(out, org, trans, even_odd):
  if even_odd is None:
    bg = 'none'

  else:
    if even_odd:
      bg = 'even'

    else:
      bg = 'odd'

  out.write("  <tr>\n")


###############################################################################
# @brief Writes table separator later input of translators names in fodt
# @param out     outputfile
# @param title   title for document navigator
#
def table_separator_fodt(out, title):
  out.write("  <tr>\n")
