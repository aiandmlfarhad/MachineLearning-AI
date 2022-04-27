"""int1 = int(input(":"))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34, 56]
def binary(list, int):
    mid = len(list) // 2
    if int < list[mid]:
        return binary(list[0:mid], int)
    elif len(list) == 1 and list[0] == int:
        return True
    elif int == list[mid]:
        return True
    else:
        return binary(list[mid+1:len(list)], int)
try:
    print(binary(list1,int1))
except:
    print("False")"""
"""int1 = int(input(";"))
list1 = [34,23,45,56,67,78]
for element in list1:
    if element == int1:
        print(True)"""
"""int1 = int(input(":"))
numbers = [12,14,16,17,28,29,45,67]
interval = 4
bool1 = False
jump = interval
while len(numbers) > interval:
    if int1 > numbers[interval-1]:
        numbers = numbers[interval-1:len(numbers) - 1]
        interval += interval
    elif int1 < numbers[interval-1]:
        numbers = numbers[interval-jump:interval-1]
        interval += interval
    else:
        bool1 = True
for elemenst in numbers:
    if elemenst == int1:
        bool1 = True
print(bool1)"""
"""import turtle
class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        self.total_angles = (self.sides - 2) * 180
        self.angles = self.total_angles / self.sides
    def draw(self):
        for side in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angles)
        turtle.done()
square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")
hexagon = Polygon(6, "Hexagon")
hexagon.draw()"""
"""class User:
    def __init__(self, name, surname, age, budget):
        self.name = name
        self.surname = surname
        self.budget = budget
        self.age = age
    def show(self):
        print(f"Welcome Mr/Mrs {self.name} {self.surname}, age = {self.age}. Your budget is {self.budget}")
class Bank(User):
    def __init__(self, name, surname, age, budget):
        super().__init__(name, surname, age, budget)
    def deposit(self):
        deposit_budget = int(input("Please input the amount you want to deposit:"))
        self.budget += deposit_budget
    def withdraw(self):
        withdraw_budget = int(input("Please input the amount you want to withdraw:"))
        self.budget -= withdraw_budget
    def view_budget(self):
        print(f"Your budget is {self.budget}")
User1 = Bank("Farhad","Hashimov", 19, 180)
User2 = Bank("Kamil", "Haydarov", 21, 900)
User2.withdraw()
User2.view_budget()"""
"""import matplotlib.pyplot as plt
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, otherPoint):
        x = self.x + otherPoint.x
        y = self.y + otherPoint.y
        return Point(x,y)
    def show_point(self):
        plt.scatter(self.x,self.y)
        plt.show()
a = Point(1,2)
b = Point(4,5)
c = a + b
print(c.x,c.y)"""
"""class Pokemon:
    def __init__(self, name, HP, attack, type):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.type = type
    def show(self):
        print(f"Welcome to Pokemon description window.\n Name: {self.name}\n Type: {self.type}\n HP: {self.HP}\n Attack: {self.attack}")
    def feed(self):
        fruit = str(input("Welcome to pokemon level up window.\nPlease enter the fruit you want to feed with your pokemon\n1-Apple(15)\n2-Orange(25)\n3-Grape(80)\n"))
        fruit.lower()
        if fruit == "apple":
            self.HP += 15
        elif fruit == "orange":
            self.HP += 25
        elif fruit == "grape":
            self.HP += 80
        else:
            print("A problem was occured")
    def fight(self, opponent):
        print("!!!FIGHT!!!")
        while self.HP > 0 and opponent.HP > 0:
            self.HP -= opponent.attack
            print(f"{self.name} attacks to {opponent.name}\n {self.attack} damage dealt to {opponent.name}")
            print(f"{self.name}:{self.HP}HP, {opponent.name}:{opponent.HP}HP")
            opponent.HP -= self.attack
            print(f"{opponent.name} attacks to {self.name}\n {opponent.attack} damage dealt to {self.name}")
            print(f"{self.name}:{self.HP}HP, {opponent.name}:{opponent.HP}HP")
        if self.HP < 0 and opponent.HP > 0:
            print(f"Winner is {opponent.name}")
        elif self.HP > 0 and opponent.HP < 0:
            print(f"Winner is {self.name}")
pokemon1 = Pokemon("Bulbasar", 200, 12, "Forest")
pokemon2 = Pokemon("Pikachu", 250, 11, "Electric")
pokemon3 = Pokemon("Charmander", 400, 2, "Rock")
pokemon2.fight(pokemon3)"""
"""from requests import get
from pprint import PrettyPrinter
prnt = PrettyPrinter()
url = "http://data.nba.net"
adress = "/prod/v1/today.json"
data = get(url + adress).json()
score = get(url + data["links"]["currentScoreboard"]).json()
prnt.pprint(score)
"""
"""import numpy as np
number = np.array([1.030121,2.3434312])
number = np.round(number, decimals=2)
n1 = np.array([10,20,30])# difeerence between numpy array and normal list
n2 = n1 + n1
l1 = [10,20,30]
l2 = l1+l1
check = n1 > 5
family = np.array([[1,2,3],[12,3,4],[1,56,34],[23,45,231]])
print(family[:][1:4])
"""
"""import csv
with open("C:/Users/ferha/OneDrive/Presentations/Data/addresses.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)"""
"""import numpy as np
a = np.random.normal(1.8,0.2,100)
b = np.random.normal(65,15,100)
c = np.column_stack((a,b))
print(help(np.round))"""
"""import re
string = "Sahin_restoran, Kamil_restoran ve Babil_restoran eladirda qaqa"
list = string.split(" ")
for element in list:
    print(re.findall("^[A-Z]+[a-z]+[_]+[a-z]+",element))"""
"""import matplotlib.pyplot as plt
import numpy as np
years = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
price = [12,13,14,17,19,25,24,21,30,25,23]
#plt.scatter(years,price)
plt.scatter(years,price)
plt.title("Illere gore qiymetlerin deyismesi")
plt.xlabel("Iller")
plt.ylabel("Qiymetler")
plt.yticks([1,5,10,15,20,25,30,35,40,45,50], ['1M', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M', '50M'])
plt.show()"""
"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
my_dict = {'baku':[18,20,19,21,23,22], 'ganja':[10,9,11,10,14,15], 'shaki':[12,13,16,29,15,14], 'goychay':[13,14,15,12,11,10]}
new_dict = pd.read_csv('D:/grades.csv')
print(new_dict)"""
"""def plus_printer(func):
    def inner(msg):
        msg = "+++++" + msg + "+++++"
        return msg
    return inner
def mult_printer(func):
    def inner(msg):
        msg = "*****" + msg + "*****"
        return msg
    return inner

@plus_printer
@mult_printer
def printer(msg):
    return msg
print(printer("Sikdir"))"""
"""concat_names = lambda x, y: x.strip() + " "+ y.strip()
print(concat_names("Kamil", "Hashimov"))"""
import pandas as pd
file = pd.read_csv("D://grades.csv")
#pd.set_option("max_columns", None)
#print(file[0:1].head())
print(file.loc[[0]])
