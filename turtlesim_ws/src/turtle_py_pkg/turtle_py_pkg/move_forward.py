#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from example_interfaces.msg import String

class MoveForwardNode(Node):
    def __init__(self):
        super().__init__("move_forward_node")
        self.command_publisher = self.create_publisher(String, "/commands", 10)
        self.timer = self.create_timer(2.0, self.callback_command)
        self.get_logger().info("Move forward node has been started.")

    def callback_command(self):
        msg = String()
        msg.data = "move forward"
        self.command_publisher.publish(msg)


def main(args=None):
    try:
        rclpy.init(args=args)
        node = MoveForwardNode()
        rclpy.spin(node)
        rclpy.shutdown()
    except (KeyboardInterrupt, ExternalShutdownException):
        pass



if __name__ == "__main__":
    main()
