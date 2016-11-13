from z1 import Zad1
from z2 import Zad2
from z3 import Zad3
from z4 import Zad4
from z5 import Song
from z6 import Person
from zd1 import Triangle
from zd2 import Drink

x = Zad1()
print("Zad1: " + x.get_result())

x = Zad2(int(input("Zad2: Write number between 1 and 3999> ")))
print("      " + x.get_converted_number())

numarr = [1, 2, 3, 4, 5, 6]
x = Zad3(numarr)

print("Zad3: " + str(x.do()))

numarr2 = [6, 5, 4, 3, 2, 1]
x = Zad4(numarr, numarr2)
print("Zad4: " + str(x.search_array(10)))

Let_go = Song(["When it's black, ",
               "Take a little time to hold yourself, ",
               "Take a little time to feel around, ",
               "Before it's gone!"])
print("Zad5: " + Let_go.sing_me())

print("\nZad6:")
x = [Person("Andrew", 18),
     Person("Mat", 20),
     Person("Angelika", 21),
     Person("Andrew", 19),
     Person("Andrew", 18)]
print("Person 1 and Person 5: " + str(x[0] == x[4])) # !=
print("Person 4 and Person 5: " + str(x[3] == x[4]))
print("\nBEFORE SORTING\n")
for person in x:
    print(person.name + " " + str(person.age))
x.sort()
print("\nAFTER SORTING\n")
for person in x:
    print(person.name + " " + str(person.age))

x = Triangle(60, 60, 60)
my_triangle = Triangle(59, 61, 60)
print("\nZad.d1: " + str(x.check_angles()) + "\n        " + str(x.number_of_sides) + "\n        " + str(x == my_triangle))

print("\nZad.d2: ")
drinks = [Drink("rum", "9zł", "60%", "50ml"),
          Drink("cola", "2zł", "0%", "100ml"),
          Drink("ice", "0zł", "0%", "30ml")]
sumdrink = Drink("vodka", "8zł", "40%", "50ml")
print(str(sumdrink))
for drink in drinks:
    print(str(drink))
    sumdrink += drink
    print(str(sumdrink))
print(drinks[0] * 2)
print("\nBEFORE SORTING \n")
drinks.append(Drink("vodka", "8zł", "40%", "50ml"))
drinks.append(Drink("absinthe", "15zł", "70%", "50ml"))
drinks.append(Drink("spirit", "10zł", "96%", "100ml"))
for drink in drinks:
    print(drink.name + " : " + str(drink.get_cap_to_per()))
drinks.sort()
print("\nAFTER SORTING \n")
for drink in drinks:
    print(drink.name + " : " + str(drink.get_cap_to_per()))
