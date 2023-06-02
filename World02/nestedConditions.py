#  Working with nested conditions ----------------------------------------------------------------------------------
# if: | elif: | else:

# age = int(input('Whats is your age? '));

# if age >= 18:
#     print('You are {0}, you can work in Brazil!'.format(age));
# elif age >= 16 and age < 18:
#     print('You are {0}, but you cannot work at night in Brazil!'.format(age));
# elif age >= 14 and age < 16:
#     print('You are {0}, but you can work only 6 hours in Brazil!'.format(age));
# else:
#     print('You are {0}, you cannot work in Brazil!'.format(age));



# # Challenger 36 -------------------------------------------------------------------------------------------------
# housePrice = float(input('What is the price of the house? $'));
# personWage = float(input('What is your wage? $'));
# years = int(input('How many years you can pay? '));

# months = years * 12;
# installments = housePrice / months;

# if installments > personWage * 0.3:
#     print('The installments price is {0:.2f}, you cannot pay for that!'.format(installments));
# else: 
#     print('The installments price is {0:.2f}, you can pay for that!'.format(installments));


# # Challenger 37 -------------------------------------------------------------------------------------------------
# import math;
# number = int(input('Write some number: '));

# print('\n--- Choose an option ---');
# choose = int(input('(1) - binary\n(2) - octal\n(3) - hexadecimal\n'));

# if choose == 1:
#     bin = bin(number);
#     print('The number in binary: {0}'.format(bin[2:]));
    
# elif choose == 2:
#     oct = oct(number);
#     print('The number in octal: {0}'.format(oct[2:]));
    
# else:
#     hex = hex(number);
#     print('The number in hexadecimal: {0}'.format(hex[2:]));


# # Challenger 38 -------------------------------------------------------------------------------------------------
# value1 = int(input('Write the first number: '));
# value2 = int(input('Write the second number: '));

# if value1 > value2:
#     print('The first number "{0}" is bigger than the second number "{1}"'.format(value1, value2));
# elif value1 < value2:
#     print('The second number "{0}" is bigger than the first number "{1}"'.format(value2, value1));
# else:
#     print('The numbers are the same!');


# # Challenger 39 -------------------------------------------------------------------------------------------------
# from datetime import date;
# colors = {'clean':'\033[m','red':'\033[31m', 'green':'\033[32m', 'yellow':'\033[33m'};

# personBirthday = int(input('Write your date of birth: '));
# age = date.today().year - personBirthday;

# if age == 18:
#     print('You are {0}, {1}now you can enlist!{2}'.format(age, colors['green'], colors['clean']));
# elif age > 18:
#     print('You are {0}. {1}It is past time for you to enlist!{2}. {3} years have passed'.format(age, colors['red'], colors['clean'], age - 18));
# else:
#     print('You are {0}, {1}you cannot enlist yet!{2}. {3} years left'.format(age, colors['yellow'], colors['clean'], 18 - age));


# # Challenger 40 -------------------------------------------------------------------------------------------------
# firstGrade = float(input('Write the frist grade of the student: '));
# secondGrade = float(input('Write the second grade of the studen: '));
# finalGrade = (firstGrade + secondGrade) / 2;

# if finalGrade < 5.0:
#     print('The final student grade is {0:.2f}, you failed!'.format(finalGrade));
# elif finalGrade >= 5.0 and finalGrade <= 6.9:
#     print('The final student grade is {0:.2f}, you are recovering!'.format(finalGrade));
# else:
#     print('The final student grade is {0:.2f}, you passed!'.format(finalGrade));


# # Challenger 41 -------------------------------------------------------------------------------------------------
# athleteAge = int(input('Whats the athletes age? '));

# if athleteAge <= 9:
#     print('Your category is: First Junior');
    
# elif athleteAge > 9 and athleteAge <= 14:
#     print('Your category is: Child');
    
# elif athleteAge > 14 and athleteAge <= 19:
#     print('Your category is: Second Junior');
    
# elif athleteAge == 20:
#     print('Your category is: Senior');
    
# else:
#     print('Your category is: Master');


# # Challenger 42 -------------------------------------------------------------------------------------------------
# side1 = int(input('Write the number of the side1: '));
# side2 = int(input('Write the number of the side2: '));
# side3 = int(input('Write the number of the side3: '));

# if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
#     print('\nYou can do a triangle with these sides!');
    
#     if side1 == side2 and side1 == side3:
#         print('An equilateral triangle!\n');
#     elif side1 != side2 and side1 != side3:
#         print('A scalene triangle!\n');
#     else: 
#         print('An isocellar triangle!\n');
# else:
#     print('You cannot do a tiangle with these sides!');


# Challenger 43 -------------------------------------------------------------------------------------------------


# Challenger 44 -------------------------------------------------------------------------------------------------


# Challenger 45 -------------------------------------------------------------------------------------------------