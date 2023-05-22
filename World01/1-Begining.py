# Perfil test -------------------------------------------------------------------------------------------------
name = input('What is your name?');
age = input('How old are you?');

print('Hi {0}, you are {1} years old'.format(name, age));



# Challenger 01 -------------------------------------------------------------------------------------------------
name02 = input('What is your name?');
print('Welcome {}!'.format(name02));


# Challenger 02
day = input('Write the day: ');
month = input('Write the month: ');
year = input('Write the year: ');

print('The date is: {0}/{1}/{2}'.format(day,month,year));


# Challenger 03 -------------------------------------------------------------------------------------------------
numbers = [int(input('Write a number: ')), int(input('Write another number: '))]
add = sum(numbers);


print('The add between {0} + {1} is {2}'.format(numbers[0],numbers[1],add));


# Challenger 04 -------------------------------------------------------------------------------------------------
something = input('Write something: ');
print('You writed: {0}\n Is this type is string? {1}\n Is this type is numeric? {2}'.format(something, something.isalpha(), something.isnumeric()));