from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord
import time

mc = MyCobot("COM4", 115200)
time.sleep(2)

def direct(mc):
    mc.power_off()
    time.sleep(10)
    mc.power_on()
    time.sleep(1)
    coord_datas = mc.get_coords()
    angle_datas = mc.get_angles()
    print(coord_datas)
    print(angle_datas)
direct(mc)
