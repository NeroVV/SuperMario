# 游戏入口

from data import tools,setup

def main():
    game = tools.Game()
    game.run(setup.GRAPHICS)

if __name__ == '__main__':
    main()