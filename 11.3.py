#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0
   stu_count_wl163=0
   stu_count_wl161=0
 
   def __init__(self,stu_no,name,stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class= stu_class
      self.male=male
      Student.stuCount += 1
      if self.stu_class=='wl163':
        Student.stu_class_wl163 += 1
      elif self.stu_class=='wl161':
        Student.stu_class_wl161 += 1
   
   def displayCountByClass(self):
     print "Total Student %d" % Student.stuCount
 
   def displayStudent(self):
      print "Stu_no: ", self.stu_no, ", Name : ", self.name,",Stu_class:",self.stu_class,", Male: ",self.male,
   
