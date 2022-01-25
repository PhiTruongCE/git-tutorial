"""
autonomousRobot
This project is to simulate an autonomousRobot that try to find a way to reach a goal (target) 
author: Binh Tran Thanh / email:thanhbinh@hcmut.edu.vn
"""
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

from Robot_lib import *
from Robot_paths_lib import *
from Robot_draw_lib import *
from Robot_sight_lib import *
from Robot_map_lib import *
from Robot_world_lib import *
from Robot_csv_lib import *
from Robot_goal_lib import *
from Program_config import *
from Robot_control_panel import *
plt.figure(figsize=(5,5))
ptA = (0, 0)
ptB = (10, 0)
ptC = (6,3)

obstacles=[]

# obstacle_in = [
#             (177,201),
#             (176,202),
#             (175,202),
#             (175,203),
#             (174,204),
#             (174,205),
#             (177,205),
#             (178,204),
#             (178,203),
#             (176,205),
#             (175,205),
#             (174,204),
#             (177,201),
#             (180,201),
#             (181,202),
#             (183,202),
#             (184,203),
#             (186,203),
#             (187,204),
#             (189,204),
#             (190,205),
#             (191,205),
#             (192,206),
#             (194,206),
#             (192,206),
#             (191,205),
#             (190,205),
#             (189,204),
#             (187,204),
#             (186,203),
#             (184,203),
#             (183,202),
#             (181,202),
#             (180,201),
#             (177,201)
# ]

obstacle_in = [
            (0,0), 
            (10,0), 
            (2.5,2.5),
            (0,12),
            (0,0)
]

obstacles.append(obstacle_in)

#map_display(plt, "Binh_test_configure_space", obstacles)

for obstacle in obstacles:
    i = 0
    obstacle.pop()
    while (i < len(obstacle)):
        if (obstacle[(i + 1)%len(obstacle)] == obstacle[i - 1]):
            obstacle.pop(i)
            if (i == 0):
                obstacle.pop(-1)
            elif (i == len(obstacle)):
                obstacle.pop(0)
                i = i - 2
            else:
                obstacle.pop(i)
                i = i - 1
        else:
            i = i + 1

    j = 0
    while (j < len(obstacle)):
        if (belong_line(obstacle[j],[obstacle[j - 1], obstacle[(j + 1)%len(obstacle)]])):
            obstacle.pop(j)
        else:
            j = j + 1
    
    if (len(obstacle) > 0):
        obstacle.append(obstacle[0]) 

i = 0
while (i < len(obstacles)):
    if (len(obstacles[i]) < 1):
        obstacles.pop(i)
    else:
        i += 1 
        
print ("________________")
#print (obstacles)
cspaces = find_configure_space_update_2(obstacles, 0.2)
#cspaces = find_configure_space(obstacles, 1.1)
#print (cspaces)
# fig, axs = plt.subplots(3)
# map_display_update(axs[0], obstacles)
# map_display_update(axs[1], cspaces)
# map_display_update(axs[2], obstacles)
# map_display_update(axs[2], cspaces)
# print (obstacles)
map_display(plt, "Binh_test_configure_space", obstacles)
map_display(plt, "Binh_test_configure_space", cspaces)

plt.grid(True)
plt.show()
