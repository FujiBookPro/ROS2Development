#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from example_interfaces.msg import String
from geometry_msgs.msg import Twist

class CommandConverterNode(Node):
    def __init__(self):
        super().__init__("command_converter")
        self.command_subscriber = self.create_subscription(
            String, "/commands", self.callback_command, 10)
        self.vel_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.get_logger().info("Command converter has been started.")

    def callback_command(self, command_msg: String):
        vel_msg = Twist()
        if command_msg.data == "move forward":
            vel_msg.linear.x = 1.0
        elif command_msg.data == "move right":
            vel_msg.linear.y = -1.0
        else:
            vel_msg.linear.x = 0.0
            vel_msg.linear.y = 0.0

        self.vel_publisher.publish(vel_msg)


def main(args=None):
    try:
        rclpy.init(args=args)
        node = CommandConverterNode()
        rclpy.spin(node)
        rclpy.shutdown()
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == "__main__":
    main()