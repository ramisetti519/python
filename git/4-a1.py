#program that prompts the user for a distance in meters and then displays that distance converted to miles, feet and inches
meter = 0.000621371
i= float(input('Enter meters '))
#converting into miles    
i= i * meter
miles= int(i)
i=i - miles
#into Feet    
i=i* 5280
feet = int(i)
i= i- feet
#to Inches
i= i * 12
inches= round(int(i))
print("Distance is:", miles, 'miles', feet, 'feet',round(inches,2), 'Inches')
