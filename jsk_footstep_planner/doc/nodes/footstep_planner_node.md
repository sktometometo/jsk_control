# jsk\_footstep\_planner

## What is this?


## Actionlib Server

* `goal` ( `jsk_footstep_msgs/PlanFootstep` )


## Subscribing topics

* `pointcloud_model` ( `sensor_msgs/PointCloud2` )

footstep を計算するときに用いる環境の点群.

* `obstacle_model` ( `sensor_msgs/PointCloud2` )

footstep を計算するときに用いる障害物の点群.


## Publishing topics

* `text` (`jsk_rviz_plugins/OverlayText`)

何かエラーが存在するときに、テキストを rviz に表示するための topic.

* `close_list` (`sensor_msgs/PointCloud2`)

探索グラフのクローズリスト?

* `open_list` (`sensor_msgs/PointCloud2`)

探索グラフのオープンリスト?

* `debug_marker_array` ( `visualization_msgs/MarkerArray` )


## Service Servers

* `project_footprint` ( `FootstepPlanner/projectFootPrint` )

* `project_footprint_with_local_search` ( `FootstepPlanner/projectFootPrintWithLocalSearch` )

* `collision_bounding_box_info` ( `FootstepPlanner/collisionBoundingBoxInfo` )

* `project_footstep` ( `FootstepPlanner/projectFootstep` )

* `set_heuristic_path` ( `FootstepPlanner/setHeuristicPath` )


## Parameters

* `lleg_footstep_offset` ( String representing an array of double values, default: `"[0, 0, 0]"` )

* `rleg_footstep_offset` ( String representing an array of double values, default: `"[0, 0, 0]"` )

* `collision_bbox_size` ( String representing an array of double values, default: `"[0, 0, 0]"` )

* `collision_bbox_offset` ( String representing an array of double values, default: `"[0, 0, 0]"` )

* `default_lfoot_to_rfoot_offset` ( String representing an array of double values, default: `"[0, 0, 0]"` )

* `successors` ( String representing an array of dicts representing a succesor )


## Dynamic Parameters

* `planning_timeout` ( Double, default: `10.0`, range: `[]` )

* `use_pointcloud_model` ( Bool, default: `False` )

* `use_lazy_perception` ( Bool, default: `False` )

* `use_local_movement` ( Bool, default: `False` )

* `use_transition_limit` ( Bool, default: `False` )

* `use_global_transition` ( Bool, default: `False` )

* `use_obstacle_model` ( Bool, default: `False` )

* `project_start_state` ( Bool, default: `False` )

* `project_goal_state` ( Bool, default: `False` )

* `local_move_x` ( Double, default: `1.0`, range: `[]` )

* `local_move_y` ( Double, default: `1.0`, range: `[]` )

* `local_move_theta` ( Double, default: `1.0`, range: `[]` )

* `local_move_x_offset` ( Double, default: `1.0`, range: `[]` )

* `local_move_y_offset` ( Double, default: `1.0`, range: `[]` )

* `local_move_theta_offset` ( Double, default: `1.0`, range: `[]` )

* `local_move_x_num` ( Int, default: `1.0`, range: `[]` )

* `local_move_y_num` ( Int, default: `1.0`, range: `[]` )

* `local_move_theta_num` ( Int, default: `1.0`, range: `[]` )

* `transition_limit_x` ( Double, default: `1.0`, range: `[]` )

* `transition_limit_y` ( Double, default: `1.0`, range: `[]` )

* `transition_limit_z` ( Double, default: `1.0`, range: `[]` )

* `transition_limit_roll` ( Double, default: `1.0`, range: `[]` )

* `transition_limit_pitch` ( Double, default: `1.0`, range: `[]` )

* `transition_limit_yaw` ( Double, default: `1.0`, range: `[]` )

* `global_transition_limit_roll` ( Double, default: `1.0`, range: `[]` )

* `global_transition_limit_pitch` ( Double, default: `1.0`, range: `[]` )

* `goal_pos_thr` ( Double, default: `0.5`, range: `[]` )

* `goal_rot_thr` ( Double, default: `pi`, range: `[]` )

* `plane_estimation_use_normal` ( Bool, default: `0.5`, range: `[]` )

* `plane_estimation_normal_distance_weight` ( Double, default: `1.0`, range: `[]` )

* `plane_estimation_normal_openning_angle` ( Double, default: `1.0`, range: `[]` )

* `plane_estimation_min_ratio_of_inliers` ( Double, default: `1.0`, range: `[]` )

* `plane_estimation_max_iteration` ( Int, default: ``, range: `[]` )

* `plane_estimation_min_inliers` ( Int, default: `100`, range: `[1,1001]` )

* `plane_estimation_outlier_threshold` ( Double, default: ``, range: `[]` )

* `support_check_x_sampling` ( Int, default: ``, range: `[]` )

* `support_check_y_sampling` ( Int, default: ``, range: `[]` )

* `support_check_vertex_neighbor_threshold` ( Double, default: ``, range: `[]` )

* `support_check_padding_x` ( Double, default: ``, range: `[]` )

* `support_check_padding_y` ( Double, default: ``, range: `[]` )

* `skip_cropping` ( Bool, default: ``, range: `[]` )

* `resolution_x` ( Double, default: ``, range: `[]` )

* `resolution_y` ( Double, default: ``, range: `[]` )

* `resolution_theta` ( Double, default: ``, range: `[]` )

* `footstep_size_x` ( Double, default: ``, range: `[]` )

* `footstep_size_y` ( Double, default: ``, range: `[]` )

* `close_list_x_num` ( Int, default: ``, range: `[]` )

* `close_list_y_num` ( Int, default: ``, range: `[]` )

* `close_list_theta_num` ( Int, default: ``, range: `[]` )

* `rich_profiling` ( Bool, default: ``, range: `[]` )

* `profile_period` ( Bool, default: ``, range: `[]` )

* `heuristic` ( String (enum), default: ``, range: `[]` )

* `heuristic_first_rotation_weight` ( Double, default: ``, range: `[]` )

* `heuristic_second_rotation_weight` ( Double, default: ``, range: `[]` )

* `cost_weight` ( Double, default: ``, range: `[]` )

* `heuristic_weight` ( Double, default: ``, range: `[]` )

* `obstacle_resolution` ( Double, default: ``, range: `[]` )

