# Pokemon proqrami yazilacak
# En az 10 pokemondan ibaret bazasi olacak
# Pokemonlarin elementleri olacaq - electriciy, water, flame, rock, wind, forest
# Kritik vurus ata bilmedirler
# 2 pokemon secib dovusdure bilmeli, onlari qidalandirib boyude bilmeliyik
# Alinan yemekler ucun sebet olmali
# Yemekler pulla alinmali, pul ise doyusmekle alinir
# 1 vs 2 doyus sistemide var hansi ki 5 qat pul verir
class Pokemon:
    def __init__(self, name, element, base_hp, base_attack, armor, price, win_rate=0, evolved=False):
        self.name = name
        self.element = element
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.armor = armor
        self.price = price
        self.win_rate = win_rate
        self.evolved = evolved
class Food:
    def __init__(self, name, price, main_powerup, effect):
        self.name = name
        self.price = price
        self.main_powerup = main_powerup
        self.effect = effect
class Account:
    def __init__(self, user, wallet, pokemons = None):
        self.user = user
        self.wallet = wallet
        self.pokemon = pokemons
Othys = Account('Othys', 2000)
Bulbasar = Pokemon('Bulbasar', 'forest', 2000, 300, 80, 500, 0)
Pikachu = Pokemon('Pikachu', 'electricity', 3000, 650, 70, 1200)
blue_flower = Food('blue_flower', 35, 'base_attack', 0.025)
red_flower = Food('red_flower', 40, 'base_hp', 0.030)

