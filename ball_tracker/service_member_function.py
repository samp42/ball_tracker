from example_interfaces.srv import AddTwoInts
import cv2 as cv
import rclpy
from rclpy.node import Node


class VisionService(Node):

    def __init__(self):
        super().__init__('vision_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d, %s' % (request.a, request.b, cv.__version__))

        return response

    def calibrate_camera_callback(self, request, response):
        self.get_logger().info('request')
        return response

    def find_balls_callback(self, request, response):
        self.get_logger().info('request')
        return response

    def find_closest_ball_callback(self, request, response):
        self.get_logger().info('request')
        return response


def main():
    rclpy.init()

    vision_service = VisionService()

    rclpy.spin(vision_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
