This README.txt file was generated on 2024-10-30 by Mateus Karvat.

--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset: Adver-City Dataset

2. Author Information
	A. Corresponding Author Contact Information
		Name: Mateus Karvat 
		Institution: Queen's University
		Email: mateus.karvat@queensu.ca
	
	B. Principal Investigator Contact Information
		Name: Sidney Givigi
		Institution: Queen's University
		Email: sidney.givigi@queensu.ca


3. Date of data collection: 2024-08-01 to 2024-08-07

4. Information about funding sources that supported the collection of the data: NSERC Discovery

---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data: 

These data are available under a CC BY-SA 4.0 license <https://creativecommons.org/licenses/by-sa/4.0/> 

2. Links to publications that cite or use the data: 

https://arxiv.org/abs/2410.06380

3. Links/relationships to ancillary data sets or software packages: 

Data generated in the CARLA Simulator v0.9.12 with OpenCDA v0.1.2.

CARLA: An Open Urban Driving Simulator
Alexey Dosovitskiy, German Ros, Felipe Codevilla, Antonio Lopez, Vladlen Koltun; PMLR 78:1-16. https://proceedings.mlr.press/v78/dosovitskiy17a/dosovitskiy17a.pdf

Xu, R., Guo, Y., Han, X., Xia, X., Xiang, H., & Ma, J. (2021, September). Opencda: an open cooperative driving automation framework integrated with co-simulation. In 2021 IEEE International Intelligent Transportation Systems Conference (ITSC) (pp. 1155-1162). IEEE. https://doi.org/10.48550/arXiv.2107.06260

4. Recommended citation for this dataset: 

Karvat, Mateus AND Givigi, Sidney. (2024). Adver-City Dataset. Federated Research Data Repository. doi: 10.20383/103.01084

---------------------
DATA & FILE OVERVIEW
---------------------

There are 111 7Zip files that should be extracted before usage. Except for the stats.7z file, which contains plots and a CSV file with statistics of the dataset, each 7z corresponds to a scenario, following the labeling scheme described below:

|     Road Configuration      | Abbreviation |
|:---------------------------:|:------------:|
|     Urban Intersection      |      ui      |
|     Urban Non-Junction      |     unj      |
|     Rural Intersection      |      ri      |
| Rural Straight Non-Junction |     rsnj     |
|  Rural Curved Non-Junction  |     rcnj     |

|   Weather and Daytime Condition   | Abbreviation |
|:---------------------------------:|:------------:|
|             Clear Day             |      cd      |
|            Clear Night            |      cn      |
|           Soft Rain Day           |     srd      |
|          Soft Rain Night          |     srn      |
|          Heavy Rain Day           |     hrd      |
|         Heavy Rain Night          |     hrn      |
|             Foggy Day             |      fd      |
|            Foggy Night            |      fn      |
|       Foggy Heavy Rain Day        |     fhrd     |
|      Foggy Heavy Rain Night       |     fhrn     |
|             Glare Day             |      gd      |

| Density Setting | Abbreviation |
|:---------------:|:------------:|
|      Dense      |      d       |
|     Sparse      |      s       |

The folder and file structure is as follows:

Adver-City  # root of project
├───data_dumping 
│    ├──2024_07_12_14_13_22  # timestamp of scenario generation
│    │   ├──unj_cn_d  # scenario label
│    │   │  ├──data_protocol.yaml  # merged configuration of all configuration YAMLs used for this scenario
│    │   │  ├──summary.yaml  # summary file of the scenario, used to quickly generate statistics
│    │   │  ├──698  # each CAV's folder is named after the object id it is assigned in CARLA
│    │   │  │  ├──000060.yaml  # ground truth file with information on frame 60 (frame count starts at 60)
│    │   │  │  ├──000060_camera0.png  # frontal RGB camera 
│    │   │  │  ├──000060_camera1.png  # right RGB camera 
│    │   │  │  ├──000060_camera2.png  # left RGB camera 
│    │   │  │  ├──000060_camera3.png  # back RGB camera 
│    │   │  │  ├──000060_semantic0.png  # frontal semantic camera
│    │   │  │  ├──000060_semantic1.png  # right semantic camera
│    │   │  │  ├──000060_semantic2.png  # left semantic camera
│    │   │  │  ├──000060_semantic3.png  # back semantic camera 
│    │   │  │  ├──000060_lidar.ply  # point cloud file 
│    │   │  │  ├──000060_gnss_imu.yaml  # gnss and imu data (only available for vehicles) 

