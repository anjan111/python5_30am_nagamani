Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # logical Operators
>>> # logical AND  , Logical OR , Logical  NOT
>>> # Logical AND  ----->>> and  is a keyword which is used for to do the logical AND operation
>>> # input1     and     inpput2 ----->>>>  input1/ input2
>>> # input1   and  input2 ------>>> True/ False
>>> True  and True
True
>>> True  and False
False
>>> False and True
False
>>> False and False
False
>>> # input1 --->> result  when the input1 is False
>>> # input2 --->> result when the input1 is True
>>> 67   and   78
78
>>> # int  --->>>  0--> False ,   +ve/-ve ----> True
>>> # float --->>  0.0-> False ,  +ve/-ve ----> True
>>> # complex -->  0 + 0j --> False , ow--->>>> True
>>> # None ------>> False
>>> # str, list, tuple, set, dict ----->> len of any thing--> 0 ---> False
>>> [] and   45
[]
>>> {34,90} and (34,89)
(34, 89)
>>> ""  and {}
''
>>> "   "  and {}
{}
>>> # Logical OR  ----->>> or  is a keyword which is used for to do the logical OR  operation
>>> # input1     or    inpput2 ----->>>>  input1/ input2
>>> # input1 --->> result  when the input1 is True
>>> # input2 --->> result when the input1 is False
>>> []  or  90
90
>>> {4,3} or 0
set([3, 4])
>>> "" or  {}
{}
>>> "    "  or  {}
'    '
>>> # logical NOT ----->>> not
>>> not {1,2,3}
False
>>> not ""
True
>>> # in
>>> 78  in {45,90,23,78}
True
>>> 90  in {45,78,34}
False
>>> # not in
>>> 78 not in {56,90,78}
False
>>> 90 not in {45,89,23}
True
>>> # is
>>> a =  123
>>> b =  123
>>> id(a)
37515280L
>>> id(b)
37515280L
>>> a is b
True
>>> c = 124
>>> id(c)
37515256L
>>> a is c
False
>>> a = [1,2,3,4]
>>> b = [1,2,3,4]
>>> c = a
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> c
[1, 2, 3, 4]
>>> id(a)
37171848L
>>> id(b)
50154376L
>>> id(c)
37171848L
>>> a is b
False
>>> a is c
True
>>> a is not b
True
>>> a is not c
False
>>> 
