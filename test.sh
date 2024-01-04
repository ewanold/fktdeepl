export FKTDEEPL_KEY="f5c84e42-f195-6b60-5f67-e13b97626693:fx"

# Test call to deepl via curl
# curl -X POST https://api-free.deepl.com/v2/translate  -H "Authorization: DeepL-Auth-Key f5c84e42-f195-6b60-5f67-e13b97626693:fx"  -d "text=Hello, world!" -d "source_lang=EN"  -d "target_lang=RU"

# run python apps

# create fodt documents, 2 columns, 2 languages
python fktdeepl.py -i testfile2.txt -c -l DE    -o testfile2-de.fodt -t fodt
python fktdeepl.py -i testfile2.txt -c -l EN-GB -o testfile2-en.fodt -t fodt

# create lorem fodt document, 2 columns, column 2 empty
python fktdeepl.py -i testfile2.txt -2 -d    

# extract 3 columns from TXT export of translations document
python fktsplit3.py  testfile3-export.txt   "####links####"  "####mitte####"  "####rechts####"  "####ende####"

# extract 2 columns from TXT export of translations document
python fktsplit2.py  testfile2-export.txt   "####links####"  "####rechts####"  "####ende####"

