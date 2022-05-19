from rplidar import RPLidar
import rclpy
from sensor_msgs.msg import LaserScan
#http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html
#idfk this msg
import sensor_msgs
from rclpy.node import Node



class LaserData():
    def __init__(self, node=None):
        lidar=RPLidar('/dev/ttyUSB0')
        info=lidar.get_info()
        print(info)
        self.log_info

        self.node=node
    def log_info(self, msg):
        if self.node is not None:
            self.node.get_logger().loginfo(msg)
        else:
            print(msg)
    def convert_to(self,data_type):
        if data_type==sensor_msgs.msg.LaserScan:
            


        if data_type=='string':
            return self.convert_to_string()
        elif data_type=='json':
            return self.convert_to_json()
        else:
            return self.convert_to_string()






class ScannerNode(Node):
    
        def __init__(self):
            super().__init__('scanner_node')
            self.scan_pub=self.create_publisher(
                LaserScan,
                'scan',
                10)
            freq=10
            self.timer_period=1/freq
            self.timer=self.create_timer(self.timer_period, self.timer_callback)
        def timer_standard_callback(self):
            msg=LaserScan()
            msg.angle_increment

        def timer_custom_callback(self):


    
        def scan_callback(self, msg):
            print('Received scan: ', msg)

def main():
    rclpy.init()
    node = ScannerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()