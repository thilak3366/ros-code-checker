import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node("good_node")
    rclpy.spin(node)

if __name__ == "__main__":
    main()
