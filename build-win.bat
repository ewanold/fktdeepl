pyinstaller --onefile fktwrap.py
pyinstaller --onefile fktdeepl.py
pyinstaller --onefile fktsplit2.py
pyinstaller --onefile fktsplit3.py

md c:\tmp
md c:\tmp\fktdeepl

copy dist\fktwrap.exe    c:\tmp\fktdeepl /Y 
copy dist\fktdeepl.exe   c:\tmp\fktdeepl /Y 
copy dist\fktsplit2.exe  c:\tmp\fktdeepl /Y 
copy dist\fktsplit3.exe  c:\tmp\fktdeepl /Y 

copy test\test.bat       c:\tmp\fktdeepl /Y
copy test\testfile2.txt  c:\tmp\fktdeepl /Y

