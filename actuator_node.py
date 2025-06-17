# actuator_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ActuatorNode(Node):
    def __init__(self):
        super().__init__('actuator_node')
        self.subscription = self.create_subscription(
            Float32,
            'motor_command',
            self.listener_callback,
            10
        )
        self.altitude = 0.0

    def listener_callback(self, msg):
        thrust = msg.data
        self.altitude += thrust * 0.1  # fake physics
        self.get_logger().info(f'Altitude: {self.altitude:.2f} (thrust: {thrust:.2f})')

def main(args=None):
    rclpy.init(args=args)
    node = ActuatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
