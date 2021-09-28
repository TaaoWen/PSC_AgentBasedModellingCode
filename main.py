# main.py
'''
Agent Based Modelling

@author: Tao Wen
@Version: 0.00
'''

# =============================================================================
# # ####################################Pay attention####################################
# # Please use "Ctrl + 5" to remove the comments for code block surrounded by "==="
# # Please use "Ctrl + 4" to comment in code block surrounded by "==="
# # Please use "Ctrl + 1" to remove or add comments for multiple lines
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
    with open("output_store.txt", "a+") as f:
        f.write(write_str)
        f.write("\n")
        
# Function: Write environment to txt file
def write_environment_to_output(write_str):
    with open("output_environment.txt", "a+") as f:
        for j in range(len(write_str)-1):
            f.write(str(write_str[j]))
            f.write(',')
        # Write out the last value without "," at the end
        f.write(str(write_str[-1]))
        # New line
        f.write("\n")

# Function: Obtain the distance between two agents
def distance_between(agents_row_a, agents_row_b):
    """
    Obtain the distance between two agents
    
    :param agents_row_a: First agent 
    :param agents_row_b: Second agent
    
    :return: The distance between two agents based on Euclidean distance
    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Function: Calculate the distance between each pair of agent
def calculate_distance_0(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA and agentB are all from 1 to end, and agentA != agentB
    
    :param agents: Agent list
    
    :return: need_time: Timing needed to obtain the distance
    :return: max_dis: The maximum distance between agents
    :return: min_dis: The minimum distance between agents
    """
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time()
    for i in range(0, num_of_agents, 1):
        for j in range(0, num_of_agents, 1):
            if i != j:
#                # Uncomment next line to print the distance between each pair of agents
#                print("The distance between Agent", agents_row_a.ID, \
#                      "and Agent", agents_row_b.ID, \
#                      "is", distance_between(agents_row_a, agents_row_b))
                max_dis = max(max_dis, distance_between(agents[i], agents[j]))
                min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time()
    need_time = end_time - start_time
#    # Uncomment next lines to print the max and min distances, as well as the timing
#    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
#    print("Running time is", need_time)
    return need_time, max_dis, min_dis

