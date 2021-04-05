# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:04:57 2020

@author: MAGIL
"""


cas_number = '7732-18-5'
rho = 1000 
mu = 1 
Tm = 273.15 
Tb = 373.13 
k = 0.58 


def convert_to_kelvin(temperature, units):
    var_type = type(temperature)
    if (var_type != float and var_type != int) or (units != 'C' and units != 'F' and units != 'K'):
        print('Invalid temperature or units input')
        return None
    if units == 'K':
        return temperature
    elif units == 'C':
        return temperature + 273.15
    elif units == 'F':
        return (temperature - 32) * 5 / 9 + 273.15
    
def is_gas(temperature):
    if type(temperature) != float and type(temperature) != int:
        return None
    elif (temperature >= Tb):
        return True
    else:
        return False

def is_liquid(temperature):
    if type(temperature) != float and type(temperature) != int:
        return None
    elif (Tm <= temperature < Tb):
        return True
    else:
        return False

def is_solid(temperature):
    if type(temperature) != float and type(temperature) != int:
        return None
    elif (Tm > temperature):
        return True
    else:
        return False


if __name__ == '__main__':
    
    units = input("Input your desired units: \n('K' for Kelvin, 'C' for Celcius, and 'F' for Fahrenheit)")
    if units != 'C' and units != 'F' and units != 'K':
        print("Invalid unit input")
    else:
        
        temperature = input("Input your desired temperature value: ")        
        try: 
            temperature = float(temperature) 
            temperature = convert_to_kelvin(temperature, units)
            if temperature == None:
                print('Invalid input!')
            else:
                if is_solid(temperature) == True:
                    print('The state of your material is solid.')
                elif is_liquid(temperature) == True:
                    print('The state of your material is liquid.')
                elif is_gas(temperature) == True:
                    print('The state of your material is gaseous.')
                else:
                    print('Invalid input! Neither of 3 states')
        except:
            print('Invalid input!')
   

