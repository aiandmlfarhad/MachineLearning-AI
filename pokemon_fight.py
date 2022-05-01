import pandas as pd
"""pokemon_dict = {'name': [], 'element': [], 'base_hp': [], 'base_attack': [], 'armor': [], 'price': [],
                'evolve_price': [], 'win_rate': [], 'evolved': []}
account_dict = {'name':[], 'pokemons':[], 'wallet':[]}"""

df_pokemon = pd.read_csv('pokemon_data.csv')
df_account = pd.read_csv('account_data.csv')
# df_pokemon.to_csv('pokemon_data.csv')
# df_account.to_csv('account_data.csv')


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
            pokemon.base_hp, pokemon.base_attack, pokemon.armor = 2*pokemon.base_hp, 2*pokemon.base_attack,\
                                                                  2*pokemon.armor
        else:
            print('Insufficient amount of money!!!')


class Food:
    def __init__(self, name, price, main_powerup, effect):
        self.name = name
        self.price = price
        self.main_powerup = main_powerup
        self.effect = effect


class Account:
    def __init__(self, name, pokemons, wallet=2000):
        self.name = name
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

    def duel(self, player, opponent_pokemon, own_pokemon):
        while opponent_pokemon.base_hp > 0 and own_pokemon.base_hp > 0:
            print(f"{own_pokemon.name} is attacking {opponent_pokemon.name}...\n {own_pokemon.base_attack}\
                    damage is dealt!!!")
            opponent_pokemon.base_hp -= own_pokemon.base_attack
            print(opponent_pokemon.base_hp)
            print(f"{opponent_pokemon.name} is attacking back to {own_pokemon.name}...\n {opponent_pokemon.base_attack}\
                    damage is dealt!!!")
            own_pokemon.base_hp -= opponent_pokemon.base_attack
            print(own_pokemon.base_hp)
        if opponent_pokemon.base_hp > 0:
            print(f"Winner is {player.user}'s {opponent_pokemon.name}")
        else:
            print(f"Winner is {self.name}'s {own_pokemon.name}")

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

def create_user():
    name = str(input('Welcome to the PokeWorld!!!, please follow the instructions.\n Please write your new user name:'))
    new_account = Account(name,[])
    df_account.loc[len(df_account.index) + 1] = [name,0,2000]
    df_account.to_csv('account_data.csv')
    print(f'Welcome to the PokeWorld {name}, you will be given 2000 poke Tokens at the beginning of your journey.')
    print('-----------ENTERING POKEWORLD-----------')


def existing_user(user_name):
    check = False
    for element in df_account.name:
        if user_name == element:
            check = True
            break
    if check:
        print('Welcome back Mr/Mrs {}'.format(user_name))
    else:
        raise ValueError

def game():
    print('Welcome to Pokemania v1.0')
    account_type = int(input('Are you an existing user(1) or a new one(2) ?\n ----- >'))
    if account_type == 1:
        nm = str(input('Please enter your existing user name:'))
        existing_user(nm)
    else:
        create_user()
game()