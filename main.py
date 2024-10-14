import constants as c
from game import Game

def main():
    print (f'Welcome to {c.WINDOW_TITLE} !')
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

