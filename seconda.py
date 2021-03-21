time = int(input('Input time in second\'s : '))
seconds = time
minutes = seconds // 60
hours = minutes // 60
print(f'Time is equal : {hours:02d}:{minutes % 60:02d}:{seconds % 60:02}')
