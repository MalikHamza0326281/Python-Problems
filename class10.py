# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
# Freezing: Temperatures 0°C or below
# Moderate: Temperatures between 1°C and 24°C
# Hot: Temperatures 25°C and above
celc = int(input("enter the temperature in celcius:"))
if celc <= 0:
    print("the temperature is cold")
elif celc >= 1:
    print("the temperature is moderate")
elif celc <= 25:
    print("the temperature is hot")
