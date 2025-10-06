def celsius_to_fahrenheit(celsius):
    #temperature_c = 25
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
def fahrenheit_to_celsius(fahrenheit):
    #temperature_f = 77
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temperature, unit):
        if unit == 'C':    
            converted_value = celsius_to_fahrenheit(temperature)
        elif unit == 'F':
            converted_value = fahrenheit_to_celsius(temperature)
            
        return converted_value

temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')
    
print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")
    