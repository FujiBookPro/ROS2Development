#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class PizzaShopNode(Node):
    def __init__(self):
        super().__init__("pizza_shop")
        self.counter = 0
        self.publisher = self.create_publisher(String, "pizza", 10)
        self.timer = self.create_timer(1.0, self.deliver_pizza)
        self.get_logger().info("Pizza shop has been started.")

    def deliver_pizza(self):
        msg = String()
        msg.data = "pizza " + str(self.counter)
        self.counter += 1
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PizzaShopNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()