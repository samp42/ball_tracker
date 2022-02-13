import cv2 as cv
import rclpy
from rclpy.node import Node
from ball_tracker_interfaces.srv import get_image_service

class GetImageService(Node):

    def __init__(self):
        super().__init__('get_image_service')
        self.srv = self.create_service(GetImageService, 'get_image', self.get_image_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d, %s' % (request.a, request.b, cv.__version__))

        return response

    def get_image_callback(self, request, response):
        self.get_logger().info('Incoming request\ncamera: {}'.format(request.cameraID))
        return response


def main():
    rclpy.init()

    get_image_service = GetImageService()

    rclpy.spin(get_image_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
