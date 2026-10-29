print ("hello world")
print ('My favourite people are', 'my dad', 'mom', 'and siblings')
my_integer_var = 45
print('Integer:', my_integer_var)
my_float_var = 5.8
print('Float:', my_float_var)
my_string_var = 'Just a girl'
print('String:', my_string_var)
my_Boolean_var = True or False
print('Boolean', my_Boolean_var)
print(type(my_Boolean_var));
print(type(my_float_var));
print(type(my_string_var));
print(isinstance(my_Boolean_var, (int, float)));

# The first trial
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float))
print(score, type(score))

msg = 'It\'s a sunny day'
momo = "she said \"she is happy\""

lolo = "Hello my love"
print(len(lolo))
print("Hello" in lolo)
print(lolo[0])
print(lolo[-2])

# string concatenation
years = 20
color = 'Green'
together = str(years) + ' ' + color
print (together)

#string interpolation
Name = "Ama"
Age = 40
Together = f'My name is {Name} and I\'m {Age} years old'
print(Together)

first = 34
second = 23
both = f'The sum of {first} and {second} is {first + second}'
print(both)

# String slicing
gogo = "Hello my world"
print(gogo[1:4]);
print(gogo[0:9:2]);
print(gogo[-1]);
print(gogo[:5]);
print(gogo[::2]);
print(gogo[2:]);

print(gogo.upper());
print(gogo.lower());
print(gogo.replace("Hello", "Hi"));
print(gogo.title());
print(gogo.capitalize());
print(gogo.count('o'));
print(gogo.startswith('Hello'));
print(gogo.endswith('world'));
print(gogo.isupper());
print(gogo.islower());

# numbers and Math operations
num = 5.675
num_2 = 34
print(int(num))
print(float(num_2))
print(pow(6,3))
pow(6, 3, 4)
print(abs(num)) # 2 ** 3 % 4
print(round(num, 2))
print(round(num))

#augumented form
count = 23
count += 2
count -= 3
count **= 4
yeye = 'Hello'
yeye += ' world'
print(yeye)

# conditional statements and Comparison
print(3 > 4)
print (3 == 4)
print(5!=6)

age = 56
if age >= 80:
    print('Grade: A you\'ve done well')
elif age >= 60:
    print('Grade: B you tried')
elif age >= 40:
    print('Grade: C Try harder next time')
elif age >= 20:
    print('Grade: F you don\'t learn?')
else:
    print('pack your bags and go yy')

    # falsy values = 0, 0.0, false, " "
print(bool(" "))
print(bool(False))
print(bool(0))
print(bool(0.0))

age = 25
is_student = True
if age >= 18 and is_student:
    print('Oh guy you are an adult now')
else:
    print('you are such a baby')

if age >= 18 or is_student:
    print('Oh guy you are an adult now')
else:
    print('you are such a baby')

if age <= 18 and is_student:
    print('Oh guy you are an adult now')
else:
    print('you are such a baby')

is_citizen = False
if not is_citizen:
    print('age is 18 and more')
else:
    print('age is less')

    # function
def calculate_sum(a, b):
    return a + b
sum_total = calculate_sum(9, 91)
print(sum_total)

tax_rate = 0.1
def cacu(price):
    tax = tax_rate * price
    return tax
print(cacu(50))

#apply Discount Lab
def apply_discount(price, discount):
    if not isinstance(price,(int, float)):
     return'The price should be a number'
    
    if not isinstance(discount,(int, float)):
     return'The discount should be a number'
    
    if price <= 0: 
      return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
      return "The discount should be between 0 and 100"
     
    return price * (1-discount/100)
apply_discount(200, 50)

#Caesar Cipher
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)

#name = input('What is your name Lovely?')
#print('Hello!' + name + ' you look good')

# List
listi = ['Ruby', 'Caro', 'Eddy', 3]
print(listi[0])
del listi[1]
print(listi)
print(len(listi))
listi[2] = 4
print(listi)
'Ruby' in listi 
developer = ['Ama', 'Kofi', 'Gogo',  ['Didi', 'Dodo']]
print(developer[3][1])

nukor = 'Jessica'
print(list(nukor))

human = [ 'Ruby', '18', 'Cybersecurist']
name, age, job = human
print(name)
print(job)
name, *rest = human
human[1:2]

