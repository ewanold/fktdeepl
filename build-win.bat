pyinstaller --onefile fktdeepl.py

md c:\tmp
md c:\tmp\fktdeepl

copy dist\fktdeepl.exe c:\tmp\fktdeepl /Y
copy test.bat          c:\tmp\fktdeepl /Y
copy testfile2.txt     c:\tmp\fktdeepl /Y

