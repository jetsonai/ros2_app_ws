from setuptools import find_packages
import os
from glob import glob
from setuptools import setup

package_name = 'ros_yolo_pack'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))         
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='katevm',
    maintainer_email='katevm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros_yolo_pub = ros_yolo_pack.ros_yolo_pub:main',
            'ros_yolo_pub2 = ros_yolo_pack.ros_yolo_pub2:main',
            'ros_yolo_sub = ros_yolo_pack.ros_yolo_sub:main',
            'ros_yolo_node = ros_yolo_pack.yolo11_node:main',
        ],
    },
)
