#Filename: compute_bmi.py
#Author: Tan Di Sheng
#Created: 20130121
#Modified: 20130121
#Description: This program is used to calculate the user's BMI using the
#input data of the user's height and weight from the user.

mass = int(False)
mass = input("Enter your mass in kilograms: ")
if mass.isdigit() == False:
    print("Please input a number")
print("Your mass is " + str(mass) + "kg")
mass = int(False)

height = float(False)    
height = input("Enter your height in metres: ")
if height.isdigit() == False:
    print("Please input a number")
print("Your height is " + str(height) + "m")
height = float(False) 

bmi = mass / (height * height)

print("BMI = {0:.1f}".format(bmi))

