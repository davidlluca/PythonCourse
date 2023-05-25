colors = {'clear':'\033[m',
          'white':'\033[30m',
          'red':'\033[31m',
          'green':'\033[32m',
          'yellow':'\033[33m',
          'blue':'\033[34m',
          'purple':'\033[35m',
          'cyan':'\033[36m',
          'gray':'\033[37m'}


# Perfil test -------------------------------------------------------------------------------------------------
name = input('What is your name?');
age = input('How old are you?');

print('Hi {0}{1}{2}, you are {3} years old'.format(colors['blue'], name, colors['clear'], age));


# Challenger 01 -------------------------------------------------------------------------------------------------
name02 = input('What is your name?');
print('Welcome {}{}{}!'.format('\033[33m', name02, '\033['));


# Challenger 02 -------------------------------------------------------------------------------------------------
day = input('Write the day: ');
month = input('Write the month: ');
year = input('Write the year: ');

print('The date is: {0}{1}/{2}/{3}{4}'.format(colors['yellow'],day,month,year, colors['clear']));


# Challenger 03 -------------------------------------------------------------------------------------------------
numbers = [int(input('Write a number: ')), int(input('Write another number: '))]
add = sum(numbers);

print('The add between {0} + {1} is {2}{3}{4}'.format(numbers[0],numbers[1], colors['green'], add, colors['clear']));


# Challenger 04 -------------------------------------------------------------------------------------------------
something = input('Write something: ');
print('You writed: {0}{1}{2}\n Is this type is string? {3}\n Is this type is numeric? {4}'.format(colors['purple'],something, colors['clear'], something.isalpha(), something.isnumeric()));