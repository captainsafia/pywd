Pywd
=====
Pywd is a command-line application written in Python. The application generates a password of the desired length and includes a combination of leters (optionally uppercase), numbers, and symbols. The module can also be used to generate passwords from within another application such as Django web application.

Usage
======
From the commandline
-------
```shell
$ pywd --length=10 --symbol --numbers --letters 
#09;54~4@j
$ pywd --length=10 --symbol --letters 
gvg/ozxyef
$ pywd --length=10 --letters --uppercase 
QWPWTCAPXV 
```
From another module
-------
```python
from pywd.pywd import create_password
create_password(10, True, False, True, False) #)_(`9**53:
create_password(10, False, True, True, False) #]c;$cj)sbv 
create_password(10, False, True, False, True) #hmHoQkFFWQ
```
