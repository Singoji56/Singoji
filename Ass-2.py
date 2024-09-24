Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=[10,10.05,True,15+2j,'PYSPIDERS' , ['10string'.'QSPIDERS'],['Ram','Sam'] , [10,20,30],["Hello", ['venu', ' kashi']]]
SyntaxError: invalid syntax
x
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x
NameError: name 'x' is not defined
X
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    X
NameError: name 'X' is not defined

x=[10,10.05,True,15+2j,'PYSPIDERS' , ['10string','QSPIDERS'],['Ram','Sam'] , [10,20,30],["Hello", ['venu', ' kashi']]]
x
[10, 10.05, True, (15+2j), 'PYSPIDERS', ['10string', 'QSPIDERS'], ['Ram', 'Sam'], [10, 20, 30], ['Hello', ['venu', ' kashi']]]
x=[10,10.05,True,15+2j,'PYSPIDERS' , ['10string','QSPIDERS'],['Ram','Sam'] , [10,20,30],["Hello", ['venu', ' kashi']]]
x
[10, 10.05, True, (15+2j), 'PYSPIDERS', ['10string', 'QSPIDERS'], ['Ram', 'Sam'], [10, 20, 30], ['Hello', ['venu', ' kashi']]]
x=[10, 10.05, True, 15+2j, 'PYSPIDERS' , ['10string', 'QSPIDERS'],[Ram', 'Sam'], [10, 20, 30],[ "Hello", ['venu', 'kashi']]]
                                                                   
SyntaxError: unterminated string literal (detected at line 1)
x=[10, 10.05, True, 15+2j, 'PYSPIDERS' , ['10string', 'QSPIDERS'],['Ram', 'Sam'], [10, 20, 30],[ "Hello", ['venu' , 'kashi']]]
                                                                   
x
                                                                   
[10, 10.05, True, (15+2j), 'PYSPIDERS', ['10string', 'QSPIDERS'], ['Ram', 'Sam'], [10, 20, 30], ['Hello', ['venu', 'kashi']]]
x[4][0:9:]
                                                                   
'PYSPIDERS'
x[5][0][2:5]
                                                                   
'str'
x[4][2:7:]
                                                                   
'SPIDE'
x[6][1][0:5:2]
                                                                   
'Sm'
x[5][1][0:5:2]
                                                                   
'QPD'
x[-3][0:1]
                                                                   
['Ram']
x[-3][-1:-2]
                                                                   
[]
x[-3][::-1]
                                                                   
['Sam', 'Ram']
x=[10, 10.05, True, 15+2j, 'PYSPIDERS' , ['10string', 'QSPIDERS'],['Ram', 'Sam'], [10, 20, 30],[ "Hello", ['venu' , 'kashi']]]
                                                                   
x[7][6:8:]
                                                                   
[]
x[7][:8]
                                                                   
[10, 20, 30]
x[7][6:8:]
                                                                   
[]
x[7][4:8:]
                                                                   
[]
x[7][2]+[7][1]+[7][0]
                                                                   
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x[7][2]+[7][1]+[7][0]
IndexError: list index out of range
x[7][2],[7][1],[7][0]
                                                                   
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x[7][2],[7][1],[7][0]
IndexError: list index out of range
x[7][2],x[7][1],x[7][0]
                                                                   
(30, 20, 10)
x[7][2]+x[7][1]+x[7][0]
                                                                   
60
list(x[7][2],x[7][1],x[7][0])
                                                                   
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(x[7][2],x[7][1],x[7][0])
TypeError: list expected at most 1 argument, got 3
s=x[7][2],x[7][1],x[7][0]
                                                                   
list(s)
                                                                   
[30, 20, 10]
s=x[7][2],x[7][0],x[7][1]
                                                                   
list(s)
                                                                   
[30, 10, 20]
x=[10, 10.05, True, 15+2j, 'PYSPIDERS' , ['10string', 'QSPIDERS'],['Ram', 'Sam'], [10, 20, 30],[ "Hello", ['venu' , 'kashi']]]
                                                                   
x[-1][:-2:-1]
                                                                   
[['venu', 'kashi']]
x[-1][:-2]
                                                                   
[]
x[-1][-2]
                                                                   
'Hello'
x[-1][-1][-2]
                                                                   
'venu'
x[-1][-1]
                                                                   
['venu', 'kashi']
x[-1][::-1]
                                                                   
[['venu', 'kashi'], 'Hello']
>>> x[-1][-1][::-1]
...                                                                    
['kashi', 'venu']
>>> x[-4][-1:-6:-2]
...                                                                    
['QSPIDERS']
>>> x[-4][-1::-2]
...                                                                    
['QSPIDERS']
>>> x[-5][-1::-2]
...                                                                    
'SEISP'
>>> x[-5][-1:-7+1:-2]
...                                                                    
'SEI'
>>> x[-5][-1:-8+1:-2]
...                                                                    
'SEI'
>>> x[-5][-1:-7-1:-2]
...                                                                    
'SEIS'
>>> x=[10, 10.05, True, 15+2j, 'PYSPIDERS' , ['10string', 'QSPIDERS'],['Ram', 'Sam'], [10, 20, 30],[ "Hello", ['venu' , 'kashi']]]
...                                                                    
>>> x[5][0][2:6+1]
...                                                                    
'strin'
>>> x[5][0][2:6+1:2]
...                                                                    
'srn'
