from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD # When using the Raspberry Pi version of myCob
import time



class RobotMotion:
    def __init__(self, port , baud):
        # Initialize a MyCobot object
        self.mc = MyCobot(port, baud)

    # Power the robot arm
    def power_on(self):
        if not self.mc.is_power_on():
            self.mc.power_on()

    # Power off the robot arm
    def power_off(self):
        self.mc.power_off()
        if self.mc.is_all_servo_enable() == -1:
            print('작동 종료 확인')
    
    # 로봇 암을 해제하여 수동으로 조정 가능
    def release_all_servos(self):
        self.mc.release_all_servos()

    def get_coords(self):
        print(self.mc.get_coords())
    
    def led(self):
        timer = 0.5
        i = 7
        while i > 0:                            
            self.mc.set_color(0,0,255) #blue light on
            time.sleep(timer)    #wait for 2 seconds                
            self.mc.set_color(255,0,0) #red light on
            time.sleep(timer)    #wait for 2 seconds
            self.mc.set_color(0,255,0) #green light on
            time.sleep(timer)    #wait for 2 seconds
            i -= 1

    def swing_left_right(self):
        angle_datas = self.mc.get_angles()
        print(angle_datas)

        self.mc.send_angles([0, 0, 0, 0, 0, 0], 20)
        time.sleep(2.5)

        self.mc.send_angle(Angle.J1.value, 90, 50)
        time.sleep(2)

        num=3
        while num > 0:
            self.mc.send_angle(Angle.J1.value, 50, 50)
            time.sleep(1.5)
            self.mc.send_angle(Angle.J1.value, -50, 50)
            time.sleep(1.5)
            num -= 1

        self.mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)
        time.sleep(2.5)

    # 0: run, 1: stop running
    def pump_on(self):
        self.mc.set_basic_output(2, 0)
        self.mc.set_basic_output(5, 0)

    # 펌프 종료
    def pump_off(self):
        self.mc.set_basic_output(2, 1)
        self.mc.set_basic_output(5, 1)




if __name__=='__main__':
    mycobot = RobotMotion("COM8", 115200)
    # mycobot.led()
    mycobot.power_on()
    # mycobot.power_off()
    mycobot.swing_left_right()
    # 
    # mycobot.get_coords()

    # mycobot.pump_on()
    # time.sleep(3)
    # mycobot.pump_off()
