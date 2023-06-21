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


# # Challenger 52 -------------------------------------------------------------------------------------------------
# number = int(input('Write some number: '));
# total = 0;

# for csNumber in range(1, number + 1):
#     if number % csNumber == 0:
#         total += 1;
#         print('\033[31m{0}\033[m'.format(csNumber), end=' ');
        
#     else:
#         print('{0}'.format(csNumber), end=' ');
        
# if total == 2:
#     print('\nThis number is a prime number!');
# else:
#     print('\nThis number is not a prime number. It was divided {0} times'.format(total));


# # Challenger 53 -------------------------------------------------------------------------------------------------
# sentence = str(input('Write something random: ')).strip().upper();
# word = sentence.split();
# tgther = ''.join(word)
# inverse = '';

# for newSentence in range(len(tgther) - 1, -1, -1):
#     inverse += tgther[newSentence];
    
# if inverse == tgther:
#     print('{0} {1}\n{2}It is a palindrome!{3}'.format(tgther, inverse, '\033[32m', '\033[m'));
# else:
#     print('{0} {1}\n{2}This sentence is not a palindrome{3}'.format(tgther, inverse, '\033[31m', '\033[m'));


# # Challenger 54 -------------------------------------------------------------------------------------------------
# from datetime import date;

# count = 0;
# count2 = 0;

# for birthday in range(0,7):
#     btPerson = int(input('Write the year you were born: '));
#     age = date.today().year - btPerson;

#     if age >= 21:
#         count += 1;
        
#     else:
#         count2 += 1;
    
# print('\n{0} {1}have reached{2} the age of majority'.format(count, '\033[32m', '\033[m'));
# print('{0} {1}have not reached{2} the age of majority yet'.format(count2, '\033[31m', '\033[m')); 


# # Challenger 55 -------------------------------------------------------------------------------------------------
# bigger = 0;
# smaller = 0;

# for weight in range(1,6):
#     wgPerson = float(input('write the person weight: '));
    
#     if weight == 1:
#         bigger = wgPerson;
#         smaller = wgPerson;
#     else: 
#         if wgPerson > bigger:
#             bigger = wgPerson;
            
#         if wgPerson < smaller:
#             smaller = wgPerson;

# print('The biggest person weight is {0}'.format(bigger));
# print('The smmalest person weight is {0}'.format(smaller));


# Challenger 56 -------------------------------------------------------------------------------------------------


