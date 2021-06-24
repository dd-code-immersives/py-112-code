

cars = ['Ford','Tesla','Mercedes']
for i,car in enumerate(cars):
    print(f'index = {i} and the element is {car} or {cars[i]}')

cars = ['Ford','Tesla','Mercedes']
cars[1] = 'Kia'  # Tesla overridden with Kia
print(cars)

cars = ['Ford','Tesla','Mercedes']
pos = cars.index('Mercedes')
print(f'The car named Mercedes can be found at position {pos}')

cars = ['Ford','Tesla','Mercedes']
if cars.count('Toyota') > 0:
    pos = cars.index('Toyota')   # Would produce an error because it is not in the list
else:
    print(f'Toyota is not in the list')









