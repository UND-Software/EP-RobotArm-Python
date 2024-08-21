from pymycobot.mycobot import MyCobot
import time


mc = MyCobot("COM4", 115200)

i = 7
while i > 0:                            
    mc.set_color(0,0,255) #blue light on
    time.sleep(0.5)                  
    mc.set_color(255,0,0) #red light on
    time.sleep(0.5)    
    mc.set_color(0,255,0) #green light on
    time.sleep(0.5)    
    i -= 1