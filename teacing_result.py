from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord
import time

mc = MyCobot("COM4", 115200)
time.sleep(2)

def make_move(mc):
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    time.sleep(2.5)
    mc.send_coords([165.5, -62.8, 195.8, -179.31, 2.06, -24.88], 50, 1)
    time.sleep(2.5)
    mc.send_coords([144.1, -63.7, 319.9, -95.01, -65.09, -84.48], 50, 1)
    time.sleep(2.5)
    mc.send_coords([180.0, 125.6, 240.9, -149.43, -59.51, 19.92], 50, 1)
    time.sleep(2.5)
    mc.send_coords([92.1, 24.7, 228.0, 160.71, 36.97, 7.04], 50, 1)
    time.sleep(2.5)

make_move(mc)