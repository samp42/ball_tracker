from setuptools import setup

package_name = 'ball_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Samuel Proulx',
    maintainer_email='samuelproulx26@gmail.com',
    description='Program to track a moving ball',
    license='GPL-v3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = ball_tracker.service_member_function:main',
            'client = ball_tracker.client_member_function:main',
        ],
    },
)
