# 游戏入口

from data import tools
from data.states import main_menu,load_screen,level
from data import constants as C

def main():

    state_dict = {
        C.MAIN_MENU:main_menu.MainMenu(),
        C.LOAD_SCREEN:load_screen.LoadScreen(),
        C.LEVEL:level.Level()
    }
    game = tools.Game(state_dict,'main_menu')

    game.run()

if __name__ == '__main__':
    main()