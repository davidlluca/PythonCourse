# Working with imports

# Challenger 16 -------------------------------------------------------------------------------------------------
from math import ceil;
randomNum = float(input('Write a float number: '));

print('The number is {0}, his all part is {1}'.format(randomNum, ceil(randomNum)));


# Challenger 17 -------------------------------------------------------------------------------------------------
from math import sqrt, pow;

cat1 = float(input('Write a c1 value: '));
cat2 = float(input('Write a c2 value: '));
hip = pow(2, cat1) + pow(2, cat2);

print('\nH² = {0}² + {1}²\nThe value of the hypotenuse is {2:.2f}'.format(cat1, cat2, sqrt(hip)));


# Challenger 18 -------------------------------------------------------------------------------------------------
import math;
angle = float(input('Write an angle: '));

print('\nSine: {0:.2f}\nCosine: {1:.2f}\nTangent: {2:.2f}\n'.format(math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan(math.radians(angle))));


# Challenger 19 -------------------------------------------------------------------------------------------------
from random import choice;

namesStudents = [input('Write the student 1: '), input('Write the student 2: '), input('Write the student 3: '), input('Write the student 4: ',)];

print('The student chosen was {0}'.format(choice(namesStudents)));


# Challenger 20 -------------------------------------------------------------------------------------------------
from random import sample, shuffle;
names = [input('First student: '), input('Second student: '), input('Third student: '), input('Fouth student: ')]

#With shuffle
shuffle(names);
print('\nThe order of presentation will be: {0}'.format(names));

#with sample
# randomSeq = sample(names, len(names));
# print('\nThe order of presentation will be: ')
# for nome in randomSeq:
#     print(nome);