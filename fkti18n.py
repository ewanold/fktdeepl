###############################################################################
# @brief Get user text based on locale
#

from fktlib import is_locale

#####################################################
# i18n section modeled with functions instead of gettext & Co.
#

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


def bad_state_for_left(ln):
  if is_locale("RU"): return "Неверный статус для слева в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Links in Zeile {0}".format(ln)
  return                     "Wrong state für left in line".format(ln)


def bad_state_for_center(ln):
  if is_locale("RU"): return "Неверный статус для центра в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Mitte in Zeile {0}".format(ln)
  return                     "Wrong state für middle in line".format(ln)


def bad_state_for_right(ln):
  if is_locale("RU"): return "Неверный статус для справа в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Rechts in Zeile {0}".format(ln)
  return                     "Wrong state für right in line".format(ln)


def bad_state_for_end(ln):
  if is_locale("RU"): return "Неверный статус для  в линии {0}".format(ln)
  if is_locale("DE"): return "Falscher Zustand für Ende in Zeile {0}".format(ln)
  return                     "Wrong state für end in line".format(ln)


def bad_column_sum():
  if is_locale("RU"): return "Неравное количество ячеек в столбцах"
  if is_locale("DE"): return "Ungleiche Anzahl Zellen in den Spalten"
  return                     "Differing numbers of cells in columns"


def text_section(n):
  if is_locale("RU"): return "перевод {0}".format(n)
  if is_locale("DE"): return "Abschnitt {0}".format(n)
  return                     "Section {0}".format(n)


def text_statistic(n, tm):
  sec = int(tm * 10 ) / 10
  if is_locale("RU"): return "{0} Ячейки таблицы созданы в {1}".format(n, sec)
  if is_locale("DE"): return "{0} Tabellenzellen erzeugt in {1}s".format(n, sec)
  return                     "{0} table cells created in {1}s".format(n, sec)

def no_authkey():
  if is_locale("RU"): return "Не передан ключ API для deepl"
  if is_locale("DE"): return "Kein API-Key für deepl übergeben"
  return                     "No API key for deepl given"
