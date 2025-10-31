#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MoveRightNode(Node):
    def __init__(self):
        super().__init__("move_right_node")
        self.command_publisher = self.create_publisher(String, "/commands", 10)
        self.timer = self.create_timer(2.0, self.callback_command)
        self.get_logger().info("Move right node has been started.")

    def callback_command(self):
        msg = String()
        msg.data = "move right"
        self.command_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MoveRightNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