numbers = [ 1, 2, 3, 4, 5, 6, 7]
numbers[1::2]
numbers.append(8)
print(numbers)
even_numbers = [10, 12, 14, 20]
numbers.append(even_numbers)
print(numbers)
numbers.extend(even_numbers)
print(numbers)
numbers.insert(0,0)
print(numbers)
numbers.remove(20)
numbers.pop() #remove the last element
numbers.pop(9)
print(numbers)
numbers.reverse()
print(numbers)
numbers.clear

Lang =('Python', 'rust', 'Javascript', 'Java')
print(sorted(Lang))
print(sorted(Lang, key = len))
print(sorted(Lang, reverse = False))
print(Lang.index('Python'))

#Loop
ass= ['Me', 'You', 'Us', 'We']
for ruru in ass:
    print(ruru)
for ruby in 'JESUS':
    print(ruby)

categories = ['Fruits', 'Veges', 'The rest']
Foods = ['Banana', 'Onion', 'Bel-Cola']
for category in categories:
    for food in Foods:
     print(category, food)

for category in categories:
    if category == 'Veges':
     break
    print(category)

for category in categories:
    if category == 'Veges':
     continue
    print(category)

words = ['Apple', 'Ball', 'Cat', 'Dog']
for word in words:
   for letter in word:
      if letter.lower() in 'aeiou':
         print(f'{word} contains the vowel {letter}' )
else:
     print(f'{word} does not contain any vowel')
    

magic_num = 3
bobo = 2

while bobo != magic_num:
    guess = int(input('Guess any number from 1-5'))
    if guess != magic_num:
        print('You no get luck oo')
    else:
        bobo = magic_num
print('God bless you')

#Range
for num in range(3):
   print(num) 
for num in range (11, 1, -2):
   print(num)
mumu = list(range(1, 11, 2))
print(mumu)

languages = ['English', 'Ewe', 'Spanish', 'French']
index = 0
for lang in languages:
   print(f'{index} and {lang}')
   index += 1

list(enumerate(languages))

id = [1, 2, 3, 4]
for lang, ids in zip(languages, id):
   print(f'Language: {lang}')
   print(f'id: {ids}')

result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
total = sum(id)
print(total)

def is_lang(word):
   return len(word) > 4
long_word = list(filter(is_lang, languages))
print(long_word)

# Dictionary
pizza = {
   'name': 'Bobo',
   'price': 50,
   'ingredient': 'pepper',
   'toppings': ['Peri', 'Strawberry']
     }
print(pizza['name'])
print(pizza.get('toppings', []))
print(pizza.keys())
print(pizza.values())
print(pizza.items())
pizza.pop('price', 50)
pizza.update({'flavor': 'pepperoni'})
print(pizza)

for piz in pizza.keys():
   print(piz)
for val in pizza.values():
   print(val)
for item in pizza.items():
   print(item)
for piz, val in pizza.items():
   print(piz, val)

for index, piz in enumerate(pizza.keys()):
   print(index, piz)
for index, val in enumerate(pizza.values()):
   print(index, val)
for index, item in enumerate(pizza.items()):
   print(index, item)

# Sets
my_set = {1, 2, 3, 4, 5, 6}
your_set = { 2, 3, 4, 7}

print(your_set.issubset(my_set))
print(my_set | your_set)
print(my_set & your_set)
print(my_set - your_set)

#
import math as m
m.sqrt(36)

from math import radians, sin, cos
angle_degrees = 40
angle_radians = radians(angle_degrees )
sine_value = sin(angle_radians)
print(sine_value)

from math import * # import everything 

import datetime
birthday = datetime.date(2009, 7, 2)
print(birthday.day)
print(birthday.year)
print(birthday.month)

#class and object
class ClassName:
   def __init__(self,name,age):
      self.name = Name
      self.age = Age
   def ti_tan(self):
      print(self.name.upper())


class Cat:
   def __init__(self, name, age):
      self.name = Name
      self.age = Age
   def sound(self):
       print(f'{self.name.upper()} is my name and I\'m {self.age} fucking years old')
object_1 = Cat('Kofi', 3)

class book:
   def __init__(self,title,page):
      self.title = title
      self.page = page
   def __len__(self):
      return self.page 
   def __str__(self):
      return f'{self.title} has {self.page} fucking pages'
   def __eq__(self,other):
      return self.page == other.page