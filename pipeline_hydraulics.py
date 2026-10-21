System_Boundary_limit = 3.0
print(f'Critical Velocity Cap: {System_Boundary_limit} m/s')
Option_A = 'Standard Volumetric Metric Approach'
Volumetric_Flow_Rate_A = 0.28
Pipe_Cross_Sectional_Area_A = 0.08
Velocity_A = Volumetric_Flow_Rate_A/ Pipe_Cross_Sectional_Area_A
print(Option_A)
print(f'Volumetric Flow Rate: {Volumetric_Flow_Rate_A} m^3/s')
print(f'Pipe_Cross_Sectional_Area: {Pipe_Cross_Sectional_Area_A} m^2')
print(f'Velocity_A: {Velocity_A} m/s')
if Velocity_A >= System_Boundary_limit:
    print('CONDITION: WARNING!!! INTENSE KINETIC PRESSURE SPIKE')
else:
    print('CONDITION: OPTIMAL OPERATION')


print()

print()
Option_B = 'Scaled Industrial Litres Millimetres Approach'
Volumetric_Flow_Rate_B = 42.0
Pipe_Cross_Sectional_Area_B = 15000.0
Velocity_B = (Volumetric_Flow_Rate_B / Pipe_Cross_Sectional_Area_B)*1000
print(Option_B)
print(f'Volumetric Flow Rate for Imperial System: {Volumetric_Flow_Rate_B}Litres/Second')
print(f'Pipe_Cross_Sectional_Area for Imperial System: {Pipe_Cross_Sectional_Area_B}mm^2')
print(f'Velocity_B: {Velocity_B}m/s')
if Velocity_B >= System_Boundary_limit:
    print('CONDITION: WARNING!!! INTENSE KINETIC PRESSURE SPIKE')
else:
    print('CONDITION: OPTIMAL OPERATION')