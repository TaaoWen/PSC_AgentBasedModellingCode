# main.py
'''
Agent Based Modelling
This Python code is a used as the practicals (Agent Based Modelling) for the module "Programming for Social Science".
This is the main file, and Agents classes are stored in "agentframework.py". 
More detail can be found in comments below.

@author: Tao Wen
@Version: Final
'''

# =============================================================================
# # ####################################Pay attention (Read before simulation)####################################
# # Please use "Ctrl + 5" to remove the comments for code block surrounded by "==="
# # Please use "Ctrl + 4" to comment in code block surrounded by "==="
# # Please use "Ctrl + 1" to remove or add comments for multiple lines together
# # It will be very troublesome and may introduce ERRORS if adding or removing "#" manually line by line!
# # If there is any problem, please contact me via taaowen@gmail.com
# # or read "http://e-callisto.org/cospar2018/SpyderKeyboardShortcutsEditor.pdf", the top of the 2nd page
# =============================================================================


import sys
import random
import operator
import time
import tkinter
import matplotlib
# Please uncomment next line to design GUI, but comment in the next line for other figures and outcomes
#matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import requests
import bs4

# Function: Write total amount stored by all the agents to txt file
def write_store_to_output(write_str):
    """
    Write total amount stored by all the agents to "output_store.txt"
    Note: The output does not contain the initial total amount 
    because it is 0 by default setting
    
    Parameters
    ----------
    write_str: str
        str needs to be output in the .txt file
    """
    # open the .txt file
    with open("output_store.txt", "a+") as f:
        f.write(write_str) # wirte the str
        f.write("\n") # New line
        
# Function: Write environment to txt file
def write_environment_to_output(write_str):
    """
    Write environment to "output_environment.txt"
    The size of the matrix of the environment is the same as the matrix read 
    from "in.txt" because the code only changes the value of element and does 
    not change the size
    
    Parameters
    ----------
    write_str: str
        str needs to be output in the .txt file
    """
    # open the .txt file
    with open("output_environment.txt", "a+") as f:
        # Each line of the environment (**apart from** the last one in each line)
        for j in range(len(write_str)-1):
            f.write(str(write_str[j])) # Write each line **apart from** the last one
            f.write(',') # wirte ","
        f.write(str(write_str[-1])) # Write out the last value WITHOUT "," at the end of each line
        f.write("\n") # New line

