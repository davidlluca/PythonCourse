# Testing conditions -----------------------------------------------------------------------------------------------
# if : | else :
# age = int(input('How old are u? '));
# if age < 21 :
#     print('You are young!');
# else: 
#     print('You are an adult');



# Challenger 28 -------------------------------------------------------------------------------------------------
import random;
from time import sleep;

numberRand = random.randint(0,5);
numberWrit = int(input('Guess the computer number: '));
print('loading...');
sleep(2);

if numberWrit == numberRand:
    print('You are right! You won.');
else:
    print('The correct number is {0}! You lost.'.format(numberRand));


# Challenger 29 -------------------------------------------------------------------------------------------------
numberLimit = int(input('Write the velocity in KM: '));
tax = (numberLimit - 80) * 7;

if numberLimit <= 80.0:
    print('You are OK');
else:
    print('You are above the limit! However you will be charged!\nThe tax will be ${0}'.format(tax));


# Challenger 30 -------------------------------------------------------------------------------------------------
number = int(input('Write a number: '));
result = number % 2;

if result == 0:
    print('The number {0} is par!'.format(number));
else:
    print('The number {0} is odd!'.format(number));


# Challenger 31 -------------------------------------------------------------------------------------------------
distance = int(input('Write in KM, what is the distance of the trip? '));

if distance <= 200:
    price = 0.50;
    print('The price of the trip will be ${0}'.format(distance * price));
else:
    price = 0.45;
    print('The price of the trip will be {0}'.format(distance * price));


# Challenger 32 -------------------------------------------------------------------------------------------------
from datetime import date;
year = int(input('Write some year or write 0 for the current year: '));

if year == 0:
    year = date.today().year;

if year % 4 == 0 and year % 100 != 0 or 400 == 0:
    print('{0} is a leap year!'.format(year));
else:
    print('{0} is not a leap year!'.format(year));


# Challenger 33 -------------------------------------------------------------------------------------------------
numbers = [int(input('Write the first number: ')), int(input('Write the second number: ')), int(input('Write the third number: '))];

# checking the smallest number
smaller = numbers[0];
if numbers[1] < numbers[0] and numbers[1] < numbers[2]:
    smaller = numbers[1];
if numbers[2] < numbers[0] and numbers[2] < numbers[1]:
    smaller = numbers[2];
    
# checking the highest number
higher = numbers[0];
if numbers[1] > numbers[0] and numbers[1] > numbers[2]:
    higher = numbers[1];
if numbers[2] > numbers[0] and numbers[2] > numbers[1]:
    higher = numbers[2];
    
print('\nThe smaller number is {0}\nThe higher number is {1}'.format(smaller, higher));


# Challenger 34 -------------------------------------------------------------------------------------------------
wage = float(input('Write your wage for month: '));

if wage <= 1250:
    print('The increase is 15 percent in your wage, now you earn: ${0:.2f}'.format((wage * 0.15) + wage));
else:
    print('The increase is 10 percent in your wage, now you earn: ${0:.2f}'.format((wage * 0.10) + wage));


# Challenger 35 -------------------------------------------------------------------------------------------------
numbers = [float(input('Write the first number: ')), float(input('Write the second number: ')), float(input('Write the third number: '))];

if numbers[0] < numbers[1] + numbers[2] and numbers[1] < numbers[0] + numbers[2] and numbers[2] < numbers[0] + numbers[1]:
    print('you can form a triangle with these three numbers!');
else:
    print('You cannot form a triangle with these three numbers!');