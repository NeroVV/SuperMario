# 游戏入口

from data import tools,setup
from data.states import main_menu

def main():
    game = tools.Game()
    state = main_menu.MainMenu()
    game.run(state)

if __name__ == '__main__':
    main()