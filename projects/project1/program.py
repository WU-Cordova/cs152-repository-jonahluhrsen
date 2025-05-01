from Multideck import Multideck
from Game import Game
from Card import Card

def main():
    game = Game()
    start_input = input('Do you want to play Bagjack?: ').upper()
    if start_input == 'YES':
        game.play_game()

if __name__ == '__main__':
    main()