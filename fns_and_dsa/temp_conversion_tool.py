FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temperature}°C")
def convert_to_fahrenheit(celsius):
    temperature = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {temperature}°F")


try: 
    temperature = float(input("Enter the temperature to convert: "))

    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if choice.upper() == "C":
        convert_to_fahrenheit(temperature)
    elif choice.upper() == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid choice")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    
    
    
    