# Function: Obtain the distance between two agents based on the Euclidean Distance
def distance_between(agents_row_a, agents_row_b):
    """
    Obtain the distance between two agents based on the Euclidean Distance
    
    Parameters
    ----------
    agents_row_a: agentframework.Agent
        The framework of the first agent 
    agents_row_b: agentframework.Agent
        The framework of the second agent
    
    Returns
    -------
    distance_obtain: float
        The distance between two agents based on Euclidean distance
    """
    # Euclidean Distance
    distance_obtain = (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
    return distance_obtain

# Function: Calculate the distance between each pair of agent based on function "calculate_distance_0"
def calculate_distance_0(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA and agentB are both from 1 to end, and agentA != agentB
    
    Parameters
    ----------
    agents: list
        The list of agents
        
    Returns
    -------
    need_time: float
        Timing needed to obtain the distance for all pair of agents based on this function
    max_dis: float
        The maximum distance between agents
    min_dis: float
        The minimum distance between agents
    """
    # Initial setting for max and min distance
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time() # Time begin
    # agentA and agentB are both from 1 to end
    for i in range(0, num_of_agents, 1):
        for j in range(0, num_of_agents, 1):
            # agentA != agentB
            if i != j:
#                # Uncomment next line to print the distance between each pair of agents
#                print("The distance between Agent", agents_row_a.ID, \
#                      "and Agent", agents_row_b.ID, \
#                      "is", distance_between(agents_row_a, agents_row_b))
                
                # Update the max and min distance
                max_dis = max(max_dis, distance_between(agents[i], agents[j]))
                min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time() # Time end
    need_time = end_time - start_time # Time calculate
#    # Uncomment next lines to print the max and min distances, as well as the timing
#    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
#    print("Running time is", need_time)
    return need_time, max_dis, min_dis

# Function: Calculate the distance between each pair of agent based on function "calculate_distance_1"
def calculate_distance_1(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA and agentB are both from 1 to end, but the distance is ONLY calculated
    when agents_row_a.ID > agents_row_b.ID
    
    Parameters
    ----------
    agents: list
        The list of agents
        
    Returns
    -------
    need_time: float
        Timing needed to obtain the distance for all pair of agents based on this function
    max_dis: float
        The maximum distance between agents
    min_dis: float
        The minimum distance between agents
    """
    # Initial setting for max and min distance
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time() # Time begin
    # agentA and agentB are both from 1 to end
    for i in range(0, num_of_agents, 1):
        for j in range(0, num_of_agents, 1):
            # distance is ONLY calculated when agents_row_a.ID > agents_row_b.ID
            if i > j:
#                # Uncomment next line to print the distance between each pair of agents
#                print("The distance between Agent", agents_row_a.ID, \
#                      "and Agent", agents_row_b.ID, \
#                      "is", distance_between(agents_row_a, agents_row_b))
                
                # Update the max and min distance
                max_dis = max(max_dis, distance_between(agents[i], agents[j]))
                min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time() # Time end
    need_time = end_time - start_time # Time calculate
#    # Uncomment next lines to print the max and min distances, as well as the timing
#    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
#    print("Running time is", need_time)
    return need_time, max_dis, min_dis

# Function: Calculate the distance between each pair of agent based on function "calculate_distance_2"
def calculate_distance_2(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA is from 1 to end, agentB is from agentA to end (NOT include agentA)
    
    Parameters
    ----------
    agents: list
        The list of agents
        
    Returns
    -------
    need_time: float
        Timing needed to obtain the distance for all pair of agents based on this function
    max_dis: float
        The maximum distance between agents
    min_dis: float
        The minimum distance between agents
    """
    # Initial setting for max and min distance
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time() # Time begin
    # agentA is from 1 to end
    for i in range(0, num_of_agents, 1):
        # agentB is from agentA to end (NOT include agentA)
        for j in range(i + 1, num_of_agents, 1):
#            # Uncomment next line to print the distance between each pair of agents
#            print("The distance between Agent", agents_row_a.ID, \
#                  "and Agent", agents_row_b.ID, \
#                  "is", distance_between(agents_row_a, agents_row_b))
            
            # Update the max and min distance
            max_dis = max(max_dis, distance_between(agents[i], agents[j]))
            min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time() # Time end
    need_time = end_time - start_time # Time calculate
#    # Uncomment next lines to print the max and min distances, as well as the timing
#    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
#    print("Running time is", need_time)
    return need_time, max_dis, min_dis


# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # # Code below is for initial setting
# # # =============================================================================
# # =============================================================================

# Environment and other setting
random.seed(0) # This line can be removed for randomization

num_of_iterations = 50 # Number of iterations
environment = [] # List of environment that will be read later

# Sheep setting, please note "sheep" and "agent" are the same meaning in this code
agents = [] # List of sheep (agent) that will be given later
num_of_agents = 10 # Number of sheep
neighbourhood = 20 # Sheep share store with neighbor sheep within this distance "neighbourhood"
times_for_move = 1.1 # Sheep move quickly if their store is "times_for_move" times the average storage
born_iteration_sheep = 5 # New sheep are born every "born_iteration_sheep" iterations
new_sheep_partion = 0.2 # The number of new sheep is "new_sheep_partion" of the number of alive sheep

# Wolves setting
wolves = [] # List of wolves that will be given later
num_of_wolves = 5 # Number of wolves
required_distance = 30 # Wolves eat sheep within this distance "required_distance"
unit_step_wovle = 5 # The unit that the wolf moves at each iteration in each direction
born_iteration_wolves = 10 # New wolves are born every "born_iteration_sheep" iterations
new_wolves_partion = 0.2 # The number of new wolves is "new_wolves_partion" of the number of alive wolves
wolves_dead_criterion = 5 # Wolves die when they eat "wolves_dead_criterion" sheep 

# Please NOTE
# Living sheep are represented by blue points and dead sheep are represented by red points
# Living wolves are represented by black points and dead wolves are represented by yellow points
    

# =============================================================================
# # Uncomment next lines to read model parameters from the command line
# # The input will replace the value given above, so do not need to comment in lines above
# num_of_agents = int(sys.argv[1]) # Number of sheep
# num_of_iterations = int(sys.argv[2]) # Number of iterations
# neighbourhood = int(sys.argv[3]) # Sheep share store with neighbor sheep within this distance "neighbourhood"
# =============================================================================

# Read the environment from txt file
f = open("in.txt") # open the file
for line in f: # read all lines
    parsed_line = str.split(line,",") # divide each line by ","
    rowlist = [] # line initializing
    for value in parsed_line: # read all numbers in one line
        rowlist.append(float(value))
    environment.append(rowlist) 
f.close() # close the file

# =============================================================================
# # Uncomment next lines to visualize the environment without agents
# matplotlib.pyplot.xlim(0, len(environment[0])) # range of x axis
# matplotlib.pyplot.ylim(0, len(environment)) # range of y axis
# matplotlib.pyplot.imshow(environment) # show the figure
# matplotlib.pyplot.show()
# =============================================================================

# Make the wovles, the number is "num_of_wolves"
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#    # Uncomment next line to print the initial position of all wovles
#    print(wolves[i])

# Make the sheep, the number is "num_of_agents"
for i in range(num_of_agents):
    # Position is randomly given by default, you can also input the position of agents 
    # by using "agents.append(agentframework.Agent(environment,agents,i,ypos,xpos))"
    # where "ypos" and "xpos" are "float" that indicate the position of this agent
    # More details can be found in the next code block 
    agents.append(agentframework.Agent(environment,agents,i))
#    # Uncomment next line to print the initial position of all sheep
#    print(agents[i])

# =============================================================================
# # Uncomment next lines to read the agent position from website
# # Please comment in "Make the sheep" code bloak above if you want to read position from website (this code block)
# r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
# content = r.text
# soup = bs4.BeautifulSoup(content, 'html.parser')
# td_ys = soup.find_all(attrs={"class" : "y"})
# td_xs = soup.find_all(attrs={"class" : "x"})
# 
# for i in range(num_of_agents):
#     y = int(td_ys[i].text)
#     x = int(td_xs[i].text)
#     agents.append(agentframework.Agent(environment, agents, i, y, x))
# #    # Uncomment next line to print the initial position of all agents
# #    print(agents[i])
# =============================================================================

# =============================================================================
# # Uncomment next lines to test if "distance_between" function can work normally.
# print("The position of agent A is", agents[0]) # information of agent A
# print("The position of agent B is", agents[1]) # information of agent B
# print("The distance between agent A and B is", distance_between(agents[0],agents[1])) # distance between agent A and B
# =============================================================================

# =============================================================================
# # Uncomment next lines to find the agent with the largest x (furthest east)
# matplotlib.pyplot.xlim(0, len(environment[0])) # range of x axis
# matplotlib.pyplot.ylim(0, len(environment)) # range of y axis
# for i in range(num_of_agents): # all agents are given in black color
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'black')
# sorted_agents = sorted(agents, key = lambda a: a.x) # sort the agent based on x
# # agent with largest x is given by red color
# matplotlib.pyplot.scatter(sorted_agents[len(agents)-1].x,sorted_agents[len(agents)-1].y, color = 'red')
# matplotlib.pyplot.show()
# =============================================================================

# =============================================================================
# # Uncomment next lines to obtain the timings, the maximum distances, 
# # and the minimum distances from three functions
# need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
# need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
# need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
# =============================================================================

# =============================================================================
# # Uncomment next lines to obtain the timings for three function under different number of agents
# num_of_agents_list = [10,20,50,100,200,500,1000,2000] # To test the timings for different number of agents
# # timing initializing
# running_time0 = []
# running_time1 = []
# running_time2 = []
# for num_of_agents in num_of_agents_list:
#     # Print the current number of agents
#     print("Now, the number of agents is", num_of_agents)
#     agents = []
#     # make the agents
#     for i in range(num_of_agents):
#         # Position is randomly given by default, you can input the position manually (refer to comments above)
#         agents.append(agentframework.Agent(environment, agents, i))
# #        # Uncomment next line to print the initial position of all agents
# #        print(agents[i])
#     
#     # obtain the timings, the maximum distances, and the minimum distances from three functions
#     need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
#     running_time0.append(need_time0)
#     need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
#     running_time1.append(need_time1)
#     need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
#     running_time2.append(need_time2)
#     
# # Calculate the maximum time it takes for any run, then set the axis limit
# max_time = max(running_time0)
# max_time = max(max_time, max(running_time1))
# max_time = max(max_time, max(running_time2))
# # Set the axis limits
# matplotlib.pyplot.ylim(0, 1.1 * max(num_of_agents_list))
# matplotlib.pyplot.xlim(0, 1.1 * max_time)
# # visualize the timings obtained from different functions
# for i in range(len(num_of_agents_list)):
#     # Please note the color for each function
#     matplotlib.pyplot.scatter(running_time0[i],num_of_agents_list[i], color="red")
#     matplotlib.pyplot.scatter(running_time1[i],num_of_agents_list[i], color="black")
#     matplotlib.pyplot.scatter(running_time2[i],num_of_agents_list[i], color="green")
# # name of label and legend
# matplotlib.pyplot.xlabel("Timing")
# matplotlib.pyplot.ylabel("Number of agents")
# matplotlib.pyplot.legend(["Function0","Function1","Function2"])
# matplotlib.pyplot.show() 
# =============================================================================

# =============================================================================
# # Uncomment next lines to test if each agent has the information of other agents.
# print("This is the original information from Agent 1:", agents[1])
# print("This is the information of Agent 1 from Agent 0:", agents[0].agents[1])
# =============================================================================

# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # # Code above is for initial setting
# # # =============================================================================
# # =============================================================================





# =============================================================================
# # =============================================================================
# # # Code below is for Basic figures
# # =============================================================================
# =============================================================================

# =============================================================================
# for j in range(num_of_iterations): # each iteration
# #    # Uncomment next line to randomise the order of agents if you want
# #    # and you can also uncomment the code block below to obtain the normal order
# #    random.shuffle(agents)
#     
#     # Obtain the average store of all agents before actions
#     store_total = 0
#     for i in range(num_of_agents):
#         store_total += agents[i].store
#     store_average = store_total/num_of_agents
# #    # Uncomment next line to print the average store of all agents in this step
# #    print("Average store for step", j, "is", store_average)
#     
# #    # Uncomment next line to print the step of the movement
# #    print("It is", j, "step")
#     
#     # Action of the sheep
#     for i in range(num_of_agents): # each sheep
#         if agents[i].state == 1: # Only living sheep can move, eat, and share
# #            # Uncomment next line to print the position of agent before moving
# #            print("Before moving",agents[i])
#             agents[i].move(times_for_move,store_average) # move
# #            # Uncomment next line to print the position of agent after moving
# #            print("After moving",agents[i])
#             
#             agents[i].eat() # sheep eat the environment, they will not leave negative values and sick up their store
#             agents[i].share_with_neighbours(neighbourhood) # Share the stores with neighbour agents within the distance
#             
# #            # Uncomment next line to print the position of each agent in each step
# #            print(agents[i])
#     
#     # Action of the wolves
#     for i in range(num_of_wolves): # each wolf
#         # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
#         if wolves[i].eatSheep >= wolves_dead_criterion:
#             wolves[i].state = 0 # die
#         
#         # living wolf eats and moves
#         if wolves[i].state == 1:
#             wolves[i].move(unit_step_wovle) # move
#             wolves[i].find_eat(required_distance) # eat sheep within the distance
#         
# #    # Uncomment next line to check the state of sheep
# #    for i in range(num_of_agents):
# #        print("The state for sheep " + str(agents[i].ID) \
# #                  + " is " + str(agents[i].state))
# 
#     # New sheep born
#     if (j + 1) % born_iteration_sheep == 0: # identify the step that is suitable to born
#         # Measure the number of living sheep
#         alive_number = 0 # initializing
#         for i in range(num_of_agents):
#             if agents[i].state == 1:
#                 alive_number += 1
#         # add_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_sheep_partion * alive_number)
#         # Current (new) number of sheep
#         new_num_of_agents = num_of_agents + add_number
#         # make the position of the new sheep (from "num_of_agents" to "new_num_of_agents")
#         for i in range(num_of_agents,new_num_of_agents,1):
#             agents.append(agentframework.Agent(environment,agents,i))
#         # Update the number of sheep
#         num_of_agents = new_num_of_agents
# #        print("Current total number of sheep is",num_of_agents)
#     
#     # New wolves born
#     if (j + 1) % born_iteration_wolves == 0: # identify the step that is suitable to born
#         # Measure the number of living wolves
#         alive_number = 0 # initializing
#         for i in range(num_of_wolves):
#             if wolves[i].state == 1:
#                 alive_number += 1
#         # add_number is the new wolves born from the living wolves (rounding)
#         add_number = round(new_wolves_partion * alive_number)
#         # Current (new) number of wolves
#         new_num_of_wolves = num_of_wolves + add_number
#         # make the position of the new wolves (from "num_of_wolves" to "new_num_of_wolves")
#         for i in range(num_of_wolves,new_num_of_wolves,1):
#             wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#         # Update the number of wolves
#         num_of_wolves = new_num_of_wolves
# #        print("Current total number of wolves is",num_of_wolves)
# 
# # =============================================================================
# #     # Uncomment next lines to output total amount stored by all the agents to txt file
# #     # The output does not contain the initial total amount because it is 0 by default setting
# #     totalStored = 0 # initializing
# #     for i in range(num_of_agents):
# #         totalStored += agents[i].store
# #     # write the str to txt file
# #     write_store_to_output("After the movement and eating of step " + str(j) + \
# #                           ", and the total amount stored by all the agents is " + str(totalStored))
# # =============================================================================
# 
# # Uncomment next lines to display environment and agent
# matplotlib.pyplot.xlim(0, len(environment[0]))
# matplotlib.pyplot.ylim(0, len(environment))
# matplotlib.pyplot.imshow(environment)
# #print("Final states")
# for i in range(num_of_agents): # visualize the sheep
# #    # Uncomment next lines to print the state for all sheep at the end.
# #    print("The state for sheep", agents[i].ID, "is", agents[i].state)
#     
#     # Living sheep are represented by blue points and dead sheep are represented by red points
#     if agents[i].state == 1: # Living sheep
#         matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
#     else: # Dead sheep
#         matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
#         
# for i in range(num_of_wolves): # visualize the wolves
# #    # Uncomment next lines to print the state for all wolves at the end.
# #    print("Wolf", wolves[i].ID, "eated total", wolves[i].eatSheep, "sheep")
#     
#     # Living wolves are represented by black points and dead wolves are represented by yellow points
#     if wolves[i].state == 1: # Living wolves
#         matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
#     else: # Dead wolves
#         matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
# matplotlib.pyplot.show()
# 
# # =============================================================================
# # # Uncomment next lines to write out the environment as .txt file
# # for i in range(len(environment)):
# #     write_environment_to_output(environment[i])
# # =============================================================================
# 
# # =============================================================================
# # # Uncomment next lines to obtain the normal order if using 'shuffle' function above
# # print("Random order")
# # for i in range(num_of_agents): # print the agents in random order
# #     print(agents[i])
# # sorted_agents = sorted(agents, key = lambda a: a.ID) # sort based on ID
# # print("Normal order")
# # for i in range(num_of_agents): # print the agents in normal order
# #     print(sorted_agents[i])
# # =============================================================================
# =============================================================================

# =============================================================================
# # =============================================================================
# # # Code above is for Basic figures
# # =============================================================================
# =============================================================================









# =============================================================================
# # =============================================================================
# # # Code below is for Animation
# # =============================================================================
# =============================================================================
    
# =============================================================================
# # Figure initializing
# fig = matplotlib.pyplot.figure(figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1])
# 
# # Parameters initializing
# carry_on = True	# stop or not
# jIteration = 0 # iteration indicator
# 
# # update (main) function for Animation
# def update(frame_number):
#     
#     fig.clear() 
#     # Parameter globalization  
#     global jIteration
#     global num_of_agents
#     global num_of_wolves
#     global carry_on
#     
#     # Plot the environment before agents
#     matplotlib.pyplot.xlim(0, len(environment[0]))
#     matplotlib.pyplot.ylim(0, len(environment))
#     matplotlib.pyplot.imshow(environment)
#     
#     # Obtain the average store of all agents before actions
#     store_total = 0
#     for i in range(num_of_agents):
#         store_total += agents[i].store
#     store_average = store_total/num_of_agents
#     
#     # Action of the sheep
#     for i in range(num_of_agents): # each sheep
#         if agents[i].state == 1: # Only living sheep can move, eat, and share
#             agents[i].move(times_for_move,store_average) # move
#             agents[i].eat() # sheep eat the environment, they will not leave negative values and sick up their store
#             agents[i].share_with_neighbours(neighbourhood) # Share the stores with neighbour agents within the distance
#             
#     # Action of the wolves
#     for i in range(num_of_wolves): # each wolf
#         # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
#         if wolves[i].eatSheep >= wolves_dead_criterion:
#             wolves[i].state = 0 # die
#         
#         # Wolf eats and moves
#         if wolves[i].state == 1:  # living wolves
#             wolves[i].move(unit_step_wovle) # move
#             wolves[i].find_eat(required_distance) # eat sheep within the distance
#     
#     # New sheep born
#     if (jIteration + 1) % born_iteration_sheep == 0: # identify the step that is suitable to born
#         # Measure the number of living sheep
#         alive_number = 0 # initializing
#         for i in range(num_of_agents):
#             if agents[i].state == 1:
#                 alive_number += 1
#         # add_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_sheep_partion * alive_number)
#         # Current (new) number of sheep
#         new_num_of_agents = num_of_agents + add_number
#         # make the position of the new sheep (from "num_of_agents" to "new_num_of_agents")
#         for i in range(num_of_agents,new_num_of_agents,1):
#             agents.append(agentframework.Agent(environment,agents,i))
#         # Update the number of sheep
#         num_of_agents = new_num_of_agents
# #        print("Current total number of sheep is",num_of_agents)
#     
#     # New wolves born
#     if (jIteration + 1) % born_iteration_wolves == 0:
#         # Measure the number of living wolves
#         alive_number = 0 # initializing
#         for i in range(num_of_wolves):
#             if wolves[i].state == 1:
#                 alive_number += 1
#         # add_number is the new wolves born from the living wolves (rounding)
#         add_number = round(new_wolves_partion * alive_number)
#         # Current (new) number of wolves
#         new_num_of_wolves = num_of_wolves + add_number
#         # make the position of the new wolves (from "num_of_wolves" to "new_num_of_wolves")
#         for i in range(num_of_wolves,new_num_of_wolves,1):
#             wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#         # Update the number of wolves
#         num_of_wolves = new_num_of_wolves
# #        print("Current total number of wolves is",num_of_wolves)
#     
#     jIteration += 1 # iteration + 1 manually
#     
#     # Stop condiction based on a random number
#     if random.random() < 0.001:
#         carry_on = False # stop indicator
#         print("stopping condition")
#     
#     # Plot the sheep and wolves in this iteration
#     for i in range(num_of_agents): # visualize the sheep
#         # Living sheep are represented by blue points and dead sheep are represented by red points
#         if agents[i].state == 1: # Living sheep
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
#         else: # Dead sheep
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
#     for i in range(num_of_wolves): # visualize the wolves
#         # Living wolves are represented by black points and dead wolves are represented by yellow points
#         if wolves[i].state == 1: # Living wolves
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
#         else: # Dead wolves
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
# 
# 		
# # Stop condition function: (1) Step number (2) Random number
# def gen_function(b = [0]):
#     a = 0
#     global carry_on #Not actually needed as we're not assigning, but clearer
#     while (a < num_of_iterations) & (carry_on) : # two stop conditions
#         yield a			# Returns control and waits next call.
#         a = a + 1
# 
# # Animation
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
# 
# matplotlib.pyplot.show()
# =============================================================================

# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # # Code above is for Animation
# # # =============================================================================
# # =============================================================================










# =============================================================================
# # =============================================================================
# # # Code below is for GUI Setting
# # =============================================================================
# =============================================================================
    
# Define the run function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
# Figure initializing
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# GUI design setting
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# Parameters initializing
carry_on = True # stop or not
jIteration = 0 # iteration indicator

# update (main) function for Animation
def update(frame_number):
    
    fig.clear()
    # Parameter globalization 
    global jIteration
    global num_of_agents
    global num_of_wolves
    global carry_on
    
    # Plot the environment before agents
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment)
    
    # Obtain the average store of all agents before actions
    store_total = 0
    for i in range(num_of_agents):
        store_total += agents[i].store
    store_average = store_total/num_of_agents
    
    # Action of the sheep
    for i in range(num_of_agents): # each sheep
        if agents[i].state == 1: # Only living sheep can move, eat, and share
            agents[i].move(times_for_move,store_average) # move
            agents[i].eat() # sheep eat the environment, they will not leave negative values and sick up their store
            agents[i].share_with_neighbours(neighbourhood) # Share the stores with neighbour agents within the distance
    
    # Action of the wolves
    for i in range(num_of_wolves): # each wolf
        # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
        if wolves[i].eatSheep >= wolves_dead_criterion:
            wolves[i].state = 0 # die
        
        # Wolf eats and moves
        if wolves[i].state == 1: # living wolves
            wolves[i].move(unit_step_wovle) # move
            wolves[i].find_eat(required_distance) # eat sheep within the distance
    
    # New sheep born
    if (jIteration + 1) % born_iteration_sheep == 0: # identify the step that is suitable to born
        # Measure the number of living sheep
        alive_number = 0 # initializing
        for i in range(num_of_agents):
            if agents[i].state == 1:
                alive_number += 1
        # add_number is the new sheep born from the living sheep (rounding)
        add_number = round(new_sheep_partion * alive_number)
        # Current (new) number of sheep
        new_num_of_agents = num_of_agents + add_number
        # make the position of the new sheep (from "num_of_agents" to "new_num_of_agents")
        for i in range(num_of_agents,new_num_of_agents,1):
            agents.append(agentframework.Agent(environment,agents,i))
        # Update the number of sheep
        num_of_agents = new_num_of_agents
#        print("Current total number of sheep is",num_of_agents)
    
    # New wolves born
    if (jIteration + 1) % born_iteration_wolves == 0:
        # Measure the number of living wolves
        alive_number = 0
        for i in range(num_of_wolves):
            if wolves[i].state == 1:
                alive_number += 1
        # add_number is the new wolves born from the living wolves (rounding)
        add_number = round(new_wolves_partion * alive_number)
        # Current (new) number of wolves
        new_num_of_wolves = num_of_wolves + add_number
        # make the position of the new wolves (from "num_of_wolves" to "new_num_of_wolves")
        for i in range(num_of_wolves,new_num_of_wolves,1):
            wolves.append(agentframework.Wolves(wolves,agents,environment,i))
        # Update the number of wolves
        num_of_wolves = new_num_of_wolves
#        print("Current total number of wolves is",num_of_wolves)
    
    jIteration += 1 # iteration + 1 manually
    
    # Stop condiction based on a random number
    if random.random() < 0.001:
        carry_on = False # stop indicator
        print("stopping condition")
    
    # Plot the sheep and wolves in this iteration
    for i in range(num_of_agents): # visualize the sheep
        # Living sheep are represented by blue points and dead sheep are represented by red points
        if agents[i].state == 1: # Living sheep
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
        else: # Dead sheep
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
    for i in range(num_of_wolves): # visualize the wolves
        # Living wolves are represented by black points and dead wolves are represented by yellow points
        if wolves[i].state == 1: # Living wolves
            matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
        else: # Dead wolves
            matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')

		
# Stop condition function: (1) Step number (2) Random number
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) : # two stop conditions
        yield a			# Returns control and waits next call.
        a = a + 1

tkinter.mainloop()

# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # # Code above is for GUI Setting
# # # =============================================================================
# # =============================================================================