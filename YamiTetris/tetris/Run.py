import pygame
import pygame_menu
from Menu import *
from Tetris import *


import sys

running=True
while running:
    menu = Menu()
    menu.run()
    tetris=Tetris()
    print('ok? ')
    if menu.Mode == 'basic':
        tetris.mode='basic'
        if __name__ == "__main__":
            tetris.run()

    if menu.Mode == 'mini':
        tetris.mode='mini'
        if __name__ == "__main__":
            tetris.run()
    if menu.Mode == 'two':
        tetris.mode='two'
        if __name__ == "__main__":
            tetris.run()

    if menu.Mode == 'ai':
        tetris.mode='ai'
        weights = [3.39357083734159515, -1.8961941343266449, -5.107694873375318, -3.6314963941589093,

                   -2.9262681134021786,

                   -2.146136640641482, -7.204192964669836, -3.476853402227247, -6.813002842291903, 4.152001386170861,

                   -21.131715861293525, -10.181622180279133, -5.351108175564556, -2.6888972099986956,

                   -2.684925769670947,

                   -4.504495386829769, -7.4527302422826, -6.3489634714511505, -4.701455626343827, -10.502314845278828,

                   0.6969259450910086, -4.483319180395864, -2.471375907554622, -6.245643268054767, -1.899364785170105,

                   -5.3416512085013395, -4.072687054171711, -5.936652569831475, -2.3140398163110643, -4.842883337741306,

                   17.677262456993276, -4.42668539845469, -6.8954976464473585, 4.481308299774875]  # 21755 lignes

        if __name__ == '__main__':
            tetris.run()
