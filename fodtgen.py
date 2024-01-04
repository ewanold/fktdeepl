###############################################################################
# @brief Generator for fodt file
#

cell_counter                  = 1
heading_row_height            = ""
          
column_width                  = "95mm" 
page_width                    = "210mm" 
page_height                   = "297mm" 
table_width                   = "190mm" 
counter_width                 = "10mm"
margin_rtlb                   = "2mm"
padding_rtlb                  = "1mm"
          
creation_date                 = "2023-12-29T15:49:57"
doc_title                     = "Titel"
frame_style                   = "1pt solid #000000"
          
translators_span_left         = "2"
translators_span_right        = "1"
heading_span                  = "3"
          
translators_color             = "#dfda53"
heading_color                 = "#deab45"
    
translation_counter_color     = "#ffffff"
translation_left_color        = "#ffffff"
translation_right_color       = "#ffffff"
translation_3rd_color         = "#ffffff"

translation_counter_color_odd = "#eeeeee"
translation_left_color_odd    = "#eeeeee"
translation_right_color_odd   = "#eeeeee"
translation_3rd_color_odd     = "#eeeeee"

translation_medium_color      = "#f8cfd8"
translation_medium_color_odd  = "#f1a8b9"

###############################################################################
# @brief Setup for internal values of table generator in fodt
# @param title   document title
# @param date    creation date
# @param cols    table columns 2, 3
#
def table_setup_fodt(title, date, cols):
  global translators_span_right, heading_span, page_width, table_width, doc_title, creation_date
  global translation_right_color_odd, translation_right_color

  doc_title = title
  creation_date = date

  if cols == 2:
    translators_span_right = "2"
    heading_span           = "3"
    page_width             = "210mm" 
    table_width            = "190mm" 

  elif cols == 3:
    translators_span_right = "3"
    heading_span           = "4"
    page_width             = "315mm" 
    table_width            = "285mm" 

    translation_right_color     = translation_medium_color
    translation_right_color_odd = translation_medium_color_odd


