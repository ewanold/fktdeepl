export FKTDEEPL_KEY="f5c84e42-f195-6b60-5f67-e13b97626693:fx"

rem Test call to deepl via curl
rem curl -X POST https://api-free.deepl.com/v2/translate  -H "Authorization: DeepL-Auth-Key f5c84e42-f195-6b60-5f67-e13b97626693:fx"  -d "text=Hello, world!" -d "source_lang=EN"  -d "target_lang=RU"

rem run python apps

python fktdeepl.py -i testfile2.txt -c -d -l DE    -o testfile2-de.html
python fktdeepl.py -i testfile2.txt -c -d -l EN-GB -o testfile2-en.html

python fktsplit3.py  testfile3-export.txt   "####links####"  "####mitte####"  "####rechts####"  "####ende####"

python fktsplit2.py  testfile2-export.txt   "####links####"  "####rechts####"  "####ende####"