Some notes regarding the folder structure:

* Each timestamp folder contains the folders for all scenarios generated when `main.py` was executed. Also, if the statistics script was executed, a `stats` folder will also appear, with the statistics files within it.

Adver-City
├───data_dumping 
│    ├──2024_07_12_14_13_22  
│    │   ├──stats
│    │   │  ├──class_histogram.pdf
│    │   │  ├──densiy_by_range_to_ego.pdf
│    │   │  ├──num_frames_per_ego_speed.pdf
│    │   │  ├──num_keyframes_per_num_annotations.pdf
│    │   │  ├──polar_density_map.pdf
│    │   │  ├──stats.csv
│    │   │  ├──time_of_day.pdf
│    │   │  ├──vehicles_per_speed.pdf
│    │   │  ├──weather.pdf
│    │   ├──unj_cn_d  
│    │   ├──unj_cn_s  
│    │   ├──unj_cd_d  
│    │   ├──unj_cn_s  

* Each scenario has a folder for each viewpoint. Adver-City's scenarios all have 2 RSUs (which always have negative ids) and 3 CAVs (whose folders are named after their CARLA object id).

Adver-City  # root of project
├───data_dumping 
│    ├──2024_07_12_14_13_22  
│    │   ├──unj_cn_d  
│    │   │  ├──698  # ego vehicle (the first folder is always the ego)
│    │   │  ├──712  # first vehicle
│    │   │  ├──726  # second vehicle
│    │   │  ├──-1  # first RSU
│    │   │  ├──-2  # second RSU

* Each frame will generate 11 files within the viewpoint's folder. As such, 55 files are saved for every frame executed in the simulation, which naturally causes CARLA to run significantly slower than usual during data dumping.
* Frame count starts at 60 since the initial frames of the simulation are not saved to avoid unusual after-spawning behavior.


---------------------------
METHODOLOGICAL INFORMATION
---------------------------

Data was generated on the CARLA Simulator v0.9.12 with OpenCDA. 

The sensor suite used is as follows:

| Sensors             | Details													    |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|
| 4x RGB cameras      | Resolution: 1920 x 1080 pixels, HFOV: 100 degrees							    |
| 4x Semantic cameras | Resolution: 1920 x 1080 pixels, HFOV: 100 degrees							    |
| 1x 3D LiDAR	      | Channels: 32 channels, Points Per Second: 1.2M, Frequency: 10 Hz, Range: 200 meters, VFOV: -25 to 15 degrees|
| GNSS & IMU	      | Standard deviation: 3e-6 rad (latitude and longitude) and 0.05 meters					    |


-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: PNG FILES
-----------------------------------------------------------------

Images from cameras in 1920x1080 resolution.

Each file name indicates which camera that image corresponds to, according to the following: 

_camera0.png - frontal RGB camera 
_camera1.png - right RGB camera 
_camera2.png - left RGB camera 
_camera3.png - back RGB camera 
_semantic0.png - frontal semantic camera 
_semantic1.png - right semantic camera 
_semantic2.png - left semantic camera 
_semantic3.png - back semantic camera 

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: PLY FILES
-----------------------------------------------------------------

Point-cloud data from the simulated 32-channel LiDAR captured at 10 Hz.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: YAML FILES
-----------------------------------------------------------------

Adver-City follows an annotation schema compatible with OPV2V. However, due to changes in sensors, there are some minor differences.

For each viewpoints' folder, each frame has a YAML file with data taken directly from the CARLA server. The data within it is organized as follows:

