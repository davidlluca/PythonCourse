# Method Cut
# sentence([0:0:0]): some sentence that you want to cut -- example: --'begin'-'end'-'jump'--

# Method Analyze ---------------------------------------------------------------------------
# len(): size of the sentence -- len(sentence);
# count('',0,0): will couting something -- sentence.count('a');
# find(): how many times find something -- sentence.find('vid');
# 'something' in variable_name: returns true or false if it that exists

# Method Tranformation ---------------------------------------------------------------------
# replace(): will replace one sentence with another one -- sentence.replace('Andrade', 'Pereira');
# upper(): transform the sentence in uppercase -- sentence.upper()
# lower(): transform the sentence in lowercase -- sentence.lower()
# capitalize(): in a sentence only the first letter is capitalized -- sentence.capitalize()
# tittle(): after a period, the title will make a word break -- sentence.title()
# strip(): ignore unnecessary spaces | rstrip - begin right | lstrip - begin left

# Division / Join --------------------------------------------------------------------------
# split(): split(division) the sentence on each space
# ''.join(): will join the all sentence, example: '-'.join(sentence);



# Challenger 22 -------------------------------------------------------------------------------------------------
namePerson = input('Write your name complete: ');
divison = namePerson.split();

print(namePerson.upper());
print(namePerson.lower());
print(len(namePerson.strip()))
print(len(divison[0]));


# Challenger 23 -------------------------------------------------------------------------------------------------
number = int(input('Write a number between 0 and 9999: '));

uniNumber = number % 10;
tenNumber = (number // 10) % 10;
hundrNumber = (number // 100) % 10;
thounNumber = (number // 1000) % 10;

print('\nThe number is {0}\nUnit: {1}\nTen: {2}\nHundred: {3}\nThousand: {4}'.format(number, uniNumber, tenNumber, hundrNumber, thounNumber));


# Challenger 24 -------------------------------------------------------------------------------------------------
nameCity = input('Whats the name of our city? ').strip();
nameDiv = nameCity.split();
print('SANTO' in nameDiv[0].upper());


# Challenger 25 -------------------------------------------------------------------------------------------------
namePerson = input('Write your name here: ');
print('SILVA' in namePerson.upper());


# Challenger 26 -------------------------------------------------------------------------------------------------
sentence = input('Write something here: ').lower().sprit();

print('Word A: {0}'.format(sentence.count('a')));
print('First time: {0}'.format(sentence.find('a')+1));
print('The last time: {0}'.format(sentence.rfind('a')+1));


# Challenger 27 -------------------------------------------------------------------------------------------------
namePerson = input('Write your name: ');
nameDiv = namePerson.split();

print('First name: {0}\nLast name: {1}'.format(nameDiv[0], nameDiv[-1]));