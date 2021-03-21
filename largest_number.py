number0 = int(input('Input number : '))
number = number0
largest_dig = 0
while number > 0:
    remain = number % 10
    if remain > largest_dig:
        largest_dig = remain
    number //=10
print(f"largest digit in number {number0} is {largest_dig}")