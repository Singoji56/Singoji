Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={100:(10,'python','helloworld',('django framework',),{'bat':['c programming','java','c++','r programming']},(10,20)),'apple':{'venugopal','pooja','kasinath'},'z':'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r programming']}, (10, 20)), 'apple': {'kasinath', 'pooja', 'venugopal'}, 'z': 'pyspiders'}

d['apple']
{'kasinath', 'pooja', 'venugopal'}
tuple(d['apple'])
('kasinath', 'pooja', 'venugopal')
a=tuple(d['apple'])
a
('kasinath', 'pooja', 'venugopal')
a[0]
'kasinath'
a[2]
'venugopal'
d[100][5]
(10, 20)
b=d[100][5]
b
(10, 20)
a[2],b
('venugopal', (10, 20))
c=('venugopal', (10, 20))
dict(c)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 9; 2 is required
c=(('venugopal', (10, 20)),)
c
(('venugopal', (10, 20)),)
dict(c)
{'venugopal': (10, 20)}
d['apple']-={'pooja','kashinath'}
d['apple']
{'kasinath', 'venugopal'}
d['apple']-={'pooja','kasinath'}
d['apple']
{'venugopal'}
a=str(d['apple'])
a
"{'venugopal'}"
ed
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    ed
NameError: name 'ed' is not defined. Did you mean: 'd'?
a=tuple(d['apple'])
a
('venugopal',)
a
('venugopal',)
a=list(d['apple'])
a
['venugopal']
a[0]
'venugopal'
dict(c)
{'venugopal': (10, 20)}
e=dict(c)
e
{'venugopal': (10, 20)}
e['venugopal']
(10, 20)
a
['venugopal']
a=tuple(d['apple'])
a
('venugopal',)
d['apple']
{'venugopal'}
d['apple']|={'pooja','kasinath'}
d['apple']
{'kasinath', 'pooja', 'venugopal'}
a=tuple(d['apple'])
a
('kasinath', 'pooja', 'venugopal')
b=a[1][::-1]
b
'ajoop'
c=a[0]
c
'kasinath'
dict(b,c)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict(b,c)
TypeError: dict expected at most 1 argument, got 2
dict((b,c))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    dict((b,c))
ValueError: dictionary update sequence element #0 has length 5; 2 is required
dict((b,c),)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    dict((b,c),)
ValueError: dictionary update sequence element #0 has length 5; 2 is required
ed
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    ed
NameError: name 'ed' is not defined. Did you mean: 'd'?
d=b,c
d
('ajoop', 'kasinath')










































d=(('ajoop', 'kasinath'),)
dict(d)
{'ajoop': 'kasinath'}
d=((b,c),)
d
(('ajoop', 'kasinath'),)
dict(d)
{'ajoop': 'kasinath'}
d
(('ajoop', 'kasinath'),)
d={100:(10,'python','helloworld',('django framework',),{'bat':['c programming','java','c++','r programming']},(10,20)),'apple':{'venugopal','pooja','kasinath'},'z':'pyspiders'}
d
{100: (10, 'python', 'helloworld', ('django framework',), {'bat': ['c programming', 'java', 'c++', 'r programming']}, (10, 20)), 'apple': {'kasinath', 'pooja', 'venugopal'}, 'z': 'pyspiders'}
a=list(d.keys())
a
[100, 'apple', 'z']
b=a[1]
b
'apple'
c=tuple(d['apple'])
c
('kasinath', 'pooja', 'venugopal')
e=a[2][:5:]
e
'z'
c=a[2][:5:]
c
'z'
c=tuple(d['apple'])c
SyntaxError: incomplete input
c
'z'
c=tuple(d['apple'])
c
('kasinath', 'pooja', 'venugopal')
e=c[2][:5:]
e
'venug'
('kasinath', 'pooja', 'venugopal')
('kasinath', 'pooja', 'venugopal')
>>> e=c[2][:4:]
>>> e
'venu'
>>> f=c[1][:4:]
>>> f
'pooj'
>>> g=c[0][:4:]
>>> g
'kasi'
>>> h=e,f,g
>>> h
('venu', 'pooj', 'kasi')
>>> z=((a,h),)
>>> z
(([100, 'apple', 'z'], ('venu', 'pooj', 'kasi')),)
>>> z=((b,h),)
>>> z
(('apple', ('venu', 'pooj', 'kasi')),)
>>> dict(z)
{'apple': ('venu', 'pooj', 'kasi')}
>>> h=set(h)
>>> h
{'kasi', 'pooj', 'venu'}
>>> z=((b,h),)
>>> z
(('apple', {'kasi', 'pooj', 'venu'}),)
