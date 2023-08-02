from typing import Counter, Hashable
import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import String
# from jetbot import Robot
import motor_backend

robot = motor_backend.Robot()

class Reci(Node):
    def __init__(self):
        super().__init__('jetbot_listener')
        print("Jetbot_listener is working")

        #once jetbot has arrived the destination
        self.create_subscription(String, '/arrival', self.arrival_callback, 10)
        # self.publisher_jetbot = self.create_publisher(Twist,"/cmd_vel", 10)

    def arrival_callback(self,msg):
        # if msg.data:
        print("arrive")
        robot.set_motors(0,0.3)  
        time.sleep(2)
        robot.stop()

def main():
    rclpy.init()
    reci = Reci()

    # Spin until ctrl + c
    rclpy.spin(reci)

    reci.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


