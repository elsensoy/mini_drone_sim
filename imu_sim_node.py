import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class ImuSimNode(Node):
    def __init__(self):
        super().__init__('imu_sim_node')
        self.publisher_ = self.create_publisher(Float32, 'imu/data', 10)
        self.timer = self.create_timer(1.0, self.publish_fake_imu)

    def publish_fake_imu(self):
        imu_value = Float32()
        imu_value.data = random.uniform(-1.0, 1.0)
        self.publisher_.publish(imu_value)
        self.get_logger().info(f'Publishing IMU data: {imu_value.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ImuSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
