# Pokemon proqrami yazilacak
# En az 10 pokemondan ibaret bazasi olacak
# Pokemonlarin elementleri olacaq - electriciy, water, flame, rock, wind, forest
# Kritik vurus ata bilmedirler
# 2 pokemon secib dovusdure bilmeli, onlari qidalandirib boyude bilmeliyik
# Alinan yemekler ucun sebet olmali
# Yemekler pulla alinmali, pul ise doyusmekle alinir
# 1 vs 2 doyus sistemide var hansi ki 5 qat pul verir
import pandas as pd
class Pokemon:
    def __init__(self, name, element, base_hp, base_attack, armor, price, evolve_price, win_rate=0, evolved=False):
        self.name = name
        self.element = element
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.armor = armor
        self.price = price
        self.win_rate = win_rate
        self.evolved = evolved
        self.evolve_price = evolve_price
    def evolve(self, user, pokemon):
        if user.wallet >= pokemon.evolve_price:
            pokemon.base_hp, pokemon.base_attack, pokemon.armor = 2*pokemon.base_hp, 2*pokemon.base_attack, 2*pokemon.armor
        else:
            print('Insufficient amount of money!!!')

class Food:
    def __init__(self, name, price, main_powerup, effect):
        self.name = name
        self.price = price
        self.main_powerup = main_powerup
        self.effect = effect
class Account:
    def __init__(self, user, wallet, pokemons):
        self.user = user
        self.wallet = wallet
        self.pokemons = pokemons
    def buy(self, pokemon):
        if self.wallet >= pokemon.price:
            self.pokemons.append(pokemon.name)
            self.wallet -= pokemon.price
        else:
            print('Insufficient amount of money!!!')
    def sell(self, pokemon):
        if len(self.pokemons) == 1:
            print("Last pokemon can't be sold!!!")
        else:
            self.pokemons.remove(pokemon.name)
            self.wallet += pokemon.price
    def duel(self, player, pokemon):
        pass
    def feed(self, food, pokemon):
        if self.wallet >= food.price:
            if food.main_powerup == 'base_hp':
                pokemon.base_hp *= food.effect
            elif food.main_powerup == 'base_attack':
                pokemon.base_attack *= food.effect
            else:
                pokemon.armor *= food.effect
        else:
            print('Insufficient amount of money!!!')

Othys = Account('Othys', 2000, [])
Bulbasar = Pokemon('Bulbasar', 'forest', 2000, 300, 80, 500, 5000)
Pikachu = Pokemon('Pikachu', 'electricity', 3000, 650, 70, 1200, 7500)
blue_flower = Food('blue_flower', 35, 'base_attack', 1.025)
red_flower = Food('red_flower', 40, 'base_hp', 1.030)

Othys.buy(Bulbasar)
Othys.buy(Pikachu)
Othys.feed(blue_flower, Bulbasar)
print(Bulbasar.base_attack)


