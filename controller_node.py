import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')

        # Subscribes to IMU data
        self.subscription = self.create_subscription(
            Float32,
            'imu/data',
            self.listener_callback,
            10
        )

        # Publishes to motor_command
        self.motor_pub = self.create_publisher(Float32, 'motor_command', 10)

    def listener_callback(self, msg):
        control_signal = -1 * msg.data  # simple inverse controller
        self.get_logger().info(f'Received IMU: {msg.data:.2f} | Control output: {control_signal:.2f}')
        
        # Send control signal to actuator
        motor_msg = Float32()
        motor_msg.data = control_signal
        self.motor_pub.publish(motor_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
