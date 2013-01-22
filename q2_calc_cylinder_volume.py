#Filename: q2_calc_cylinder_volume.py
#Author: Tan Di Sheng
#Created: 20130121
#Modified: 20130121
#Description: This program reads the radius and length of a cylinder and
#computes its volume.

import math

while (True):
    contorquit = input("Continue? ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        break
        
    while (True):
        rInput = input("Please input the radius of the cylinder: ")
        lInput = input("Please input the length of the cylinder: ")
        try:
            float(rInput) and float(lInput)
        except:
            print("Please input a number")
        else:
            break

    rInput = float(rInput)
    lInput = float(lInput)

    aInput = rInput * rInput * math.pi
    print("The base area of the cylinder is: " + "{0:5.2f}".format(aInput))

    vInput = aInput * lInput
    print("The total volume of the cylinder is: " + "{0:5.2f}".format(vInput))


