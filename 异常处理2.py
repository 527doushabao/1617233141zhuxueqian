#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
    print"OK"
    
try:
    mye(0)                
except "Invalid level!":
    print "user defined exception"
else:
    print "else......"
finally:
    print "finally always run......"
