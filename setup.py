# from setuptools import setup

# package_name = 'mini_drone_sim'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=[package_name],
#     data_files=[
#         ('share/' + package_name, ['package.xml']),
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='elida',
#     maintainer_email='elsensoy@umich.edu',
#     description='Mini drone sim with fake IMU and controller',
#     license='MIT',
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': [
#             'imu_sim = mini_drone_sim.imu_sim_node:main',
#             'controller = mini_drone_sim.controller_node:main',
#             'actuator = mini_drone_sim.actuator_node:main',
#         ],
#     },
# )
from setuptools import setup
import os
from glob import glob

package_name = 'mini_drone_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'drone'), glob('drone/*.urdf')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elida',
    maintainer_email='elsensoy@umich.edu',
    description='Mini drone sim with fake IMU and controller',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_sim = mini_drone_sim.imu_sim_node:main',
            'controller = mini_drone_sim.controller_node:main',
            'actuator = mini_drone_sim.actuator_node:main',
        ],
    },
)
