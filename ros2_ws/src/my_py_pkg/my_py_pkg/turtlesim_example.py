#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlesimExampleNode(Node):
    def __init__(self):
        super().__init__("turtlesim_example")
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(1, self.publish_movement)
        self.get_logger().info("Turtlesim example node has been started.")

    def publish_movement(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 2.0

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtlesimExampleNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