# Function: Calculate the distance between each pair of agent
def calculate_distance_1(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA and agentB are all from 1 to end, but the distance is only calculated
    when agents_row_a.ID > agents_row_b.ID
    
    :param agents: Agent list
    
    :return: need_time: Timing needed to obtain the distance
    :return: max_dis: The maximum distance between agents
    :return: min_dis: The minimum distance between agents
    """
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time()
    for i in range(0, num_of_agents, 1):
        for j in range(0, num_of_agents, 1):
            if i > j:
#                # Uncomment next line to print the distance between each pair of agents
#                print("The distance between Agent", agents_row_a.ID, \
#                      "and Agent", agents_row_b.ID, \
#                      "is", distance_between(agents_row_a, agents_row_b))
                max_dis = max(max_dis, distance_between(agents[i], agents[j]))
                min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time()
    need_time = end_time - start_time
#    # Uncomment next lines to print the max and min distances, as well as the timing
#    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
#    print("Running time is", need_time)
    return need_time, max_dis, min_dis

# Function: Calculate the distance between each pair of agent
def calculate_distance_2(agents):
    """
    Obtain the timing to calculate the distance between each pair of nodes,
    where agentA is from 1 to end, agentB is from agentA to end (not include agentA)
    
    :param agents: Agent list
    
    :return: need_time: Timing needed to obtain the distance
    :return: max_dis: The maximum distance between agents
    :return: min_dis: The minimum distance between agents
    """
    max_dis = distance_between(agents[0], agents[1])
    min_dis = max_dis
    
    start_time = time.time()
    for i in range(0, num_of_agents, 1):
        for j in range(i + 1, num_of_agents, 1):
#            # Uncomment next line to print the distance between each pair of agents
#            print("The distance between Agent", agents_row_a.ID, \
#                  "and Agent", agents_row_b.ID, \
#                  "is", distance_between(agents_row_a, agents_row_b))
            max_dis = max(max_dis, distance_between(agents[i], agents[j]))
            min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time()
    need_time = end_time - start_time
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

# Sheep setting
agents = [] # List of agents that will be given later
num_of_agents = 10 # Number of agents
neighbourhood = 20 # Agents share store with neighbor agents within this distance "neighbourhood"
times_for_move = 1.1 # Agents move quickly if their store is "times_for_move" times the average storage
born_iteration_sheep = 5 # New agents are born every "born_iteration_sheep" iterations
new_sheep_partion = 0.2 # The number of new sheep is "new_sheep_partion" of the number of alive sheep

# Wolves setting
wolves = [] # List of agents that will be given later
num_of_wolves = 5 # Number of wolves
required_distance = 30 # Wolves eat sheep within this distance "required_distance"
unit_step_wovle = 5 # The unit that the wolf moves at each iteration in each direction
born_iteration_wolves = 10 # New wolves are born every "born_iteration_sheep" iterations
new_wolves_partion = 0.2 # The number of new wolves is "new_wolves_partion" of the number of alive wolves
wolves_dead_criterion = 5 # Wolves die when they eat "wolves_dead_criterion" sheep 

# Living sheep are represented by blue points and dead sheep are represented by red points
# Living wolves are represented by black points and dead wolves are represented by yellow points
    

# =============================================================================
# # Uncomment next lines to read model parameters from the command line
# num_of_agents = int(sys.argv[1])
# num_of_iterations = int(sys.argv[2])
# neighbourhood = int(sys.argv[3])
# =============================================================================

# Read the environment from txt file
f = open("in.txt")
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for value in parsed_line:
        rowlist.append(float(value))
    environment.append(rowlist)
f.close()

# =============================================================================
# # Uncomment next lines to visualize the environment
# matplotlib.pyplot.xlim(0, len(environment[0]))
# matplotlib.pyplot.ylim(0, len(environment))
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()
# =============================================================================

# Make the wovles
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#    # Uncomment next line to print the initial position of all agents
#    print(wolves[i])

# Make the agents
# Position by default
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,i))
#    # Uncomment next line to print the initial position of all agents
#    print(agents[i])

# =============================================================================
# # Uncomment next lines to read the agent position from website
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
# print("The position of agent A is", agents[0])
# print("The position of agent B is", agents[1])
# print("The distance between agent A and B is", distance_between(agents[0],agents[1]))
# =============================================================================

# =============================================================================
# # Uncomment next lines to find the agent with the largest x (furthest east)
# matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.ylim(0, 99)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'black')
# sorted_agents = sorted(agents, key = lambda a: a.x)
# matplotlib.pyplot.scatter(sorted_agents[len(agents)-1].x,sorted_agents[len(agents)-1].y, color = 'red')
# matplotlib.pyplot.show()
# =============================================================================

# =============================================================================
# # Uncomment next lines to obtain the timings, the maximum and the minimum distances for three functions
# need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
# need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
# need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
# =============================================================================

# =============================================================================
# # Uncomment next lines to obtain the timings for three function under different number of agents
# num_of_agents_list = [10,20,50,100,200,500,1000,2000]
# running_time0 = []
# running_time1 = []
# running_time2 = []
# for num_of_agents in num_of_agents_list:
#     # Print the current number of agents
#     print("Now, the number of agents is", num_of_agents)
#     agents = []
#     for i in range(num_of_agents):
#         agents.append(agentframework.Agent(environment, agents, i, y, x))
# #    # Uncomment next line to print the initial position of all agents
# #    print(agents[i])
#     
#     need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
#     running_time0.append(need_time0)
#     need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
#     running_time1.append(need_time1)
#     need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
#     running_time2.append(need_time2)
#     
# # Calculate the maximum time it takes for any run. 
# max_time = max(running_time0)
# max_time = max(max_time, max(running_time1))
# max_time = max(max_time, max(running_time2))
# # Set the axis limits
# matplotlib.pyplot.ylim(0, 1.1 * max(num_of_agents_list))
# matplotlib.pyplot.xlim(0, 1.1 * max_time)
# # Plot the timings in a graph
# for i in range(len(num_of_agents_list)):
#     matplotlib.pyplot.scatter(running_time0[i],num_of_agents_list[i], color="red")
#     matplotlib.pyplot.scatter(running_time1[i],num_of_agents_list[i], color="black")
#     matplotlib.pyplot.scatter(running_time2[i],num_of_agents_list[i], color="green")
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

for j in range(num_of_iterations):
#    # Uncomment next line to randomise the order of agents
#    random.shuffle(agents)
    
    # Obtain the average store of all agents before actions
    store_total = 0
    for i in range(num_of_agents):
        store_total += agents[i].store
    store_average = store_total/num_of_agents
#    # Uncomment next line to print the average store of all agents in this step
#    print("Average store for step", j, "is", store_average)
    
#    # Uncomment next line to print the step of the movement
#    print("It is", j, "step")
    
    # Move the sheep
    for i in range(num_of_agents):
        # Only for living sheep
        if agents[i].state == 1:
#            # Uncomment next line to print the position of agent before moving
#            print("Before moving",agents[i])
            agents[i].move(times_for_move,store_average)
#            # Uncomment next line to print the position of agent after moving
#            print("After moving",agents[i])
            
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
#            # Uncomment next line to print the position of each agent in each step
#            print(agents[i])
    
    # Move the wolves
    for i in range(num_of_wolves):
        # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
        if wolves[i].eatSheep >= wolves_dead_criterion:
            wolves[i].state = 0
        
        # Wolf eats and moves
        if wolves[i].state == 1:
            wolves[i].move(unit_step_wovle)
            wolves[i].find_eat(required_distance)
        
#    # Uncomment next line to check the state of sheep
#    for i in range(num_of_agents):
#        print("The state for sheep " + str(agents[i].ID) \
#                  + " is " + str(agents[i].state))

    # New sheep born
    if (j + 1) % born_iteration_sheep == 0:
        # Measure the living sheep
        alive_number = 0
        for i in range(num_of_agents):
            if agents[i].state == 1:
                alive_number += 1
        # new_number is the new sheep born from the living sheep (rounding)
        add_number = round(new_sheep_partion * alive_number)
        new_num_of_agents = num_of_agents + add_number
        # make the agents
        for i in range(num_of_agents,new_num_of_agents,1):
            agents.append(agentframework.Agent(environment,agents,i))
        num_of_agents = new_num_of_agents
#        print("Current total number of sheep is",num_of_agents)
    
    # New wolves born
    if (j + 1) % born_iteration_wolves == 0:
        # Measure the living sheep
        alive_number = 0
        for i in range(num_of_wolves):
            if wolves[i].state == 1:
                alive_number += 1
        # new_number is the new sheep born from the living sheep (rounding)
        add_number = round(new_wolves_partion * alive_number)
        new_num_of_wolves = num_of_wolves + add_number
        # make the agents
        for i in range(num_of_wolves,new_num_of_wolves,1):
            wolves.append(agentframework.Wolves(wolves,agents,environment,i))
        num_of_wolves = new_num_of_wolves
#        print("Current total number of wolves is",num_of_wolves)

# =============================================================================
#     # Uncomment next lines to output total amount stored by all the agents to txt file
#     # The output does not contain the initial total amount because it is 0 by default setting
#     totalStored = 0
#     for i in range(num_of_agents):
#         totalStored += agents[i].store
#     write_store_to_output("After the movement and eating of step " + str(j) + \
#                           ", and the total amount stored by all the agents is " + str(totalStored))
# =============================================================================

# Uncomment next lines to display environment and agent
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
#print("Final states")
for i in range(num_of_agents):
#    # Uncomment next lines to print the state for all sheep at the end.
#    print("The state for sheep", agents[i].ID, "is", agents[i].state)
    
    # Living sheep are represented by blue points and dead sheep are represented by red points
    if agents[i].state == 1:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
    else:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
        
for i in range(num_of_wolves):
#    # Uncomment next lines to print the state for all wolves at the end.
#    print("Wolf", wolves[i].ID, "eated total", wolves[i].eatSheep, "sheep")
    
    # Living wolves are represented by black points and dead wolves are represented by yellow points
    if wolves[i].state == 1:
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
    else:
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
matplotlib.pyplot.show()

# =============================================================================
# # Uncomment next lines to write out the environment as .txt file
# for i in range(len(environment)):
#     write_environment_to_output(environment[i])
# =============================================================================

# =============================================================================
# # Uncomment next lines to obtain the normal order if using 'shuffle' function
# print("Random order")
# for i in range(num_of_agents):
#     print(agents[i])
# sorted_agents = sorted(agents, key = lambda a: a.ID)
# print("Normal order")
# for i in range(num_of_agents):
#     print(sorted_agents[i])
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
# carry_on = True	
# jIteration = 0
# 
# def update(frame_number):
#     
#     fig.clear()   
#     global jIteration
#     global num_of_agents
#     global num_of_wolves
#     global carry_on
#     
#     # Plot the environment
#     matplotlib.pyplot.xlim(0, len(environment[0]))
#     matplotlib.pyplot.ylim(0, len(environment))
#     matplotlib.pyplot.imshow(environment)
#     
#     # Move the agents, eat the environment, and share with neighbourhood
#     store_total = 0
#     for i in range(num_of_agents):
#         store_total += agents[i].store
#     store_average = store_total/num_of_agents
#     
#     for i in range(num_of_agents):
#         if agents[i].state == 1:
#             agents[i].move(times_for_move,store_average)
#             agents[i].eat()
#             agents[i].share_with_neighbours(neighbourhood)
#             
#     # Move the wolves
#     for i in range(num_of_wolves):
#         # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
#         if wolves[i].eatSheep >= wolves_dead_criterion:
#             wolves[i].state = 0
#         
#         # Wolf eats and moves
#         if wolves[i].state == 1:
#             wolves[i].move(unit_step_wovle)
#             wolves[i].find_eat(required_distance)
#     
#     # New sheep born
#     if (jIteration + 1) % born_iteration_sheep == 0:
#         # Measure the living sheep
#         alive_number = 0
#         for i in range(num_of_agents):
#             if agents[i].state == 1:
#                 alive_number += 1
#         # new_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_sheep_partion * alive_number)
#         new_num_of_agents = num_of_agents + add_number
#         # make the sheep
#         for i in range(num_of_agents,new_num_of_agents,1):
#             agents.append(agentframework.Agent(environment,agents,i))
#         num_of_agents = new_num_of_agents
# #        print("Current total number of sheep is",num_of_agents)
#     
#     # New wolves born
#     if (jIteration + 1) % born_iteration_wolves == 0:
#         # Measure the living sheep
#         alive_number = 0
#         for i in range(num_of_wolves):
#             if wolves[i].state == 1:
#                 alive_number += 1
#         # new_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_wolves_partion * alive_number)
#         new_num_of_wolves = num_of_wolves + add_number
#         # make the wolves
#         for i in range(num_of_wolves,new_num_of_wolves,1):
#             wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#         num_of_wolves = new_num_of_wolves
# #        print("Current total number of wolves is",num_of_wolves)
#     
#     jIteration += 1
#     
#     # Stop condiction based on a random number
#     if random.random() < 0.001:
#         carry_on = False
#         print("stopping condition")
#     
#     # Plot the agent
#     for i in range(num_of_agents):
#         if agents[i].state == 1:
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
#         else:
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
#     for i in range(num_of_wolves):
#         if wolves[i].state == 1:
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
#         else:
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
# 
# 		
# # Stop condition: (1) Step number (2) Random number
# def gen_function(b = [0]):
#     a = 0
#     global carry_on #Not actually needed as we're not assigning, but clearer
#     while (a < num_of_iterations) & (carry_on) :
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
    
# =============================================================================
# # Define the run function
# def run():
#     animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#     canvas.draw()
#     
# # Figure initializing
# fig = matplotlib.pyplot.figure(figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1])
# 
# # GUI design 
# root = tkinter.Tk()
# root.wm_title("Model")
# canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
# canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
# 
# menu = tkinter.Menu(root)
# root.config(menu=menu)
# model_menu = tkinter.Menu(menu)
# menu.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run model", command=run)
# 
# # Update rule 
# carry_on = True	
# jIteration = 0
# def update(frame_number):
#     
#     fig.clear()   
#     global jIteration
#     global num_of_agents
#     global num_of_wolves
#     global carry_on
#     
#     # Plot the environment
#     matplotlib.pyplot.xlim(0, len(environment[0]))
#     matplotlib.pyplot.ylim(0, len(environment))
#     matplotlib.pyplot.imshow(environment)
#     
#     # Move the agents, eat the environment, and share with neighbourhood
#     store_total = 0
#     for i in range(num_of_agents):
#         store_total += agents[i].store
#     store_average = store_total/num_of_agents
#     for i in range(num_of_agents):
#         if agents[i].state == 1:
#             agents[i].move(times_for_move,store_average)
#             agents[i].eat()
#             agents[i].share_with_neighbours(neighbourhood)
#     
#     # Move the wolves
#     for i in range(num_of_wolves):
#         # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
#         if wolves[i].eatSheep >= wolves_dead_criterion:
#             wolves[i].state = 0
#         
#         # Wolf eats and moves
#         if wolves[i].state == 1:
#             wolves[i].move(unit_step_wovle)
#             wolves[i].find_eat(required_distance)
#     
#     # New sheep born
#     if (jIteration + 1) % born_iteration_sheep == 0:
#         # Measure the living sheep
#         alive_number = 0
#         for i in range(num_of_agents):
#             if agents[i].state == 1:
#                 alive_number += 1
#         # new_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_sheep_partion * alive_number)
#         new_num_of_agents = num_of_agents + add_number
#         # make the sheep
#         for i in range(num_of_agents,new_num_of_agents,1):
#             agents.append(agentframework.Agent(environment,agents,i))
#         num_of_agents = new_num_of_agents
# #        print("Current total number of sheep is",num_of_agents)
#     
#     # New wolves born
#     if (jIteration + 1) % born_iteration_wolves == 0:
#         # Measure the living sheep
#         alive_number = 0
#         for i in range(num_of_wolves):
#             if wolves[i].state == 1:
#                 alive_number += 1
#         # new_number is the new sheep born from the living sheep (rounding)
#         add_number = round(new_wolves_partion * alive_number)
#         new_num_of_wolves = num_of_wolves + add_number
#         # make the wolves
#         for i in range(num_of_wolves,new_num_of_wolves,1):
#             wolves.append(agentframework.Wolves(wolves,agents,environment,i))
#         num_of_wolves = new_num_of_wolves
# #        print("Current total number of wolves is",num_of_wolves)
#     
#     jIteration += 1
#     
#     # Stop condiction based on a random number
#     if random.random() < 0.001:
#         carry_on = False
#         print("stopping condition")
#     
#     # Plot the agent
#     for i in range(num_of_agents):
#         if agents[i].state == 1:
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
#         else:
#             matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
#     for i in range(num_of_wolves):
#         if wolves[i].state == 1:
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
#         else:
#             matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
# 
# 		
# # Stop condition: (1) Step number (2) Random number
# def gen_function(b = [0]):
#     a = 0
#     global carry_on
#     while (a < num_of_iterations) & (carry_on) :
#         yield a			# Returns control and waits next call.
#         a = a + 1
# 
# tkinter.mainloop()
# =============================================================================

# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # # Code above is for GUI Setting
# # # =============================================================================
# # =============================================================================