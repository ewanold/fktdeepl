cell_counter = 1

###############################################################################
# @brief Writes header for translation table in fodt
# @param out    outputfile
#
def table_header_fodt(out):
  out.write("""<?xml version="1.0" encoding="UTF-8"?>

<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:officeooo="http://openoffice.org/2009/office" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.text">
 <office:meta>
   <meta:creation-date>2023-12-29T15:49:57.123000000</meta:creation-date>
   <meta:generator>fktdeepl</meta:generator>
  </office:meta>
 <office:automatic-styles>
  
  <style:style style:name="table_fkt" style:family="table">
   <style:table-properties style:width="19cm" fo:margin-left="-1cm" fo:margin-top="0cm" fo:margin-bottom="0cm" fo:break-before="auto" fo:break-after="auto" table:align="left" style:writing-mode="lr-tb"/>
  </style:style>
  
  <style:style style:name="table_counter_column" style:family="table-column">
   <style:table-column-properties style:column-width="1cm"/>
  </style:style>
  
  <style:style style:name="table_left_column" style:family="table-column">
   <style:table-column-properties style:column-width="9,5cm"/>
  </style:style>
  
  <style:style style:name="table_right_column" style:family="table-column">
   <style:table-column-properties style:column-width="9,5cm"/>
  </style:style>
  
  <style:style style:name="translators_row" style:family="table-row">
   <style:table-row-properties fo:keep-together="auto"/>
  </style:style>
  
  <style:style style:name="translators_counter_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color="#e6b8af" fo:padding="0.176cm" fo:border="1pt solid #000000" />
  </style:style>
  
  <style:style style:name="translators_left_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color="#e6b8af" fo:padding="0.176cm" fo:border="1pt solid #000000" />
  </style:style>
  
  <style:style style:name="translators_right_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color="#e6b8af" fo:padding="0.176cm" fo:border="1pt solid #000000" />
  </style:style>
  
  <style:style style:name="heading_row" style:family="table-row">
   <style:table-row-properties style:min-row-height="0.741cm" fo:keep-together="auto"/>
  </style:style>
  
  <style:style style:name="heading_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:padding="0.176cm" fo:border="1pt solid #000000"/>
  </style:style>
  
  <style:style style:name="translation_row" style:family="table-row">
   <style:table-row-properties fo:keep-together="auto"/>
  </style:style>
  
  <style:style style:name="translation_left_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:padding="0.176cm" fo:border="1pt solid #000000"/>
  </style:style>
  
  <style:style style:name="translation_counter_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:padding="0.176cm" fo:border="1pt solid #000000"/>
  </style:style>
  
  <style:style style:name="translation_right_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:padding="0.176cm" fo:border="1pt solid #000000"/>
  </style:style>
  
  <style:style style:name="translation_counter_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" fo:line-height="115%" fo:text-align="justify" style:justify-single-word="false"/>
   <style:text-properties officeooo:paragraph-rsid="00128241"/>
  </style:style>
  
  <style:style style:name="translation_left_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" fo:line-height="115%" fo:text-align="justify" style:justify-single-word="false"/>
   <style:text-properties officeooo:paragraph-rsid="00128241"/>
  </style:style>
  
  <style:style style:name="translation_right_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" fo:line-height="100%" fo:text-align="justify" style:justify-single-word="false" fo:keep-together="auto" fo:orphans="0" fo:widows="0" fo:text-indent="0cm" style:auto-text-indent="false" fo:padding="0cm" fo:border="none" fo:keep-with-next="auto"/>
   <style:text-properties officeooo:paragraph-rsid="00128241"/>
  </style:style>
  
  <style:style style:name="text_regular" style:family="paragraph" style:parent-style-name="Standard">
   <loext:graphic-properties draw:fill="none"/>
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:line-height="115%" fo:text-align="justify" style:justify-single-word="false" fo:text-indent="-1.3cm" style:auto-text-indent="false" fo:background-color="transparent"/>
   <style:text-properties officeooo:paragraph-rsid="00128241"/>
  </style:style>

  <style:style style:name="translators_right_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" fo:line-height="100%" fo:text-align="start" style:justify-single-word="false" fo:keep-together="auto" fo:orphans="0" fo:widows="0" fo:text-indent="0cm" style:auto-text-indent="false" fo:padding="0cm" fo:border="none" fo:keep-with-next="auto"/>
   <style:text-properties fo:font-weight="bold" officeooo:paragraph-rsid="00128241" style:font-weight-asian="bold"/>
  </style:style>
  
  <style:style style:name="heading_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" fo:line-height="115%" fo:text-align="center" style:justify-single-word="false"/>
   <style:text-properties fo:font-size="14pt" fo:font-weight="bold" officeooo:paragraph-rsid="00128241" style:font-size-asian="14pt" style:font-weight-asian="bold" style:font-size-complex="14pt"/>
  </style:style>
  
  <style:style style:name="para_title" style:family="paragraph" style:parent-style-name="Standard" style:master-page-name="">
   <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:orphans="0" fo:widows="0" style:page-number="auto" fo:break-before="auto" fo:break-after="auto"/>
   <style:text-properties style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" officeooo:paragraph-rsid="00128241" style:font-weight-asian="bold"/>
  </style:style>
  
  <style:style style:name="para_empty" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:orphans="0" fo:widows="0"/>
   <style:text-properties style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" officeooo:paragraph-rsid="00128241" style:font-weight-asian="bold"/>
  </style:style>

  <style:style style:name="heading_translators" style:display-name="Heading 1" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Text_20_body" style:default-outline-level="1" style:class="text">
   <style:paragraph-properties fo:margin-top="0.423cm" fo:margin-bottom="0.212cm" style:contextual-spacing="false"/>
   <style:text-properties fo:font-size="18pt" fo:font-weight="bold" style:font-size-asian="18pt" style:font-weight-asian="bold" style:font-size-complex="18pt" style:font-weight-complex="bold"/>
  </style:style>

  <style:page-layout style:name="page_layout">
   <style:page-layout-properties fo:page-width="21cm" fo:page-height="29.7cm" style:num-format="1" style:print-orientation="portrait" fo:margin-top="2cm" fo:margin-bottom="2cm" fo:margin-left="2cm" fo:margin-right="2cm" style:writing-mode="lr-tb" style:layout-grid-color="#c0c0c0" style:layout-grid-lines="20" style:layout-grid-base-height="0.706cm" style:layout-grid-ruby-height="0.353cm" style:layout-grid-mode="none" style:layout-grid-ruby-below="false" style:layout-grid-print="false" style:layout-grid-display="false" style:footnote-max-height="0cm" loext:margin-gutter="0cm">
    <style:footnote-sep style:width="0.018cm" style:distance-before-sep="0.101cm" style:distance-after-sep="0.101cm" style:line-style="solid" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
   </style:page-layout-properties>
  </style:page-layout>

 </office:automatic-styles>

 <office:body>
  <office:text>
   <text:p text:style-name="para_title">Тitel</text:p>
   <text:p text:style-name="para_empty"/>
   
   <table:table table:name="table_fkt" table:style-name="table_fkt">
   
    <table:table-column table:style-name="table_counter_column"/>
    <table:table-column table:style-name="table_left_column"/>
    <table:table-column table:style-name="table_right_column"/>
""")


