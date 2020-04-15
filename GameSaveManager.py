from os import system, name 
from time import sleep 
  

############ Helper/necessary functions ############

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def unpack_list(list): # In order to easily use a list with f strings
    return str(list)[1:-2]

def unpack_dict(dict): # In order to easily use a dictionary with f strings
    dict_list = []
    for (key, value) in zip(list(dict.keys()), list(dict.values())):
        dict_list.append(key)
        dict_list.append(value)
    
    return dict_list


############ The meat and bones ############

class GSM():
    def __init__(self):
        self.games_list = dict()
    
    def add_game(self, game, directory):
        self.games_list[f'{game}'] = directory

    def modify_directory(self, game_name):
        self.games_list[game_name] = input('Choose the new directory: ')
        self.go_to('main_menu')

    def modify_name(self, game_name):
        self.games_list[input('Choose the new name: ')] = self.games_list.pop(game_name)
        self.go_to('main_menu')

    def go_to(self, which_menu):
        if which_menu == 'main_menu':
            clear()
            if self.games_list:
                print(f'Your current games are:')
                for i in range(len(unpack_dict(self.games_list))):
                    if i%2 != 0:
                        continue
                    print(f'{unpack_dict(self.games_list)[i]} with the directory {unpack_dict(self.games_list)[i+1]}')

                print('\nTo add another game, type add')
                print("To change a game's name/directory, type change")
                cur_input = input()
                if cur_input.lower().startswith('a'):
                    clear()
                    self.add_game(input("Game's name: "), input("Game's directory: "))
                    clear()
                    self.go_to('main_menu')
                elif cur_input.lower().startswith('c'):
                    clear()
                    cur_input = ''
                    
                    def retry_helper():
                        try:
                            clear()
                            game_name = input('Type the current name of the game you want to modify: ')
                            if self.games_list[game_name]:
                                pass
                            cur_input = input('Do you want to modify the name or the directory? ')
                            if cur_input.lower().startswith('n'):
                                self.modify_name(game_name)
                            elif cur_input.lower().startswith('d'):
                                self.modify_directory(game_name)
                        except:
                            retry_helper()
                    
                    retry_helper()

                else:
                    self.go_to('main_menu')
            else:
                if input("You don't have any current games added. Do you want do add a game? (y/n) ").lower().startswith('y'):
                    clear()
                    self.add_game(input("Game's name: "), input("Game's directory: "))
                    clear()
                    self.go_to('main_menu')
                else:
                    self.go_to('main_menu')


############ Program Startup ############

clear()
print('Game Save Manager loaded, press enter to continue...')

if input():
    clear()
    GSM().go_to('main_menu')
else:
    clear()
    GSM().go_to('main_menu')