RSU: false # if this agent is an RSU or not
camera0: # parameters for the frontal camera
  cords: # camera coordinates under CARLA map coordinates
  - 213.1973419189453 # x
  - -5.52460241317749 # y
  - 1.483937382698059 # z
  - -0.00433349609375 # roll
  - -174.12957763671875 # yaw
  - -0.2315092533826828 # pitch
  extrinsic: # extrinsic matrix from camera to lidar
  - - 1.0
    - -2.1286936818054485e-17
    - -7.180017982536492e-20
    - -0.9500086905572118
  - - -4.959221109941733e-18
    - 0.9999999999999998
    - -4.757742642355514e-20
    - 1.0234670639874821e-06
  - - -4.90559482280122e-19
    - 6.599812935430275e-20
    - 1.0
    - 0.44999985330774583
  - - 0.0
    - 0.0
    - 0.0
    - 1.0
  intrinsic: # camera intrinsic matrix
  - - 805.5356459301888
    - 0.0
    - 960.0
  - - 0.0
    - 805.5356459301888
    - 540.0
  - - 0.0
    - 0.0
    - 1.0
camera1: ... # parameters for right camera
camera2: ... # parameters for left camera
camera3: ... # parameters for back camera
ego_speed: 0.1760935088021043 # speed of this agent in km/h
lidar_pose: # lidar pose under CARLA coordinates
- 214.1405487060547 # x
- -5.427590370178223 # y
- 1.9377721548080444 # z
- -0.00433349609375 # roll
- -174.12957763671875 # yaw
- -0.2315092533826828 # pitch
plan_trajectory: # list of locations to be followed by this agent, as defined by the path planning algorithm
- - 212.44387817382812 # x
  - -5.307567596435547 # y
  - 9.429222033557476 # z
- - 211.8439483642578
  - -5.316528797149658
  - 9.429222033557476
- - 211.04403686523438
  - -5.328477382659912
  - 9.429222033557476
- ...
predicted_ego_pos: # agent`s localization from GNSS
- 213.65081787109375 # x
- -5.478086948394775 # y
- 0.0357675738632679 # z
- -0.00433349609375 # roll
- -174.12957763671875 # yaw
- -0.2315092533826828 # pitch
true_ego_pos: # true position of this agent
- 213.65081787109375 # x
- -5.478086948394775 # y
- 0.0357675738632679 # z
- -0.00433349609375 # roll
- -174.12957763671875 # yaw
- -0.2315092533826828 # pitch
vehicles: # list of vehicles within line of sight of this agent
  1554: # id of the perceived vehicle
    angle: # under CARLA map coordinate system 
    - 0.00028235220815986395 # roll
    - 0.8933372497558594 # yaw
    - -0.032047245651483536 # pitch
    bp_id: vehicle.lincoln.mkz_2017 # blueprint id for this vehicle, from CARLA
    center: # relative position from the center of the bounding box to the frontal axis of the vehicle
    - 0.004043583292514086 # x
    - 7.466280038670448e-08 # y
    - 0.7188605070114136 # z
    class: car # class/category of this object. Adver-City has 6 classes: car, van, truck, motorcycle, bicycle and pedestrian
    color: 0, 0, 255 # integer r, g, b values for this vehicle
    dist: 94.9173812866211 # distance from the agent, in meters
    extent: # half length, width and height of the vehicle, in meters
    - 2.4508416652679443
    - 1.0641621351242065
    - 0.7553732395172119
    location: # position of the center in the frontal axis of the vehicle under CARLA map coordinate system
    - 119.29178619384766 # x
    - 4.802069187164307 # y
    - 0.0340358167886734 # z
    relative_angle: 175.0229148864746 # relative angle to the agent
    speed: 12.787282262180959 # speed of the vehicle, in km/h, in relation to the world (not in relation to the agent)
  1568: ...
  1608: ...
walkers: # list of pedestrians within line of sight of this agent
  1300:
    angle: # under CARLA map coordinate system 
    - 0.0 # roll
    - -0.6118773818016052 # yaw
    - 0.0 # pitch
    bp_id: walker.pedestrian.0024 # blueprint id for this pedestrian, from CARLA
    class: walker # class/category of this object. For pedestrians, it is always `walker`
    dist: 58.161373138427734
    extent: # half length, width and height of the pedestrian, in meters
    - 0.18767888844013214
    - 0.18767888844013214
    - 0.9300000071525574
    location: # position of the center in the frontal axis of the vehicle under CARLA map coordinate system
    - 159.15383911132812 # x
    - 14.811898231506348 # y
    - 1.1038998365402222 # z
    relative_angle: 173.51770025491714 # relative angle to the agent
    speed: 5.411598565237392 # speed of the pedestrian, in km/h, in relation to the world (not in relation to the agent)
  1318: ...
  1322: ...

