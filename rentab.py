proseeds = float(input('Input company\'s income : '))
cost = float(input('Input company\'s expenses : '))
if proseeds > cost:
    profit = proseeds - cost
    eff = profit / proseeds
    print(f'company\'s profit is : {profit}')
    print(f'company\'s rentb is : {eff}')
    n = int(input('Input how many emploee\'s working in company : '))
    profit_n = profit / n
    print(f'profit per emploee is : {profit_n}')
elif cost > proseeds:
    loss = cost - proseeds
    print(f'Company is out for : {loss}')
