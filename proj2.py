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
        self.Range_X = 100
        seld.Range_Y = 200
        
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

# define a class before this
    # move is valid 
    def Move_is_Allowed(self, Current_X, Current_y):
        return (Current_x >= (1 + self.radius + self.clearance) and Current_x <= (self.Range_X - self.radius - self.clearance) and Current_y >= (1 + self.radius + self.clearance) and Current_y <= (self.Range_Y - self.radius - self.clearance))

    #  action left
    def Action_Left(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x, Current_y - 1) and self.Obstacle_Check(Current_x, Current_y - 1) == False):
            return True
        return False

    # action right
    def Action_Right(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x, Current_y + 1) and self.Obstacle_Check(Current_x, Current_y + 1) == False):
            return True
        return False

    # action up
    def Action_Up(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x - 1, Current_y) and self.Obstacle_Check(Current_x - 1, Current_y) == False):
            return True
        return False

    # action down
    def Action_Down(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x + 1, Current_y) and self.Obstacle_Check(Current_x + 1, Current_y) == False):
            return True
        return False

    # action right up
    def Action_Up_Right(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x - 1, Current_y + 1) and self.Obstacle_Check(Current_x - 1, Current_y + 1) == False):
            return True
        return False

    # action right down
    def Action_Down_Right(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x + 1, Current_y + 1) and self.Obstacle_Check(Current_x + 1, Current_y + 1) == False):
            return True
        return False

    # action left down
    def Action_Down_Left(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x + 1, Current_y - 1) and self.Obstacle_Check(Current_x + 1, Current_y - 1) == False):
            return True
        return False

    # action left up
    def Action_Up_Left(self, Current_x, Current_y):
        if(self.Move_is_Allowed(Current_x - 1, Current_y - 1) and self.Obstacle_Check(Current_x - 1, Current_y - 1) == False):
            return True
        return False

    # if there is an obstacle for trailMap
    def Obstacle_Check(self, x, y):
        Addition = self.clearance + self.radius
        square = 1.4142 * Addition
        
        # check circle
        Distance_Circle = ((x - 160) * (x - 160) + (y - 50) * (y - 50)) - ((15 + Addition)*(15 + Addition))
        
        # check square line equations
        # x>=90 and x<= 110 and y>=40 and y<=60  
        
        if(Distance_Circle <= 0 or (x>=(90 + square)) and (x<= (110 + square)) and (y>= (40+ square)) and y<=(60 + square)):
            return True
        return False

    # Creating final map workspace
    def plot_final_workspace(x_start,y_start,x_goal,y_goal):
    img = 255 * np.ones((200, 300, 3), np.uint8)
    
    #tried in cartesian coordinates
    # Plot the rhombus
    cords_rhombus = np.array([[ 225, 190],[ 250, 175 ], [ 225, 160 ],[ 200 , 175 ]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_rhombus, [0,0,0])
    
    # Plot the circle
    cv2.circle(img, (225, 50), 25, (0, 0, 0), -1)
    
    #Plot the ellipse
    cv2.ellipse(img, (150, 100), (40, 20), 0, 0, 360, (0, 0, 0), -1)
    
    #Plot the rod
    cords_rod = np.array([[ 30.05, 162.50],[ 95, 170 ], [ 103.66, 165 ],[ 38.71 , 157.50 ]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_rod, [0,0,0])
    
    #Plot the polygon (Triangles and parallelogram)
    cords_parallelogram = np.array([[ 75, 80],[100, 50 ], [ 75, 15 ],[ 50, 50 ]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_parallelogram, [0,0,0])
    cords_triangle1 = np.array([[ 25, 15], [ 75, 15 ],[ 50, 50 ]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_triangle1, [0,0,0])
    cords_triangle2 = np.array([[ 20, 80],[25, 15 ],[ 50, 50 ]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_triangle2, [0,0,0])
    
    
    # half plane equations cartesian coordinate
    def check_rhombus(x,y):
    flag1 = False
    flag2 = False
    if 5y + 3x > 1625-radius-clearance and 5y + 3x < 1475+radius+clearance:
        flag1 = True
    if 5y - 3x > 275-radius-clearance and 5y - 3x < 125+radius+clearance:
        flag2 = True
    if flag1 and flag2:
        return False
        print("You are in the rhombus!")
    else:
        return True
    
def check_circle(x,y):
    center = [225, 50]
    dist = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
    
    if dist <= 25+radius+clearance:
        return False
        print("You are in the circle!")
    else:
        return True
    
def check_polygon(x,y):
    flag1 = False
    flag2 = False
    flag3 = False
    if y + 13x > 340-radius-clearance and 5y - 7x < -450+radius+clearance:
        flag1 = True
    if 5y - 6x > -50-radius-clearance and 5y+6x < 850+radius+clearance:
        flag2 = True
    if y + x > 100-radius-clearance and y < 15+radius+clearance:
        flag3 = True
    if flag1 and flag2 and flag3:
        return False
        print("You are in the polygon!")
    else:
        return True

def check_ellipse(x,y):
    center = [150, 100]
    dist = np.sqrt((x - center[0])/20 ** 2 + (y - center[1]) ** 2)/20
    
    if dist <= (20+radius+clearance)**2 +(40+radius+clearance)**2:
        return False
        print("You are in the ellipse!")
    else:
        return True

def check_rod(x,y):
    flag1 = False
    flag2 = False
    if y-0.115x > 159-radius-clearance and y-0.115x < 153+radius+clearance:
        flag1 = True
    if y+0.577x > 180-radius-clearance and y+0.577x < 225+radius+clearance:
        flag2 = True
    if flag1 and flag2:
        return False
        print("You are in the rod!")
    else:
        return True