###############################################################################
# @brief Writes footer for translation table in fodt
# @param out    outputfile
#
def table_footer_fodt(out):
  out.write("""
   </table:table>
  </office:text>
 </office:body>
</office:document>
""")


###############################################################################
# @brief Writes table row  with columns for origin and translation in fodt
# @param out     outputfile
# @param origin  origin in left column
# @param trans   translation in right column
#
def table_row_fodt(out, org, trans, even_odd):
  global cell_counter
 
  if even_odd is None:
    bg = 'none'

  else:
    if even_odd:
      bg = 'even'

    else:
      bg = 'odd'

  out.write("""
    <table:table-row table:style-name="translation_row">
    
     <table:table-cell table:style-name="translation_counter_cell" office:value-type="string">
      <text:p text:style-name="translation_counter_text">{0}</text:p>
     </table:table-cell>
     
     <table:table-cell table:style-name="translation_left_cell" office:value-type="string">
      <text:p text:style-name="translation_left_text">{1}</text:p>
     </table:table-cell>
     
     <table:table-cell table:style-name="translation_right_cell" office:value-type="string">
      <text:p text:style-name="translation_right_text">{2}</text:p>
     </table:table-cell>
     
    </table:table-row>
  """.format(cell_counter, org, trans))

  cell_counter += 1

###############################################################################
# @brief Writes table separator for later input of translators names in fodt
# @param out     outputfile
# @param title   title for document navigator
#
def table_translators_fodt(out, title):
  out.write("""
    <table:table-row table:style-name="translators_row">
     <table:table-cell table:style-name="translators_left_cell" table:number-columns-spanned="2" office:value-type="string">
      <text:h text:style-name="heading_translators" text:outline-level="1">{0}</text:h>
     </table:table-cell>
     <table:table-cell table:style-name="translators_right_cell" office:value-type="string">
      <text:p text:style-name="translators_right_text">EK:</text:p>
      <text:p text:style-name="translators_right_text">SK:</text:p>
     </table:table-cell>
    </table:table-row>
  """.format(title))



###############################################################################
# @brief Writes table separator to describe following content in fodt
# @param out     outputfile
# @param title   title for document navigator
#
def table_heading_fodt(out, title):
  out.write("""
    <table:table-row table:style-name="heading_row">
     <table:table-cell table:style-name="heading_cell" table:number-columns-spanned="3" office:value-type="string">
      <text:p text:style-name="heading_text">{0}</text:p>
     </table:table-cell>
     <table:covered-table-cell/>
    </table:table-row>
  """.format(title))


###############################################################################
# @brief Writes an empty paragraph in fodt
# @param out     outputfile
#
def text_empty_para_fodt(out):
  out.write("<text:p text:style-name='EMPTY'/>")


###############################################################################
# @brief returns linebreak in fodt
# @return  linebreak sequence
#
def text_linebreak_fodt():
  return "\n\n"
