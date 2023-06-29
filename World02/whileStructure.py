# Working with while --------------------------------------------------------------------------------------------
# import random;

# num = 0;
# numComputer = random.randint(1,5);

# while num != numComputer:
#     num = int(input('Guess the number: '));
# print('You Won');



# # Challenger 57 -------------------------------------------------------------------------------------------------
# sexPerson = '';

# while sexPerson != 'm' and sexPerson != 'f':
#     sexPerson = str(input('Write your sex [M/F]: ')).lower();
    
#     if sexPerson == 'm' or sexPerson == 'f':
#         print('OK');
        
#     else: 
#         print('Please, try again!');


# # Challenger 58 -------------------------------------------------------------------------------------------------
# from random import randint;

# numberComputer = randint(0,10);
# numberPerson = 0;
# count = 0;

# while numberPerson != numberComputer:
#     numberPerson = int(input('Guess the number: '));
    
#     if numberPerson == numberComputer:
#         print('You are right! The number was {0}\nYou writed {1} times to won'.format(numberComputer, count));
        
#     else:
#         print('Try again!');
#         count += 1;


# # Challenger 59 -------------------------------------------------------------------------------------------------
# num1 = int(input('Write the first number: '));
# num2 = int(input('Write the second number: '));
# option = 0;

# while option != 5:
#     print('\n----- Menu -----');
#     print('[1] Add\n[2]multiply\n[3]greater value\n[4]new numbers\n[5]exit program\n');
#     option = int(input('Select a option: '));
    
#     if option == 1:
#         add = num1 + num2;
#         print('{0} + {1} = {2}'.format(num1, num2, add));
        
#         newOption = str(input('Are you want to continue? [S/N]')).lower();
#         if newOption == 'n':
#             break;
    
#     elif option == 2:
#         mult = num1 * num2;
#         print('{0} * {1} = {2}'.format(num1, num2, mult));
        
#         newOption = str(input('Are you want to continue? [S/N]')).lower();
#         if newOption == 'n':
#             break;
        
#     elif option == 3:
#         if num1 > num2:
#             print('The bigger number is {0}'.format(num1));
            
#             newOption = str(input('Are you want to continue? [S/N]')).lower();
#             if newOption == 'n':
#                 break;
#         else:
#             print('The bigger number is {0}'.format(num2));
            
#             newOption = str(input('Are you want to continue? [S/N]')).lower();
#             if newOption == 'n':
#                 break;
        
#     else:
#         num1 = int(input('Write the new first number: '));
#         num2 = int(input('Write the new second number: '));
        
#         newOption = str(input('Are you want to continue? [S/N]')).lower();
#         if newOption == 'n':
#                 break;


# # Challenger 60 -------------------------------------------------------------------------------------------------
# import math;

# numb = int(input('Write some number: '));
# count = numb;

# while count > 0:
#     print('{0}'.format(count), end='');
#     print(' x ' if count > 1 else ' = ', end='');
#     count -= 1
    
# print(math.factorial(numb), end='');


# # Challenger 61 -------------------------------------------------------------------------------------------------
# print('--- Arithmetic Progression---');

# beginNumber = int(input('Write the beginner number: '));
# jumpNumber = int(input('Write the jump between the numbers: '));
# count = 1;

# while count <= 10:
#     print('{0}'.format(beginNumber), end=' ');
#     beginNumber += jumpNumber;
#     count += 1;
# print('\nThe end!');


# Challenger 62 -------------------------------------------------------------------------------------------------


# Challenger 63 -------------------------------------------------------------------------------------------------


# Challenger 64 -------------------------------------------------------------------------------------------------


# Challenger 65 -------------------------------------------------------------------------------------------------
