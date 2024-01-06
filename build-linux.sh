#!/bin/sh

~/.local/bin/pyinstaller --onefile fktdeepl.py
~/.local/bin/pyinstaller --onefile fktsplit2.py
~/.local/bin/pyinstaller --onefile fktsplit3.py
~/.local/bin/pyinstaller --onefile fktwrap.py

mkdir -p $HOME/tmp/fktdeepl

cp dist/fktwrap   $HOME/tmp/fktdeepl 
cp dist/fktdeepl  $HOME/tmp/fktdeepl 
cp dist/fktsplit2 $HOME/tmp/fktdeepl 
cp dist/fktsplit3 $HOME/tmp/fktdeepl
cp test.sh        $HOME/tmp/fktdeepl 
cp testfile2.txt  $HOME/tmp/fktdeepl 

