# ros2_app_ws

cd ros2_app_ws

colcon build 

source ./install/setup.bash

## 카메라 테스트

ros2 run cv_basics cam_node

## 카메라 발행자 구독자

ros2 run cv_basics 

ros2 run cv_basics 

## 라이다 테스트

ros2 launch ldlidar_stl_ros2 viewer_ld19.launch 

## 라이다 구독 테스트

cd ros2_app_ws

colcon build --packages-select sensor_test_pack

ros2 run sensor_test_pack lidar_sub_node_best



