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
        
def get_min_node(queue):
    min_node = 0
    for node in range(len(queue)):
        if queue[node].cost < queue[min_node].cost:
            min_node = node
    return queue.pop(min_node)

def node_exists(x,y, queue):
    for node in queue:
        if node.x == x and node.y == y:
            return queue.index(node)
        else:
            return None
        
def try_move(move, current_point, radius, clearance):
    if move == 'move_up':
        return move_up(current_point, radius, clearance)
    if move == 'move_down':
        return move_down(current_point, radius, clearance)
    if move == 'move_left':
        return move_left(current_point, radius, clearance)
    if move == 'move_right':
        return move_right(current_point, radius, clearance)
    if move == 'move_up_right':
        return move_up_right(current_point, radius, clearance)
    if move == 'move_up_left':
        return move_up_left(current_point, radius, clearance)
    if move == 'move_down_right':
        return move_down_right(current_point, radius, clearance)
    if move == 'move_down_left':
        return move_down_left(current_point, radius, clearance)

def ways_in(x,y): # a pixel with no obstacles nearby can be achieved from 8 moves
    count = 0
    if y > 0: #from bottom
        count+=1
    if y < 100: #from top
        count+=1
    if x > 0: #from left
        count+=1
    if x < 200: #from right
        count+=1
    if x < 200 and y < 100: #top right
        count+=1
    if x < 200 and y > 0: #top left
        count+=1
    if x > 0 and y > 0: #bottom left
        count+=1
    if x > 0 and y < 100: #bottom right
        count+=1
    return count

def fill_pixel(img,x,y): #fill visited pixes
    img[y,x] = [255,0,0]
    return img

def backtrack(node): #create list of parent node locations
    parentList = list()
    parent = node.parent
    while parent is not None:
        parentList.append(parent)
        parent = parent.parent
    return parentList


def check_viableX(point):
    if point >= 0 and point < 200:
        return True
    else:
        print("Invalid")
        print()
        return False
    
def check_viableY(point):
    if point > 0 and point < 100:
        return True
    else:
        print("Invalid")
        print()
        return False

def check_square(x,y):
    flag1 = False
    flag2 = False
    if x > 90-radius-clearance and x < 110+radius+clearance:
        flag1 = True
    if y > 40-radius-clearance and y < 60+radius+clearance:
        flag2 = True
    if flag1 and flag2:
        return False
        print("You are in the square!")
    else:
        return True
    
def check_circle(x,y):
    center = [160, 50]
    dist = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
    
    if dist <= 15+radius+clearance:
        return False
        print("You are in the circle!")
    else:
        return True


def plot_workspace(x_start,y_start,x_goal,y_goal):
    img = 255 * np.ones((100, 200, 3), np.uint8)

    # Plot the square
    cords_square = np.array([[90 , 40 ],[110, 40 ], [110 , 60 ],[90 , 60]], dtype=np.int32)
    cv2.fillConvexPoly(img, cords_square, [0,0,0])
    
    # Plot the circle
    cv2.circle(img, (160, 50), 15, (0, 0, 0), -1)

    return img

def move_up(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = 1
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x, y - 1]
        return new_point, base_cost
    else:
        return None, None


def move_down(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = 1
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x, y + 1]
        return new_point, base_cost
    else:
        return None, None


def move_left(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = 1
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x - 1, y]
        return new_point, base_cost
    else:
        return None, None


def move_right(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = 1
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x + 1, y]
        return new_point, base_cost
    else:
        return None, None


def move_up_right(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = np.sqrt(2)
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x + 1, y - 1]
        return new_point, base_cost
    else:
        return None, None


def move_up_left(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = np.sqrt(2)
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x - 1, y - 1]
        return new_point, base_cost
    else:
        return None, None


def move_down_right(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = np.sqrt(2)
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x + 1, y + 1]
        return new_point, base_cost
    else:
        return None, None


def move_down_left(point, radius, clearance):
    x = point[0]
    y = point[1]
    base_cost = np.sqrt(2)
    if check_viableX(x) and check_viableY(y) and check_circle(x,y) and check_square(x,y):
        new_point = [x - 1, y + 1]
        return new_point, base_cost
    else:
        return None, None


def djikstra(image, robot):
    radius = robot.radius
    clearance = robot.clearance
    start_node_pos = robot.start
    goal_node_pos = robot.goal
    image[start_node_pos[1], start_node_pos[0]] = [0, 255, 0]
    image[goal_node_pos[1], goal_node_pos[0]] = [0, 0, 255]
    start_node = Node(start_node_pos[0],start_node_pos[1])
    start_node.cost = 0

    waysIn = ways_in(goal_node_pos[0],goal_node_pos[1])
    print("Ways in", waysIn)
    visited = list()
    queue = [start_node]
    moves = ["move_up", "move_down", "move_left", "move_right",
               "move_up_right", "move_down_right", "move_up_left", "move_down_left"]
    counter = 0

    while queue:
        current_node = get_min_node(queue)
        current_point = [current_node.x,current_node.y]
        visited.append(str(current_point))

        for move in moves:
            new_point, base_cost = try_move(move, current_point, radius, clearance)
            if new_point is not None:
                if new_point == goal_node_pos:
                    
                    if counter < waysIn:
                        counter += 1
                        print("Goal reached " +str(counter) + " times")

                new_node = Node(new_point[0],new_point[1])
                new_node.parent = current_node

                image = fill_pixel(image, current_node.x,current_node.y)
                image[start_node_pos[1], start_node_pos[0]] = [0, 255, 0]
                image[goal_node_pos[1], goal_node_pos[0]] = [0, 0, 255]

                resized_new_1 = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
                cv2.imshow("Map", resized_new_1)
                cv2.waitKey(1)
                
                if str(new_point) not in visited:
                    new_node.cost = base_cost + new_node.parent.cost
                    visited.append(str(new_point))
                    queue.append(new_node)
                else:
                    node_exist_index = node_exists(new_point[0],new_point[0], queue)
                    if node_exist_index is not None:
                        temp_node = queue[node_exist_index]
                        if temp_node.cost > base_cost + new_node.parent.cost:
                            temp_node.cost = base_cost + new_node.parent.cost
                            temp_node.parent = current_node
            else:
                continue
        if counter == waysIn:
            return new_node.parent, image
    return None, None

#################################################
start = False
goal = False
radius = 0
clearance = 0

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





y_start = 100 - y_start
y_goal = 100 - y_goal

start_node = [x_start,y_start]
goal_node = [x_goal,y_goal]

#change these values for point/rigid robot
radius = 1
clearance = 3

robot1 = Robot(radius, clearance, start_node, goal_node)



workspace = plot_workspace(x_start,y_start,x_goal,y_goal)


solution, image = djikstra(workspace, robot1)

if solution is not None:
    parent_list = backtrack(solution)
    for parent in parent_list:
        x = parent.x
        y = parent.y
        image[y, x] = [0, 255, 0]
        img = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        cv2.imshow("Map", img)
        cv2.waitKey(150)
else:
    print("No path")

cv2.waitKey(0)
cv2.destroyAllWindows()


