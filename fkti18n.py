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


def bad_state_for_left(ln)
  if is_locale("RU"): return "Неверный статус для слева в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Links in Zeile {0}".format(ln)
  return                     "Wrong state für left in line".format(ln)


def bad_state_for_center(ln)
  if is_locale("RU"): return "Неверный статус для центра в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Mitte in Zeile {0}".format(ln)
  return                     "Wrong state für middle in line".format(ln)


def bad_state_for_right(ln)
  if is_locale("RU"): return "Неверный статус для справа в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Rechts in Zeile {0}".format(ln)
  return                     "Wrong state für right in line".format(ln)


def bad_state_for_end(ln)
  if is_locale("RU"): return "Неверный статус для  в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Ende in Zeile {0}".format(ln)
  return                     "Wrong state für end in line".format(ln)

