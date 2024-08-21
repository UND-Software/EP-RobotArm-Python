from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord
import time

mc = MyCobot("COM4", 115200)
time.sleep(2)

angle_datas = mc.get_angles()
print(angle_datas)

def move_angle(mc, joint_id):
    mc.send_angle(joint_id, 90, 40)
    time.sleep(2.5)
    mc.send_angles([0, 0, 0, 0, 0, 0], 40)
    time.sleep(2.5)
    mc.send_angle(joint_id, -90, 40)
    time.sleep(2.5)
    mc.send_angles([0, 0, 0, 0, 0, 0], 40)
    time.sleep(2.5)
    
move_angle(mc, Angle.J1.value)
move_angle(mc, Angle.J2.value)
move_angle(mc, Angle.J3.value)
move_angle(mc, Angle.J4.value)
move_angle(mc, Angle.J5.value)
move_angle(mc, Angle.J6.value)
