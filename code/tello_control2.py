#! /usr/bin/python
from typing import Counter, Hashable
import rclpy
from rclpy.node import Node
from djitellopy import Tello
from std_msgs.msg import String

tello = Tello()
try :
	tello.connect()
	tello.takeoff()
	# tello.streamon()
	# frame_read = tello.get_frame_read()
except:
	pass

tello.rotate_counter_clockwise(45)
tello.move_forward(88)
tello.rotate_clockwise(45)
tello.move_forward(75)
tello.rotate_counter_clockwise(45)
tello.move_forward(123)
# cv2.imwrite("picture94.png", frame_read.frame)
tello.land()

class Fly_tello(Node):
    def __init__(self):
        super().__init__('tello_listener')

        # timer
        self.i = 0 # i is counter
        timer_period = 1  #每1s
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):

        if self.i < 2:
            msg = String()
            msg.data = "arrive"
            self.publisher_arr.publish(msg)
            self.i += 1 
            
def main():

    rclpy.init()
    fly_tello = Fly_tello()

    # Spin until ctrl + c
    rclpy.spin(fly_tello)

    fly_tello.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

