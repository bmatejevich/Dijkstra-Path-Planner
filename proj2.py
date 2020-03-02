#!/usr/bin/env python
# coding: utf-8
'''

'''
import math
import numpy as np
import cv2

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
        
start = False        
goal = False


robot = Robot(1,0,[0,0],[10,10])

def check_viableX(point):
    if point >= 0 and point <= 200:
        return True
    else:
        print("invalid")
        return False
def check_viableY(point):
    if point >= 0 and point <= 100:
        return True
    else:
        print("Invalid")
        return False

def check_square(x,y):
    flag1 = False
    flag2 = False
    if x > 90 and x < 110:
        flag1 = True
    if y > 40 or y < 60:
        flag2 = True
    if flag1 and flag2:
        return False
        print("you are in the square!")
    else:
        return True
    
def check_circle(x,y):
    center = [160, 50]
    dist = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
    
    if dist <= 15:
        return False
        print("you are in the circle!")
    else:
        return True
    
while start == False:
    x_start = input("Enter robot x position : ")
    x_start = int(x_start)
    y_start = input("Enter robot y position : ") 
    y_start = int(y_start)
    start = check_viableY(y_start)
    if start == True:
        start = check_viableX(x_start)
        if start ==True:
            start = check_square(x_start,y_start)
            if start == True:
                start = check_circle(x_start,y_start)
    
while goal == False:
    x_goal = input("Enter goal x position : ") 
    x_goal = int(x_goal)
    y_goal = input("Enter goal y position : ") 
    y_goal = int(y_goal)
    goal = check_viableY(y_goal)
    if goal == True:
        goal = check_viableX(x_goal)
        if goal ==True:
            goal = check_square(x_goal,y_goal)
            if goal == True:
                goal = check_circle(x_goal,y_goal)



robot = Robot(1,0,[0,0],[0,0])
robot.start = [x_start,y_start]
robot.goal = [x_goal,y_goal]
#print(robot.start,robot.goal)



def plot_workspace(x_start,y_start,x_goal,y_goal):
    img = 255 * np.ones((100, 200, 3), np.uint8)

    # Plot the square
    cords_square = np.array([[90 , 40 ],[110, 40 ], [110 , 60 ],[90 , 60]], dtype=np.int32)
    
    cv2.fillConvexPoly(img, cords_square, [0,0,0])
    

    # Plot the circle
    cv2.circle(img, (160, 50), 15, (0, 0, 0), -1)
    
    img[y_start,x_start] = [0,0,255]
    img[y_goal,x_goal] = [0,255,0]

    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


    return img



workspace = plot_workspace(x_start,y_start,x_goal,y_goal)

cv2.imshow("img",workspace)
cv2.waitKey(0)



