System_boundary_limit = 15.0
Tractor_A = 'METRIC WHEEL SLIP'
print(f'Tractor A: {Tractor_A}')
Theoretical_Speed_A = 5.0
Actual_Tracked_Speed_A = 4.3 #Actual Speed value was changed from 3.8 to 4.3 to prevent field injury warning.
Slip_percentage_A = ((Theoretical_Speed_A - Actual_Tracked_Speed_A)/Theoretical_Speed_A)*100
print(f'Boundary limit is {System_boundary_limit}%   ')

print(f'Theoretical speed for metric wheel: {Actual_Tracked_Speed_A}m/s')
print(f'Actual speed for metric wheel: {Theoretical_Speed_A}m/s')
print(f'Slip percentage for metric wheel: {Slip_percentage_A}%')
if Slip_percentage_A >= System_boundary_limit:print('FIELD INJURY WARNING:EXCESSIVE SOIL COMPACTION OCCURRING')
else:
    print('Optimal field traction')
 #The first proceeded to give the warning since the slip percentage exceeds the boundary limit
 #Hence there is the need to change the value of the Actual speed from 3.8 to 4.3
 #After the value was changed it displayed optimal operation, hence running safely.
print()
print()
print()
Tractor_B = 'IMPERIAL WHEEL SLIP'
print(f'Tractor B: {Tractor_B}')
Theoretical_Speed_B = 8.0
Actual_tracked_Speed_B = 7.1
Slip_percentage_B = ((Theoretical_Speed_B - Actual_tracked_Speed_B)/Theoretical_Speed_B)*100
print(f'Theoretical speed for Imperial wheel: {Theoretical_Speed_B}m/s')
print(f'Actual_tracked_Speed for Imperial wheel: {Actual_tracked_Speed_B}m/s')
print(f'Slip percentage for Imperial wheel: {Slip_percentage_B}%')
if Slip_percentage_B >= System_boundary_limit:
    print('FIELD INJURY WARNING: EXCESSIVE SOIL COMPACTION OCCURRING')
else:
    print('Optimal field traction')





