from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'mini_drone_sim'
    pkg_share = get_package_share_directory(package_name)
    urdf_path = os.path.join(pkg_share, 'drone/my_quadrotor.urdf')
    rviz_config_path = os.path.join(pkg_share, 'rviz/config.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='state_publisher',
            parameters=[{'robot_description': open(urdf_path).read()}],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen',
        ),
    ])
