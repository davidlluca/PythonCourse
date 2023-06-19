# Working with repeating struture 
# for 'variable_name' in range():
# (0,0,0) '1' - begin | '2' - end | '3' - jump


# # Test 1
# begin = int(input('Write the begin: '));
# end = int(input('Write the end: '));
# jump = int(input('Write the jump: '));

# for test in range(begin, end + 1, jump):
#     print(test);


# # Test 2   
# from random import randint;

# computerNumber = randint(0,5);

# for guess in range(0,3):
#     personNumber = int(input('Try guess the computer number: '));
    
#     if personNumber == computerNumber:
#         print('You are right!');
#     else:
#         print('You lose!');



# # Challenger 46 ------------------------------------------------------------------------------------------------
# from time import sleep;

# for count in range(10,0, -1):
#     print('{0}!'.format(count));
#     sleep(1);
    
# print('Happy New Year!');


# # Challenger 47 -------------------------------------------------------------------------------------------------
# for evenNumber in range(1,51):
#     if evenNumber % 2 == 0:
#         print(evenNumber);
        
# print('The end!');


# # Challenger 48 -------------------------------------------------------------------------------------------------
# sum = 0;
# count = 0;

# for numbersCalc in range(1,501, 2):
#     if numbersCalc % 3 == 0:
#         sum = sum + numbersCalc;
#         count = count + 1;
        
# print('The sum between the {0} numbers is {1}'.format(count, sum));


# # Challenger 49 -------------------------------------------------------------------------------------------------
# count = 0;
# result = 0;
# number = int(input('Write a number: '));

# for numbersTab in range(0,10):
#     count = count + 1;
#     result = number * count;
#     print('{0}x{1} = {2}'.format(number, count, result));


# # Challenger 50 -------------------------------------------------------------------------------------------------
# sum = 0;

# for numbers in range(0,6):
#     randomNumbers = int(input('Write some number: '));
#     if randomNumbers % 2 == 0:
#         sum = sum + randomNumbers;
        
# print('The sum of the even numbers is {0}'.format(sum));


# # Challenger 51 -------------------------------------------------------------------------------------------------
# print('--- Arithmetic Progression---');

# beginNumber = int(input('Write the first number: '));
# jumpNumber = int(input('Write the jump between the number: '));
# finalNumber = beginNumber + (10 - 1) * jumpNumber

# for pa in range(beginNumber, finalNumber, jumpNumber):
#     print('{0}'.format(pa), end=' ');


# Challenger 52 -------------------------------------------------------------------------------------------------

# Challenger 53 -------------------------------------------------------------------------------------------------

# Challenger 54 -------------------------------------------------------------------------------------------------

# Challenger 55 -------------------------------------------------------------------------------------------------

# Challenger 56 -------------------------------------------------------------------------------------------------;