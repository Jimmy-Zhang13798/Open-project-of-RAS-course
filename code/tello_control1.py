#! /usr/bin/python
from typing import Counter, Hashable
import numpy as np
import cv2
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
import time
from djitellopy import Tello
import math
from sensor_msgs.msg import Image
from std_msgs.msg import String,UInt32
from nav_msgs.msg import Odometry
from rosgraph_msgs.msg import Clock
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from djitellopy import Tello

class Fly_tello(Node):
    def __init__(self):
        super().__init__('tello_listener')
        print("tello_listener is working")

        self.i = 0 # i is counter

        # these two  publishers are for controlling the jetbot
        self.publisher_control = self.create_publisher(Twist, '/control', 10)
        self.publisher_land = self.create_publisher(Empty, '/land', 10)
        self.publisher_takeoff = self.create_publisher(Empty, '/takeoff', 10)
        self.publisher_arr = self.create_publisher(String,"/arrival", 10)
        # exit()

        takeoff1=Empty()
        self.publisher_takeoff.publish(takeoff1)
        print("Already took off")
        time.sleep(3)

        # self.path = [(10, 50), (11, 49), (12, 48), (13, 47), (14, 46), (15, 45), (16, 44), (17, 43), (18, 42), (19, 41), (19, 40), (19, 39), (19, 38), (19, 37), (19, 36), (20, 35), (21, 34), (22, 33), (23, 32), (24, 31), (25, 30)]

        self.path = np.load("path.npy")
        self.path = self.path[::-1]

        print(self.path)
        # exit()
        
        for i in range(len(self.path)-1):
            move_array = np.array(self.path[i+1]) - np.array(self.path[i])

            move_cmd = Twist()
            move_cmd.angular.z = 0.0
            move_cmd.linear.z = 0.0
            move_cmd.linear.x = float(10 * move_array[0])
            move_cmd.linear.y = float(10 * move_array[1])

            print(move_cmd)
            self.publisher_control.publish(move_cmd)
            time.sleep(2)   

        land1=Empty()
        self.publisher_land.publish(land1)

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


