a = float(input('Input start distance (km) = '))
b = float(input('Input target distance (km) = '))
day = 1
print(f'{day}\'th day : {a} km')
while a <= b:
    a = a * 1.1
    day += 1
    print(f'{day}\'th day : {round(a, 2)} km')
print(f'{day}\'th day runner reach at least {b} km')
