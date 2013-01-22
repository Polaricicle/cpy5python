#Filename: q1_fahrenheit_to_celsius.py
#Author: Tan Di Sheng
#Created: 20130122
#Modified: 20130122
#Description: This program reads a Fahrenheit degree in double decimal
#from standard input, then converts it to Celsius and displays the result
#in standard output

while (True): #creates a loop to repeat calculation without restarting application

    fahrenheit = input("""Please input the temperature in Fahrenheit
or "quit" to quit the program: """)
    if (fahrenheit == "quit"): #provides a function to quit application
        quit()
    try: #creates a try and except loop to check for a number
        float(fahrenheit)
    except:
        print("Please input a number")
    else:
        fahrenheit = float(fahrenheit)
        celsius = (5/9) * (fahrenheit -32)
        print("The temperature in Celsius is: " + str(celsius))
