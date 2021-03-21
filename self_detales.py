print('Hello, lets\'s start')
ans = 'y'
while ans == 'y' :
    self_first_name = input('please input your Firstname : ')
    self_sure_name = input('please input your Surename : ')
    self_age = int(input('please input your age : '))
    print('*************************************************************')
    print('* Thank you for you time Mr.', self_first_name, self_sure_name)
    print('*************************************************************')
    # Форматирование через %
    print('* Format by %(arg)')
    print('-------------------------------------------------------------')
    print('* you  name is %s' % self_first_name)
    print('* your surename is %s' % self_sure_name)
    print('* you age is %d' % self_age)
    print('**************************************************************')
    print('%5s %25s %20s' % ('First name', 'Last name', 'Age'))
    print("%5s %25s %20d" % (self_first_name, self_sure_name, self_age))
    print('**************************************************************')
    # форматирование через Format{:>20}
    print('* Format by {:>20}')
    print('*-------------------------------------------------------------')
    print('You first name is  {}'.format(self_first_name))
    print('You sure name is  {}'.format(self_sure_name))
    print('You age name is  {}'.format(self_age))
    print('{:>5} {:>25} {:>25}'.format('first name', 'Last name', 'Age'))
    print('{:>5} {:>25} {:>25}'.format(self_first_name, self_sure_name, self_age))
    print('**************************************************************')
    print('* Format by f{}')
    print('*-------------------------------------------------------------')
    message = f'Hi {self_first_name} '\
              f'{self_sure_name} '\
              f'you age is {self_age}.'
    print(message)
    print('*-------------------------------------------------------------')
    print(f'Your first name is : {self_first_name}')
    print(f'You sure name is : {self_sure_name}')
    print(f'Your age is : {self_age}')
    print('*-------------------------------------------------------------')
    ans = input('If you want to continue press "y" or  any other key for exit : ')


else :
    print('*********************')
    print('*                   *')
    print('*    Good bye       *')
    print('*                   *')
    print('*********************')
