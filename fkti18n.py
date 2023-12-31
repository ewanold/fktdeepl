import locale

current_locale = ""

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


def enter_inputfile():
  if is_locale("RU"): return "Выберите входной файл"
  if is_locale("DE"): return "Eingabedatei auswählen"
  return                     "Choose input file"


def bad_filetype():
  if is_locale("RU"): return "Неправильный тип файла (html, fodt)"
  if is_locale("DE"): return "Falscher Dateityp (html, fodt)"
  return                     "Wrong file type (html, fodt)"


