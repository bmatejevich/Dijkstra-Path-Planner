#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = math.inf
        self.parent = None


class Robot:
    def __init__(self, radius, clearance, start, goal):
        self.radius = radius
        self.clearance = clearance
        self.start = start
        self.goal = goal
        
xs = True        
xg = True
ys = True
yg = True

robot = Robot(1,0,[0,0],[10,10])

def check_viableX(point):
    if point >= 0 and point <= 200:
        return False
    else:
        print("invalid")
        return True
def check_viableY(point):
    if point >= 0 and point <= 100:
        return False
    else:
        print("Invalid")
        return True
    
while xs == True:
    x_start = input("Enter robot x position : ")
    x_start = int(x_start)
    xs = check_viableX(x_start)
while ys == True:
    y_start = input("Enter robot y position : ") 
    y_start = int(y_start)
    ys = check_viableY(y_start)
while xg == True:
    x_goal = input("Enter goal x position : ") 
    x_goal = int(x_goal)
    xg = check_viableX(x_goal)
while yg == True:
    y_goal = input("Enter goal y position : ") 
    y_goal = int(y_goal)
    yg = check_viableY(y_goal)

robot.start = [x_start,y_start]
robot.goal = [x_goal,y_goal]
print(robot.start,robot.goal)
    


# In[1]:


import numpy as np
import cv2


# In[2]:


robot = Robot(1,0,[0,0],[10,10])
print(robot.start)


# In[4]:


def plot_workspace():
    img = 255 * np.ones((151, 251, 3), np.uint8)

    # Plot the square
    cords_square = np.array(
        [[50 , 37.5 ], [100 , 37.5 ], [100, 82.5 ],
         [50 , 82.5 ]], dtype=np.int32)
    cords_square1 = np.array([[50, 37.5], [100, 37.5], [100, 82.5], [50, 82.5]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_square, 255)
    cv2.fillConvexPoly(img, cords_square1, 0)

    # Plot the circle
    cv2.circle(img, (190, 20), 15 - 1, (255, 0, 0), -1)
    cv2.circle(img, (190, 20), 15 - 1, (0, 0, 0), -1)

    # Plot the ellipse
    cv2.ellipse(img, (140, 30), (15 , 6 ), 0, 0, 360, 255, -1)
    cv2.ellipse(img, (140, 30), (15 , 6), 0, 0, 360, 0, -1)

    return img


# In[ ]:


cv2.waitKey(1)
cv2.imshow("img",plot_workspace())


# In[ ]:




