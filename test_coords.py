from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import time

def home(mc):
    mc.send_coords([136.9, -61.8, 306.6, -89.12, -45.24, -90.09], 50, 1)
    time.sleep(3)
    
mc = MyCobot("COM4", 115200)
time.sleep(2)
    
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
time.sleep(3)
home(mc)

coords = mc.get_coords()
print(coords)

mc.send_coord(Coord.X.value, coords[0]+90, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.X.value, coords[0]-90, 50)
time.sleep(2.5)
home(mc)

mc.send_coord(Coord.Y.value, coords[1]+90, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.Y.value, coords[1]-90, 50)
time.sleep(2.5)
home(mc)

mc.send_coord(Coord.Z.value, coords[2]+45, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.Z.value, coords[2]-45, 50)
time.sleep(2.5)
home(mc)

mc.send_coord(Coord.Rx.value, coords[3]+45, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.Rx.value, coords[3]-45, 50)
time.sleep(2.5)
home(mc)

mc.send_coord(Coord.Ry.value, coords[4]+45, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.Ry.value, coords[4]-45, 50)
time.sleep(2.5)
home(mc)

mc.send_coord(Coord.Rz.value, coords[5]+45, 50)
time.sleep(2.5)
home(mc)
mc.send_coord(Coord.Rz.value, coords[5]-45, 50)
time.sleep(2.5)
home(mc)
