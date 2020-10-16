def main_actvities():
  global main_activity_input
  main_activity_input = input("""
    Welcome to the smart calculator. These are the options:
    a.addition
    b.subtraction
    c.multiplication
    d.division
    e.divisibilty_test
    f.square
    g.square root
    h.area
    i.conversion
  """)
main_actvities()

if main_activity_input == "a" or main_activity_input == "A" or main_activity_input == "addition" or main_activity_input == "Addition":
  from addition import *
  
elif main_activity_input == "b" or main_activity_input == "B" or main_activity_input == "subtraction" or main_activity_input == "Subtraction":
  from subtraction import *
  
elif main_activity_input == "c" or main_activity_input == "C" or main_activity_input == "multiplication" or main_activity_input == "Multiplication":
  from multiplication import *
  
elif main_activity_input == "d" or main_activity_input == "D" or main_activity_input == "division" or main_activity_input == "Division":
  from division import *

elif main_activity_input == "e" or main_activity_input == "E" or main_activity_input == "divisibilty_test" or main_activity_input == "Divisibilty_test":
  from divisibility import *


elif main_activity_input == "f" or main_activity_input == "F" or main_activity_input == "square" or main_activity_input == "Square":
  from squre import *  

elif main_activity_input == "g" or main_activity_input == "G" or main_activity_input == "square root" or main_activity_input == "Square root":
  from squre import *
  
elif main_activity_input == "h" or main_activity_input == "h" or main_activity_input == "area" or main_activity_input == "Area":
  from area import *
  
elif main_activity_input == "i" or main_activity_input == "I" or main_activity_input == "conversion" or main_activity_input == "Conversion":
  
  from Converting import *


