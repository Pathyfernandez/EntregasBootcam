# variable declaration
"""
Data Types
    - Primitive
        - Boolean
        - Numbers
        - Strings

"""


num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'



# log statement

"""
- List 
            - initialize
            - access value
            - change value
            - add value
            - delete value
"""

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
# length check
"""
- Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value

"""

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'

# type check
"""
- Tuples
            - initialize
            - access value
            - change value
            - add value
            - delete value
"""
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(fruit[2])


"""
conditional
    - if
    - else if
    - else
"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


"""
for loop
    - start
    - stop
    - increment
    - break
    - continue
"""
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0

"""
while loop
    - start
    - stop
    - increment

"""

while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

"""
function
    - parameter
    - argument
    - return
"""

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
- comment
    - multiline

"""

"""
Bonus section
"""
"""
- comment
    - single line
"""
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)




