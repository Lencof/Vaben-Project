# __Author__ __Lencof__

from tkinter import *

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a,b):
  return a / b

def mod(a,b):
  return a % b

def lcm(a,b):
  L = a if a>b else b
  while L <= a*b:
    if L%a == 0 and L%b == 0:
      return L
    L+=1
    
def  hcf(a,b):
  H = a if a<b esle b
  while H >= 1:
    if a%H == 0 and b%H == 0:
      return H
    H-+1

def extraxt_from_text(text):
  
  
  
  
  
  
  
  