###############################################################################
# @brief Writes header for translation table in fodt
# @param out    outputfile
# @param cls    number of columns 2, 3
#
def table_header_fodt(out, cols):
  out.write("""<?xml version="1.0" encoding="UTF-8"?>

<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" 
                 xmlns:ooo="http://openoffice.org/2004/office" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" 
                 xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" 
                 xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" 
                 xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" 
                 xmlns:rpt="http://openoffice.org/2005/report" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" 
                 xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" 
                 xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" 
                 xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:ooow="http://openoffice.org/2004/writer" 
                 xmlns:oooc="http://openoffice.org/2004/calc" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" 
                 xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:tableooo="http://openoffice.org/2009/table" 
                 xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" 
                 xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" 
                 xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" 
                 xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" 
                 xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" 
                 xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                 xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" 
                 xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:officeooo="http://openoffice.org/2009/office" office:version="1.3" 
                 office:mimetype="application/vnd.oasis.opendocument.text">
 
 <office:meta>
   <meta:creation-date>""" + creation_date + """</meta:creation-date>
   <meta:generator>fktdeepl</meta:generator>
 </office:meta>

 <office:automatic-styles>
  
  <style:style style:name="table_fkt" style:family="table">
   <style:table-properties style:width='""" + table_width + """' fo:margin-left="1cm" fo:margin-top="0cm" 
                           fo:margin-bottom="0cm" fo:break-before="auto" fo:break-after="auto" table:align="left" 
                           style:writing-mode="lr-tb"/>
  </style:style>
  
  <!-- Column definitions -->

  <style:style style:name="table_counter_column" style:family="table-column">
   <style:table-column-properties style:column-width='""" + counter_width + """'/>
  </style:style>
  
  <style:style style:name="table_left_column" style:family="table-column">
   <style:table-column-properties style:column-width='""" + column_width + """'/>
  </style:style>
  
  <style:style style:name="table_right_column" style:family="table-column">
   <style:table-column-properties style:column-width='""" + column_width + """'/>
  </style:style>
  
  <style:style style:name="table_3rd_column" style:family="table-column">
   <style:table-column-properties style:column-width='""" + column_width + """'/>
  </style:style>
  
  <!-- Translator row definitions -->

  <style:style style:name="translators_row" style:family="table-row">
   <style:table-row-properties fo:keep-together="auto"/>
  </style:style>
  
  <style:style style:name="translators_counter_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translators_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """' />
  </style:style>
  
  <style:style style:name="translators_left_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translators_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """' />
  </style:style>
  
  <style:style style:name="translators_right_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translators_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """' />
  </style:style>
  
  <!-- Heading definitions -->

  <style:style style:name="heading_row" style:family="table-row">
   <style:table-row-properties style:min-row-height="0.741cm" fo:keep-together="auto"/>
  </style:style>
  
  <style:style style:name="heading_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + heading_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <!-- Translation row definitions -->

  <style:style style:name="translation_row" style:family="table-row">
   <style:table-row-properties fo:keep-together="auto"/>
  </style:style>

  <!-- Regular translation cells -->

  <style:style style:name="translation_counter_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_counter_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_left_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_left_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_right_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_right_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_3rd_cell" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_3rd_color + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <!-- Alternative translation cells -->
    
  <style:style style:name="translation_counter_cell_odd" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_counter_color_odd + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_left_cell_odd" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_left_color_odd + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_right_cell_odd" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_right_color_odd + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <style:style style:name="translation_3rd_cell_odd" style:family="table-cell">
   <style:table-cell-properties style:vertical-align="" fo:background-color='""" + translation_3rd_color_odd + """' 
                                fo:padding='""" + padding_rtlb + """' fo:border='""" + frame_style + """'/>
  </style:style>
  
  <!-- Translation texts -->
    
  <style:style style:name="translation_counter_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" 
                               fo:line-height="115%" fo:text-align="justify" style:justify-single-word="false"/>
  </style:style>
  
  <style:style style:name="translation_left_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" 
                               fo:line-height="115%" fo:text-align="justify" style:justify-single-word="false"/>
  </style:style>
  
  <style:style style:name="translation_right_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" 
                               style:contextual-spacing="false" fo:line-height="100%" fo:text-align="justify" 
                               style:justify-single-word="false" fo:keep-together="auto" fo:orphans="0" 
                               fo:widows="0" fo:text-indent="0cm" style:auto-text-indent="false" fo:padding="0cm" 
                               fo:border="none" fo:keep-with-next="auto"/>
  </style:style>
  
  <style:style style:name="translation_3rd_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" 
                               style:contextual-spacing="false" fo:line-height="100%" fo:text-align="justify" 
                               style:justify-single-word="false" fo:keep-together="auto" fo:orphans="0" 
                               fo:widows="0" fo:text-indent="0cm" style:auto-text-indent="false" fo:padding="0cm" 
                               fo:border="none" fo:keep-with-next="auto"/>
  </style:style>
  
  <!-- Heading definitions -->

  <style:style style:name="heading_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" style:contextual-spacing="false" 
                               fo:line-height="115%" fo:text-align="center" style:justify-single-word="false"/>
   <style:text-properties fo:font-size="14pt" fo:font-weight="bold" style:font-size-complex="14pt"/>
  </style:style>
  
  <style:style style:name="heading_translators" style:display-name="Heading 1" style:family="paragraph" style:parent-style-name="Heading" 
               style:next-style-name="Text_20_body" style:default-outline-level="1" style:class="text">
   <style:paragraph-properties fo:margin-top="0.4cm" fo:margin-bottom="0.2cm" style:contextual-spacing="false"/>
   <style:text-properties fo:font-size="18pt" fo:font-weight="bold" 
                          style:font-size-complex="18pt" style:font-weight-complex="bold"/>
  </style:style>

  <!-- Other definitions -->

  <style:style style:name="text_regular" style:family="paragraph" style:parent-style-name="Standard">
   <loext:graphic-properties draw:fill="none"/>
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:line-height="115%" fo:text-align="justify" 
                               style:justify-single-word="false" fo:text-indent="-1.3cm" style:auto-text-indent="false" 
                               fo:background-color="transparent"/>
  </style:style>

  <style:style style:name="translators_right_text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" 
                               style:contextual-spacing="false" fo:line-height="100%" fo:text-align="start" 
                               style:justify-single-word="false" fo:keep-together="auto" fo:orphans="0" fo:widows="0" 
                               fo:text-indent="0cm" style:auto-text-indent="false" fo:padding="0cm" fo:border="none" 
                               fo:keep-with-next="auto"/>
   <style:text-properties fo:font-weight="bold"/>
  </style:style>
  
  <style:style style:name="para_title" style:family="paragraph" style:parent-style-name="Standard" style:master-page-name="">
   <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:orphans="0" fo:widows="0" 
                               style:page-number="auto" fo:break-before="auto" fo:break-after="auto"/>
   <style:text-properties style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" 
                          fo:font-weight="bold" />
  </style:style>
  
  <style:style style:name="para_date" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:orphans="0" fo:widows="0"/>
   <style:text-properties fo:font-weight="bold" />
  </style:style>

  <!-- Page definitions -->

  <style:page-layout style:name="page_layout">
   <style:page-layout-properties fo:page-width='""" + page_width + """' fo:page-height='""" + page_height + """' style:num-format="1"
                                 fo:margin-top='""" + margin_rtlb + """' fo:margin-bottom='""" + margin_rtlb + """' 
                                 fo:margin-left='""" + margin_rtlb + """' fo:margin-right='""" + margin_rtlb + """' 
   style:writing-mode="lr-tb" style:footnote-max-height="0cm" loext:margin-gutter="0cm">
    <style:footnote-sep style:width="0.018cm" style:distance-before-sep="0.101cm" style:distance-after-sep="0.101cm" 
                        style:line-style="solid" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
   </style:page-layout-properties>
   <style:header-style/>
   <style:footer-style/>
  </style:page-layout>

 </office:automatic-styles>

 <office:master-styles>
  <style:master-page style:name="Standard" style:page-layout-name="page_layout"/>
 </office:master-styles>

 <office:body>
  <office:text>
   <text:p text:style-name="para_title">""" + doc_title + """</text:p>
   <text:p text:style-name="para_date">""" + creation_date + """</text:p>
   
   <table:table table:name="table_fkt" table:style-name="table_fkt">
   
    <table:table-column table:style-name="table_counter_column"/>
    <table:table-column table:style-name="table_left_column"/>
    <table:table-column table:style-name="table_right_column"/>
""")

  if cols == 3:
    out.write("""    <table:table-column table:style-name="table_3rd_column"/>
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
# @param out       outputfile
# @param origin    origin in left column
# @param col3text  optional text for third column
# @param trans     translation in right column
#
def table_row_fodt(out, org, trans, col3text, even_odd):
  global cell_counter

  if even_odd is None:
    bg = ''

  else:
    if even_odd:
      bg = '_odd'

    else:
      bg = ''

  out.write("""
    <table:table-row table:style-name="translation_row">
    
     <table:table-cell table:style-name="translation_counter_cell{0}" office:value-type="string">
      <text:p text:style-name="translation_counter_text">{1}</text:p>
     </table:table-cell>
     
     <table:table-cell table:style-name="translation_left_cell{2}" office:value-type="string">
      <text:p text:style-name="translation_left_text">{3}</text:p>
     </table:table-cell>
     
     <table:table-cell table:style-name="translation_right_cell{4}" office:value-type="string">
      <text:p text:style-name="translation_right_text">{5}</text:p>
     </table:table-cell>
""".format(bg, cell_counter, bg, org, bg, trans))

  if col3text != None:
    out.write("""
     <table:table-cell table:style-name="translation_3rd_cell{0}" office:value-type="string">
      <text:p text:style-name="translation_3rd_text">{1}</text:p>
     </table:table-cell>
""".format(bg, col3text))
     
  out.write("""
    </table:table-row>
  """)

  cell_counter += 1

###############################################################################
# @brief Writes table separator for later input of translators names in fodt
# @param out     outputfile
# @param title   title for document navigator
#
def table_translators_fodt(out, title):
  print (title)
  out.write("""
    <table:table-row table:style-name="translators_row">
     <table:table-cell table:style-name="translators_left_cell" table:number-columns-spanned='""" + translators_span_left + """' office:value-type="string">
      <text:h text:style-name="heading_translators" text:outline-level="1">""" + title + """</text:h>
     </table:table-cell>
     <table:table-cell table:style-name="translators_right_cell" table:number-columns-spanned='""" + translators_span_right + """' office:value-type="string">
      <text:p text:style-name="translators_right_text">EK:</text:p>
      <text:p text:style-name="translators_right_text">SK:</text:p>
     </table:table-cell>
    </table:table-row>
  """)


###############################################################################
# @brief Writes table separator to describe following content in fodt
# @param out     outputfile
# @param title   title for document navigator
#
def table_heading_fodt(out, title):
  out.write("""
    <table:table-row table:style-name="heading_row">
     <table:table-cell table:style-name="heading_cell" table:number-columns-spanned='""" + heading_span + """' office:value-type="string">
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
  return "\n<fktdeepl:br />\n"
