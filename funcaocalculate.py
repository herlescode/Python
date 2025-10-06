def calculate_diameter_circle(radius: float) -> float:
    
    #condição se for numero negativo 
    if radius < 0:
        return -1
    
    #calcula o diametro
    diameter = (radius) * 2
    return diameter

    """
Test Cases:
- Radius: 7, Diameter: 14
- Radius: 2.5, Diameter: 5.0
- Radius: 0, Diameter: 0
- Radius: -3, Diameter: -1
- Radius: 1000000, Diameter: 2000000
    """
    #são todos os paramentros que devemos realizar o teste pelo cliente
print(f"Radius: 7, Diameter: {calculate_diameter_circle(7)}")
print(f"Radius: 2.5, Diameter: {calculate_diameter_circle(5.0)}")
print(f"Radius: 0, Diameter: {calculate_diameter_circle(0)}")
print(f"Radius: -3, Diameter: {calculate_diameter_circle(-1)}")
print(f"Radius: 1000000, Diameter: {calculate_diameter_circle(2000000)}")
 