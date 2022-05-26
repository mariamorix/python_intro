import math

print("Welcome to the velocity calculator. Please enter the following:")

mass = float(input("\nMass (in kg): "))
gravity = float(input("Gravity m/s², 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m³, 1.3 for air, 1000 for water): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

if drag_constant == 0.5 :
    radius = float(input("Radius: "))
    cross_sectional_area_sphere = math.pi * radius ** 2
    inner_value_c = (1/2) * density* cross_sectional_area_sphere * drag_constant
    velocity = math.sqrt((mass * gravity)/inner_value_c) * (1 - math.exp ((- math.sqrt(mass * gravity * inner_value_c) / mass) * time))
    print(f"\nThe inner value of c is: {inner_value_c:.3f}")
    print(f"The velocity after {time} seconds is: {velocity:.3f} m/s")
else :
    cross_sectional_area = float(input("Cross sectional area (in m²): "))
    inner_value_c = (1/2)*density*cross_sectional_area*drag_constant
    velocity = math.sqrt((mass*gravity)/inner_value_c)*(1 - math.exp ((- math.sqrt(mass * gravity * inner_value_c) / mass) * time))
    print(f"\nThe inner value of c is: {inner_value_c:.3f}")
    print(f"The velocity after {time} seconds is: {velocity:.3f} m/s")

if gravity == 9.8 :
    velocity_jupiter = math.sqrt((mass * 24)/inner_value_c)*(1 - math.exp ((- math.sqrt(mass * 24 * inner_value_c) / mass) * time))
    difference_jupiter = velocity_jupiter - velocity
    print(f"The difference between Earth and Jupiter gravities is: {difference_jupiter:.3f} ")
else :
    velocity_earth = math.sqrt((mass * 9.8)/inner_value_c)*(1 - math.exp ((- math.sqrt(mass * 9.8 * inner_value_c) / mass) * time))
    difference_earth =  velocity - velocity_earth
    print(f"The difference between Jupiter and Earth gravities is: {difference_earth:.3f} ")
    
velocity_terminal = math.sqrt((mass*gravity)/inner_value_c)
print(f"The Terminal Velocity is: {velocity_terminal:.3f}")



