#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class PizzaDeliveryNode(Node):
    def __init__(self):
        super().__init__("pizza_delivery")
        self.pizza_subscriber = self.create_subscription(
            String, "pizza", self.callback_pizza, 10)
        self.house_publisher = self.create_publisher(String, "house", 10)
        self.get_logger().info("Pizza delivery has been started.")

    def callback_pizza(self, pizza_msg: String):
        house_msg = String()
        house_msg.data = "Delivering pizza to " + pizza_msg.data[6:] + " house."
        self.house_publisher.publish(house_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PizzaDeliveryNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
