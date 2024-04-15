# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:18:36 2023

@author: USER
"""

# 不定長度引數，會以串列來承接內容
def showStudents(*stud):
    for people in stud:
        print("學生：",people)
    
    
showStudents()

showStudents('David','John','Peter')    

print()


def employee(name,pay,*work,area):
    print("員工：",name)
    print("薪資：",pay)
    for item in work:
        print("工作項目：",item)
        
    print("工作地：",area)


employee("Bill",45000,'睡覺','喝茶','看youtube',area='台中市')



    

