System_boundary_limit = 4.0
Option_A = "Metric reactor system"
Volumetric_flow_rates_A = float(1800.0)
Reactor_Volume_A = float(500.0)
Space_Velocity_A = float(Volumetric_flow_rates_A / Reactor_Volume_A)
print(Option_A)
print(f'Space_Velocity for metric system: {Space_Velocity_A}', "hours")
print(f'Reactor Volume for metric system: {Reactor_Volume_A}', "Litre")
print(f'Volumetric flow rate for metric system: {Volumetric_flow_rates_A}', 'Litres/hours')
print(f'Space Velocity: {Space_Velocity_A}', ' per hour')
if Space_Velocity_A < System_boundary_limit:print(f"Condition for metric system: Normal condition")
else:print("Condition for metric system: WARNING!!! RUNNING TOO FAST")
# The Metric reactor system is in normal condition since it printed normal condition.

Option_B = "Imperial reactor system"
# After Imperial reactor system was altered.
# Change the volumetric flow rate from 8.5 to 7.0
Volumetric_flow_rates_B = float(7.0)
Reactor_Volume_B = float(110.0)
Space_Velocity_B = float(Volumetric_flow_rates_B / Reactor_Volume_B)*60
print()
print()
print(Option_B)
print(f"Reactor Volume for Imperial reactor system: {Reactor_Volume_B} Gallons")
print(f"Volumetric flow rate for Imperial reactor system: {Volumetric_flow_rates_B} Gallons/minutes")
print(f"Space Velocity for Imperial reactor system: {Space_Velocity_B} per minute")
if Space_Velocity_B <= System_boundary_limit:
   print(f"Condition for Imperial System: Running Normal")
else:
    print(f"Condition for Imperial System: WARNING!!! RUNNING TOO FAST")
#After the imperial reactor system was altered it returned to normal condition.
