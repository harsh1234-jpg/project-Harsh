# print("hello world")
# if 5>2:
#  print("five is greater than two")

# x=3
# y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

# #h=5

# x=7
# y="harsh"
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# x=3
# y=5
# print(bool(x+y))
# x=""
# print(bool(x))

# a = 5
# print(a)

# x,y,z = "30","40","50"
# print(x)

# x="30","40","50"
# print(x)

# fruit =["apple","banana","cherry"]
# x,y,z=fruit
# print(x)

# x=[1,2,3,4,5]
# print(type(x))
# x ='ANKIT'
# y='is'
# z='a boy'
# print(x,y,z)

# x ="good"
# def my_function():
#   print("pythan is "+x)
# my_function()

# def y():
#  global x
#  x="bad"
# y()
# print("python is "+x)

# x=2
# y=6
# print(x*y)
# print(y/x)
# print(y%x)
# print(x**y)
# print(y//x)

# a=["apple","banana"]
# print(a)

# a=["apple","banana",1,2,True]
# print(a)

# a=["apple","banana","cherry","yfy","fyfyfy","tyry"]
# print(len(a))
# print(a[-1])
# print(a[3])
# print(a[2:5])

# print("hello world")

# a=["apple","banana","cherry",1,2,3]
# a[2]="orange"
# print(a)

# a=[1,2,4,5,6]
# a.insert(2,3)
# print(a)
# a.append(3)

# print(a)
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# print(list1)

# list1=[1,2,3,"apple",4,5,6]
# list1.remove("apple")
# print(list1)
# list1.pop(3)
# print(list1)

# list2=[1,2,3,"apple",4,5,6]
# list2.pop()
# print(list2)

# list1=[1,2,3,4,5,6]
# list1.insert(2,"apple")
# list1.append("banana")
# list1.remove("apple")
# list1.pop()
# print(list1)
# list1.clear()
# print(list1)
# list1=[]
# list1.append(1)
# print(list1)

# list1=[1,2,3,4,5,6]
# for x in list1:
#  print(x)

#  list1=[1,2,3,4,4,4,5,6,7]
#  for x in list1:
#   print(x)

#   list1=[1,5,3,6,7,2]
#   list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# age=18
# if age>=18:
#  print("you are adult")
# else:
#  print("you are not adult")

# mark=90
# if mark>=90:
#  print("grade A+")
# elif mark>=75:
#  print("grade A")
# elif mark>=60:
#  print("grade B")
# else:
#  print("grade C")

# x=20
# if x>10:
#  print("x is greater than 10")
#  if x>20:
#   print("x is also greater than 20")
#  else:
#   print("x is not greater than 20")
# else:
#  print("x is less than 10")

# x=3
# if x%2==0:
#  print("the number is even")
# else:
#  print("the number is odd")

# x = 9
# y = 3
# z = 4
# if x>y and x>z:
#  print("x is greatest")
# elif y>x and y>z:
#  print("y is greatest")
# elif z>x and z>y:
#  print("z is greatest")

# x=["apple","banana","cherry"]
# for y in x:
#  print(y)

# for x in range(10):
#  print(x)

# for x in range(1,20,10):
#  print(x)

# for x in range(1,10):
#   if x%2!=0:
#     print(x)

# for x in range(1,10,2):
#   print(x)

# for x in range(1,4):
#     for y in range(1,3):
#         print(f"i={x},j={y}")

# for x in range(1,10):
#     if x == 4:
#       print(x)
#       break
       
# for x in range(1,4):
#  for y in range(1,4):
#         print(x*y,end='\t')
#  print()

# def greet():
#    print("python")

# greet()

# def greet(name):
#     print(f"hello ,{name}")

# greet("alice")
# greet("bob")

# def greet(num):
#     print(f"number,{num}")

# greet(4)
# greet(5)

# def add(a,b):
#     return a+b
# result = add(4,4)
# print(result)

# def greet(name="student"):
#     print(f"hello,{name}")
# greet()
# greet("alice")

# a=10
# b=20
# def my_func():
#     print(a,b)
# my_func()
# print(a,b)

# #Class

# class Car:
#     def __init__(self, brand, color):  # Correct constructor
#         self.brand = brand
#         self.color = color

#     def drive(self):  # Properly indented method
#         print(f"{self.color} {self.brand} is driving🚓")

# # Object creation
# car1 = Car("BMW", "Black")
# car1.drive()

# car2 = Car("Tesla", "White")
# car2.drive()

# import array
# x=array.array('i',[1,2,3,4,5])
# print(x)

from numpy import random

# x=random.randint(100)
# print(x)

# x=random.rand()
# print(x)
# print(type(x))

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,5))
# print(x)

# x=random.randint(100,size=(2,3,5))
# print(x)

# x=random.choice([1,3,5],size=(2,5,4))
# print(x)

import pandas as pd 
# data = [10,20,30,40]
# s=pd.Series(data)
# print(s)

data={
    "name":["alice","bob","cherlie","davil"],
    "age":[24,25,26,27],
    "city":["delhi","mumbai","chennai","kolkata"]
}
df=pd.DataFrame(data)
print(df)

import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)

import pandas as pd
df=pd.read_csv("")
print(df)

