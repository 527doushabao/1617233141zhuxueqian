Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics', 'chemistry', 1997, 2000)
>>> tup2 = (1, 2, 3, 4, 5, 6, 7 )
>>> print "tup1[0]: ", tup1[0]
tup1[0]:  physics
>>> print "tup2[1:5]: ", tup2[1:5]
tup2[1:5]:  (2, 3, 4, 5)
>>> tup1 = (12, 34.56)
>>> tup2 = ('abc', 'xyz')
>>> tup3 = tup1 + tup2
>>> print tup3
(12, 34.56, 'abc', 'xyz')
>>> print 'abc', -4.24e93, 18+6.6j, 'xyz';
abc -4.24e+93 (18+6.6j) xyz
>>> x, y = 1, 2
>>> print "Value of x , y : ", x,y
Value of x , y :  1 2
>>> tup1 = ("all")
>>> print tup1
all
>>>  tup1 = ("all",)
 
  File "<pyshell#13>", line 2
    tup1 = ("all",)
    ^
IndentationError: unexpected indent
>>> print tup1
all
>>> tup1 = ("all",)
>>> print tup1
('all',)
>>> 
