# Operators arithmetic
# + : add
# - : subtraction
# * : multiplication
# / : division
# ** : power
# // : rest of div
# % : whole of div

# Testing ------------------------------------------------------------------------------------------------------
firstNumber = int(input('Write some number: '));
secondNumber = int(input('Write another number: '));

add = firstNumber + secondNumber;
sub = firstNumber - secondNumber;
mult = firstNumber * secondNumber;
div = firstNumber / secondNumber;
pwr = firstNumber ** secondNumber
restDiv = firstNumber // secondNumber;
wholeDiv = firstNumber % secondNumber;

print('The add is {0}\n The sub is {1}\n The mult is {2}\n The div is {3:.2f}\n The power is {4}\n The rest of div is {5}\n The whole div is {6}'.format(add, sub, mult, div, pwr, restDiv, wholeDiv));


# Challenger 05 -------------------------------------------------------------------------------------------------
num = int(input('Write a number: '));
print('Before: {0}, Him: {1}, After: {2}'.format(num-1, num, num+1));


# Challenger 06 -------------------------------------------------------------------------------------------------
# import math;
from math import sqrt;
num02 = int(input('Write a number: '));
print('Double: {0}, Triple: {1}, Square root: {2:.2f}'.format(num02*2, num02*3, sqrt(num02)));
 
 
# Challenger 07 -------------------------------------------------------------------------------------------------
firstGrade = float(input('Write a grade of the student: '));
secondGrade = float(input('Write another grade of the student: '));

print('The average grade of the student is {}'.format((firstGrade+secondGrade) / 2));


# Challenger 08 -------------------------------------------------------------------------------------------------
numMeter = int(input('Write a number in meters: '))

print('\nIn meters is {0}\n In centimeters is: {1}\n In milliliters is: {2}'.format(numMeter, numMeter*100, numMeter*1000));


# Challenger 09 -------------------------------------------------------------------------------------------------
numberTab = int(input('Write a number: '));
print('\n{0} x 1 = {1}\n {2} x 2 = {3}\n {4} x 3 = {5}\n {6} x 4 = {7}\n {8} x 5 = {9}'.format(numberTab, numberTab*1, numberTab, numberTab*2, numberTab, numberTab*3, numberTab, numberTab*4, numberTab, numberTab*5));


# Challenger 10 -------------------------------------------------------------------------------------------------
dollar = 3.27;
personCash = float(input('How much money do you have? '));

print('You can buy {:.2f} dollars'.format(personCash/dollar));


# Challenger 11 -------------------------------------------------------------------------------------------------
height = float(input('Write the height of the wall: '));
width = float(input('Write the width of the wall: '));

areaWall = height * width;
paint = 2;

print('The total area of the wall is {0:.2f}, we need {1:.2f}m² of the ink to paint all of them'.format(areaWall, areaWall/paint));


# Challenger 12 -------------------------------------------------------------------------------------------------
priceProduct = float(input('Write the products price: $'));
discount = 0.5;

print('The original price is ${0}, with 5 percent of discount, the new price is ${1}'.format(priceProduct, priceProduct * discount));


# Challenger 13 -------------------------------------------------------------------------------------------------
personWage = float(input('Write your wage for month: $'));
increase = personWage * 0.15;

print('Your wage is ${0}, with 15 percent of increase, your new wage is ${1}'.format(personWage, personWage + increase));