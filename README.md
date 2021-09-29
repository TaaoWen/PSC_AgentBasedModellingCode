# Programming for Social Science

This code is only used as the practicals (Agent Based Modelling) for the module "[Programming for Social Science](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/)". More information about this assessment can be found [here](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment1/index.html).

The website that introduces this code is [here](https://taaowen.github.io/ABM.html).

[toc]

---

## Basic Introduction

**A simple list of what all the files/directories are:**

There are two `*.py` files. `main.py` contains the main program code, and `agentframework.py` constructs the Agents class for sheep and wolves, as well as their actions. 

There are three text files. `in.txt` provides the environment data. `output_environment.txt` and `output_store.txt` are output files that save the environment data after running the code and the total amount stored by all the agents at each step, respectively.

Some figures obtained by testing are in `testfigure`.

More information about this code can be found in `README.md`. In addition, `LICENSE ` is also given in this folder.

The website that introduces this code is [here](https://taaowen.github.io/ABM.html).

---

**The software is:**

This software is designed to model different kinds of action of agents, including the birth, movement, eating, and sharing information with neighbors. The specific information is shown below.

1. There are different numbers of sheep and wolves at the beginning whose positions are randomly distributed in the environment, and they can move randomly in the process. However, wolves can move quicker than sheep, and sheep with different stores have different speeds. 
2. Sheep can eat the grass in the environment based on certain rules. Wolves can eat sheep when they are close.  
3. Sheep will die when they are eaten by wolves, and wolves will die when they eat a certain number of sheep. The state of each sheep and wolf will be saved in code and shown in the visualized figure.
4. Sheep can share the information/store with neighbor within a defined distance.
5. Sheep and wolves have different birth rates.

The mathematic model of my code can be found in the submitted word file because it contains many equations.

---

**How to run the software and what to expect when it is run:**

There are 4 parts in `main.py`. The initial parameter setting, function, and `Agents` class can be used in all 3 parts.

1. **Initial setting**: All initial information about agents and environment are set here and users do not need to change it if they want to use default value.
2. **Basic figures**: Users only need to click 'Run files' or `F5` to run this part. Users can obtain the final visualized figure that shows the environment and positions of sheep and wolves (with different color). Users can also obtain the environment after modelling and the total amount stored by all the agents at each step in `.txt` files by uncommenting some lines based on the introduction in `main.py`. Please uncomment all codes between `Code below is for Basic figures` and `Code above is for Basic figures` when users want to run this part of code.
3. **Animation**: Users only need to click 'Run files' or `F5` to run this part. Users can get a GIF of agents (wolves and sheep) moving in the environment that shows agents’ movement and state, as well as the amount of grass in each point. Please uncomment all codes between `Code below is for Animation` and `Code above is for Animation` when users want to run this part of code.
4. **GUI design**: Users only need to click 'Run files' to run this part. The same results in "Animation" can be obtained, but users need to click 'Run model' in GUI. Please uncomment all codes between `Code below is for GUI Setting` and `Code above is for GUI Setting` when users want to run this part of code. In addition, users need to use `Tkinter` and can refer to this [introduction](https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/index.html) to set.

Please note that all tests are included in `main.py` and `agentframework.py` by commenting. Thus, users can uncomment specific lines to test whether the code can work normally based on the introduction in these files (test results are also given in this file). For example,

1. Read model parameters from the command line;
2. Visualize the environment data obtained from text file;
3. Measure the distance between two agents by different functions defined in advance, and obtain the timings for different functions with different number of agents to visualize;
4. Identify the agent with the largest x (furthest east);
5. Print the position (and other information) of agents in each iteration;
6. Write the environment data after eating and movement into text file;
7. and others.

---

**Known issues:**

There are no known issues now.

Please note that the test code below may be different from the final version, but it does **NOT** change the final outcome and performance of the code.

---

**Testing done:**

Almost all codes are tested, and all details can be found in the comment of `main.py` and `agentframework.py`.

---

**Ideas for further development:**

The mathematic model about the movement and dynamic of agents can be further improved.

## First module -- Agent Based Modelling

Some tests are shown below. **Notice**: We direct test these basic codes and functions based on the `Agents` class. 

**Test 1**: Identify the initial position of each agent based on the random.randint function.

```python
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,i))
    # Uncomment next line to print the initial position of all agents
    print(agents[i])
```

Output is below, where `ID` is the agent ID,`x` and `y` represent the position of each agent.

`ID = 0, x=97, y=49
ID = 1, x=5, y=53
ID = 2, x=65, y=33
ID = 3, x=51, y=62
ID = 4, x=61, y=38
ID = 5, x=74, y=45
ID = 6, x=64, y=27
ID = 7, x=36, y=17
ID = 8, x=96, y=17
ID = 9, x=79, y=12`

----

**Test 2**: Find the position of each agent in each step when they move randomly.

```python
# Move the agents.
for j in range(num_of_iterations):
    # Uncomment next line to print the step of the movement
    print("It is", j, "step")
    for i in range(num_of_agents):
        agents[i].move()
        # Uncomment next line to print the position of each agent in each step
        print(agents[i])
```

Output is below, where `ID` is the agent ID,`x` and `y` represent the position of each agent after the movement. We can find the position of each agent is continues (`x = x +/- 1, y = y +/- 1`). 

`It is 0 step
ID = 0, x=96, y=48
ID = 1, x=4, y=52
ID = 2, x=64, y=34
ID = 3, x=52, y=63
ID = 4, x=60, y=39
ID = 5, x=73, y=46
ID = 6, x=65, y=26
ID = 7, x=37, y=16
ID = 8, x=97, y=16
ID = 9, x=80, y=11
It is 1 step
ID = 0, x=95, y=49
ID = 1, x=3, y=51
ID = 2, x=63, y=33
ID = 3, x=51, y=62
ID = 4, x=61, y=38
ID = 5, x=72, y=47
ID = 6, x=64, y=27
ID = 7, x=36, y=17
ID = 8, x=96, y=17
ID = 9, x=79, y=10
It is 2 step
ID = 0, x=94, y=50
ID = 1, x=4, y=52
ID = 2, x=64, y=34
ID = 3, x=50, y=63
ID = 4, x=60, y=37
ID = 5, x=73, y=48
ID = 6, x=63, y=28
ID = 7, x=37, y=18
ID = 8, x=95, y=18
ID = 9, x=78, y=11`

---

**Test 3**: With our defined function `distance_between` that measures the distance between two agents, 

```python
# Obtain the distance between two agents
def distance_between(agents_row_a, agents_row_b):
    """
    Obtain the distance between two agents
    
    :param agents_row_a: First agent 
    :param agents_row_b: Second agent
    
    :return: The distance between two agents based on Euclidean distance
    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
```

we test if this function can work normally.

```python
# Uncomment next line to test if "distance_between" function can work normally.
print("The position of agent A is", agents[0])
print("The position of agent B is", agents[1])
print("The distance between agent A and B is", distance_between(agents[0],agents[1]))
```

Output is below. We can find the distance obtained by our defined function is correct. 

`The position of agent A is ID = 0, x=97, y=49
The position of agent B is ID = 1, x=5, y=53
The distance between agent A and B is 92.0869154657707`

## Second module -- Code shrinking I

The storage of agent position (by `*.append`) has been test **Test 1** in the first module, so we do not repeat to test it here.

**Test 1**: After initializing the position of all agents, we want to test if our code can find the agent with the largest `x` (furthest east) position. The code is shown below.

```python
# Uncomment next lines to find the agent with the largest x (furthest east)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
sorted_agents = sorted(agents, key = lambda a: a.y)
matplotlib.pyplot.scatter(sorted_agents[len(agents)-1].x,sorted_agents[len(agents)-1].y, color = 'black')
matplotlib.pyplot.show()
```

Then, we can obtain the agent with the largest `x` (furthest east) shown as the **red** point in this figure, which is different from other black points. 

<img src="testfigure/largest_y.png" alt="largest_y" style="zoom:72%;" />

## Third module -- Code shrinking II

**Test 1**: We want to use for-loops to reduce the code size, the initialization and movement of `num_of_agents` agents in `num_of_iterations` steps are shown below.

```python
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,i))
    # Uncomment next line to print the initial position of all agents
    print(agents[i])

# Move the agents.
for j in range(num_of_iterations):
    # Uncomment next line to print the step of the movement
    print("It is", j, "step")
    
    for i in range(num_of_agents):
        agents[i].move()
```

Output is below. We can find the initial position and the movement of `num_of_agents = 10` agent in `num_of_iterations = 3` steps (<u>`num_of_agents` and `num_of_iterations` are small here only for a test</u>). The movement of all agents is continues, which is the same as the output of **Test 2** in the first module.

`ID = 0, x=97, y=49
ID = 1, x=5, y=53
ID = 2, x=65, y=33
ID = 3, x=51, y=62
ID = 4, x=61, y=38
ID = 5, x=74, y=45
ID = 6, x=64, y=27
ID = 7, x=36, y=17
ID = 8, x=96, y=17
ID = 9, x=79, y=12
It is 0 step
ID = 0, x=96, y=48
ID = 1, x=4, y=52
ID = 2, x=64, y=34
ID = 3, x=52, y=63
ID = 4, x=60, y=39
ID = 5, x=73, y=46
ID = 6, x=65, y=26
ID = 7, x=37, y=16
ID = 8, x=97, y=16
ID = 9, x=80, y=11
It is 1 step
ID = 0, x=95, y=49
ID = 1, x=3, y=51
ID = 2, x=63, y=33
ID = 3, x=51, y=62
ID = 4, x=61, y=38
ID = 5, x=72, y=47
ID = 6, x=64, y=27
ID = 7, x=36, y=17
ID = 8, x=96, y=17
ID = 9, x=79, y=10
It is 2 step
ID = 0, x=94, y=50
ID = 1, x=4, y=52
ID = 2, x=64, y=34
ID = 3, x=50, y=63
ID = 4, x=60, y=37
ID = 5, x=73, y=48
ID = 6, x=63, y=28
ID = 7, x=37, y=18
ID = 8, x=95, y=18
ID = 9, x=78, y=11`

## Fourth module -- Building tools

Whether the `distance_between` function can work normally has been tested in **Test 3** of the first module, so we do not repeat to test it here.

**Test 1**: We will test the running time to calculate the distance between each pair of agent, and we only do not calculate the distance from `agentA` to `agentA` in this function, that is, `i != j`. The code is shown below.

```python
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
                # Uncomment next line to print the distance between each pair of agents
                print("The distance between Agent", agents_row_a.ID, \
                      "and Agent", agents_row_b.ID, \
                      "is", distance_between(agents_row_a, agents_row_b))
                max_dis = max(max_dis, distance_between(agents[i], agents[j]))
                min_dis = min(min_dis, distance_between(agents[i], agents[j]))
    end_time = time.time()
    need_time = end_time - start_time
    # Uncomment next lines to print the max and min distances, as well as the timing
    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
    print("Running time is", need_time)
    return need_time, max_dis, min_dis
```

As we mentioned in the comment of Python code "`agentA ` and `agentB` are all from 1 to end and `agentA != agentB`". Output is below, we can obtain the distance between each pair of agents, the maximum and minimum distance among all agents, and the running time to obtain the result.

`The distance between Agent 0 and Agent 1 is 92.0869154657707
The distance between Agent 0 and Agent 2 is 35.77708763999664
The distance between Agent 0 and Agent 3 is 47.80167361086848
The distance between Agent 0 and Agent 4 is 37.64306044943742
The distance between Agent 0 and Agent 5 is 23.345235059857504
The distance between Agent 0 and Agent 6 is 39.66106403010388
The distance between Agent 0 and Agent 7 is 68.8839603971781
The distance between Agent 0 and Agent 8 is 32.01562118716424
The distance between Agent 0 and Agent 9 is 41.14608122288197
The distance between Agent 1 and Agent 0 is 92.0869154657707
The distance between Agent 1 and Agent 2 is 63.245553203367585
The distance between Agent 1 and Agent 3 is 46.87216658103186
The distance between Agent 1 and Agent 4 is 57.97413216254298
The distance between Agent 1 and Agent 5 is 69.46221994724903
The distance between Agent 1 and Agent 6 is 64.47480127925948
The distance between Agent 1 and Agent 7 is 47.50789408087881
The distance between Agent 1 and Agent 8 is 97.86214794290998
The distance between Agent 1 and Agent 9 is 84.59905436823747
The distance between Agent 2 and Agent 0 is 35.77708763999664
The distance between Agent 2 and Agent 1 is 63.245553203367585
The distance between Agent 2 and Agent 3 is 32.202484376209235
The distance between Agent 2 and Agent 4 is 6.4031242374328485
The distance between Agent 2 and Agent 5 is 15.0
The distance between Agent 2 and Agent 6 is 6.082762530298219
The distance between Agent 2 and Agent 7 is 33.12099032335839
The distance between Agent 2 and Agent 8 is 34.88552708502482
The distance between Agent 2 and Agent 9 is 25.238858928247925
The distance between Agent 3 and Agent 0 is 47.80167361086848
The distance between Agent 3 and Agent 1 is 46.87216658103186
The distance between Agent 3 and Agent 2 is 32.202484376209235
The distance between Agent 3 and Agent 4 is 26.0
The distance between Agent 3 and Agent 5 is 28.600699292150182
The distance between Agent 3 and Agent 6 is 37.33630940518894
The distance between Agent 3 and Agent 7 is 47.43416490252569
The distance between Agent 3 and Agent 8 is 63.63961030678928
The distance between Agent 3 and Agent 9 is 57.30619512757761
The distance between Agent 4 and Agent 0 is 37.64306044943742
The distance between Agent 4 and Agent 1 is 57.97413216254298
The distance between Agent 4 and Agent 2 is 6.4031242374328485
The distance between Agent 4 and Agent 3 is 26.0
The distance between Agent 4 and Agent 5 is 14.7648230602334
The distance between Agent 4 and Agent 6 is 11.40175425099138
The distance between Agent 4 and Agent 7 is 32.64965543462902
The distance between Agent 4 and Agent 8 is 40.8166632639171
The distance between Agent 4 and Agent 9 is 31.622776601683793
The distance between Agent 5 and Agent 0 is 23.345235059857504
The distance between Agent 5 and Agent 1 is 69.46221994724903
The distance between Agent 5 and Agent 2 is 15.0
The distance between Agent 5 and Agent 3 is 28.600699292150182
The distance between Agent 5 and Agent 4 is 14.7648230602334
The distance between Agent 5 and Agent 6 is 20.591260281974
The distance between Agent 5 and Agent 7 is 47.20169488482379
The distance between Agent 5 and Agent 8 is 35.608987629529715
The distance between Agent 5 and Agent 9 is 33.37663853655727
The distance between Agent 6 and Agent 0 is 39.66106403010388
The distance between Agent 6 and Agent 1 is 64.47480127925948
The distance between Agent 6 and Agent 2 is 6.082762530298219
The distance between Agent 6 and Agent 3 is 37.33630940518894
The distance between Agent 6 and Agent 4 is 11.40175425099138
The distance between Agent 6 and Agent 5 is 20.591260281974
The distance between Agent 6 and Agent 7 is 29.732137494637012
The distance between Agent 6 and Agent 8 is 33.52610922848042
The distance between Agent 6 and Agent 9 is 21.213203435596427
The distance between Agent 7 and Agent 0 is 68.8839603971781
The distance between Agent 7 and Agent 1 is 47.50789408087881
The distance between Agent 7 and Agent 2 is 33.12099032335839
The distance between Agent 7 and Agent 3 is 47.43416490252569
The distance between Agent 7 and Agent 4 is 32.64965543462902
The distance between Agent 7 and Agent 5 is 47.20169488482379
The distance between Agent 7 and Agent 6 is 29.732137494637012
The distance between Agent 7 and Agent 8 is 60.0
The distance between Agent 7 and Agent 9 is 43.289721643826724
The distance between Agent 8 and Agent 0 is 32.01562118716424
The distance between Agent 8 and Agent 1 is 97.86214794290998
The distance between Agent 8 and Agent 2 is 34.88552708502482
The distance between Agent 8 and Agent 3 is 63.63961030678928
The distance between Agent 8 and Agent 4 is 40.8166632639171
The distance between Agent 8 and Agent 5 is 35.608987629529715
The distance between Agent 8 and Agent 6 is 33.52610922848042
The distance between Agent 8 and Agent 7 is 60.0
The distance between Agent 8 and Agent 9 is 17.72004514666935
The distance between Agent 9 and Agent 0 is 41.14608122288197
The distance between Agent 9 and Agent 1 is 84.59905436823747
The distance between Agent 9 and Agent 2 is 25.238858928247925
The distance between Agent 9 and Agent 3 is 57.30619512757761
The distance between Agent 9 and Agent 4 is 31.622776601683793
The distance between Agent 9 and Agent 5 is 33.37663853655727
The distance between Agent 9 and Agent 6 is 21.213203435596427
The distance between Agent 9 and Agent 7 is 43.289721643826724
The distance between Agent 9 and Agent 8 is 17.72004514666935
Maximum distance is 97.86214794290998 and minimum distance is 6.082762530298219
Running time is 0.0`

---

**Test 2**: Apart from the function `calculate_distance_0` that `agentA` and `agentB` are all from 1 to end (`agentA != agentB`), a new function `calculate_distance_1` that only calculate the distance between agents when `agents_row_a.ID > agents_row_b.ID` although `agentA` and `agentB` are still from 1 to end is then used. The code is below.

```python
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
    # Uncomment next lines to print the max and min distances, as well as the timing
    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
    print("Running time is", need_time)
    return need_time, max_dis, min_dis
```

The third function `calculate_distance_2` has a different for-loops, that is, `agentA` is from 1 to end, `agentB` is from `agentA` to end (not include `agentA`), and it is shown below.

```python
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
    # Uncomment next lines to print the max and min distances, as well as the timing
    print("Maximum distance is", max_dis, "and minimum distance is", min_dis)
    print("Running time is", need_time)
    return need_time, max_dis, min_dis
```

When these three functions are implemented.

```python
# Uncomment next lines to obtain the timings, the maximum and the minimum distances for three functions
need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
```

The output of three functions are below. 

`Maximum distance is 97.86214794290998 and minimum distance is 6.082762530298219
Running time is 0.0
Maximum distance is 97.86214794290998 and minimum distance is 6.082762530298219
Running time is 0.0
Maximum distance is 97.86214794290998 and minimum distance is 6.082762530298219
Running time is 0.0`

We can find the maximum and minimum distance obtained by three functions are the same, and it meets our expectation. The running time of three function is the same due to the setting of the number of agents, and we will further test it with different number of agents in **Test 3**.

----

**Test 3**: The running time for two distance calculating functions with different number of agents are then tested.

```python
# Uncomment next lines to obtain the timings for three function under different number of agents
num_of_agents_list = [10,20,50,100,200,500,1000,2000,4000]
running_time0 = []
running_time1 = []
running_time2 = []
for num_of_agents in num_of_agents_list:
    # Print the current number of agents
    print("Now, the number of agents is", num_of_agents)
    agents = []
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment,agents,i))
#    # Uncomment next line to print the initial position of all agents
#    print(agents[i])
    
    need_time0, max_dis0, min_dis0 = calculate_distance_0(agents)
    running_time0.append(need_time0)
    need_time1, max_dis1, min_dis1 = calculate_distance_1(agents)
    running_time1.append(need_time1)
    need_time2, max_dis2, min_dis2 = calculate_distance_2(agents)
    running_time2.append(need_time2)
    
# Calculate the maximum time it takes for any run. 
max_time = max(running_time0)
max_time = max(max_time, max(running_time1))
max_time = max(max_time, max(running_time2))
# Set the axis limits
matplotlib.pyplot.ylim(0, 1.1 * max(num_of_agents_list))
matplotlib.pyplot.xlim(0, 1.1 * max_time)
# Plot the timings in a graph
for i in range(len(num_of_agents_list)):
    matplotlib.pyplot.scatter(running_time0[i],num_of_agents_list[i], color="red")
    matplotlib.pyplot.scatter(running_time1[i],num_of_agents_list[i], color="black")
    matplotlib.pyplot.scatter(running_time2[i],num_of_agents_list[i], color="green")
matplotlib.pyplot.xlabel("Timing")
matplotlib.pyplot.ylabel("Number of agents")
matplotlib.pyplot.legend(["Function0","Function1","Function2"])
matplotlib.pyplot.show() 
```

When the list of the number of agents is `num_of_agents_list = [10,20,50,100,200,500,1000,2000,4000]`, the figure is shown below. We can find the timing for `calculate_distance_0` is the largest. The timing for `calculate_distance_1` and `calculate_distance_2` are very close, but they are both much shorter than the timing for `calculate_distance_0` (half of `calculate_distance_0` timing), because they do not repeat to calculate the distance. The difference  is the largest. The timing for `calculate_distance_0` is so large when `num_of_agents = 4000` that the difference of other timing cannot be found in this figure. However, the timing for `calculate_distance_1` and `calculate_distance_2` is different.

<img src="testfigure/timingForAgents.png" alt="timingForAgents" style="zoom:72%;" />



## Fifth module -- Agents!

Whether the `Agents` class can make the agent position normally has been tested in **Test 1** of the first module, so we do not repeat to test it here.

**Test 1**: To test if the `Agents` class can move the agent based on `random.random()`, the code below is used.

```python
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Uncomment next line to print the position of agent before moving
        print("Before moving",agents[i])
        
        agents[i].move()
        
        # Uncomment next line to print the position of agent after moving
        print("After moving",agents[i])
```

Only part of outcomes are shown below. We can find the movement of each agent is continues (`x = x +/- 1, y = y +/- 1`). 

`Before moving ID = 0, x=95, y=49
After moving ID = 0, x=94, y=50
Before moving ID = 1, x=3, y=51
After moving ID = 1, x=4, y=52
Before moving ID = 2, x=63, y=33
After moving ID = 2, x=64, y=34
Before moving ID = 3, x=51, y=62
After moving ID = 3, x=50, y=63`

## Sixth module -- I/O

**Test 1**: In order to test if we can input the environment from the `.txt` file, the code below is used.

```python
# Uncomment next lines to visualize the environment
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
```

The figure is shown below, and we can find the environment can be inputted from the `.txt` file successfully.

<img src="testfigure/environment.png" alt="environment" style="zoom:72%;" />

---

**Test 2**: We then test if we can display the environment and agents simultaneously, the code below is used.

```python
# Uncomment next lines to display environment and agent
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
matplotlib.pyplot.show()
```

The output is shown below, where agents are shown as red points in the environment.

<img src="testfigure/environment_agents.png" alt="environment_agents" style="zoom:72%;" />

---

**Test 3**: We then write out the environment as a file, and the code is below.

```python
# Uncomment next lines to write out the environment as .txt file
for i in range(len(environment)):
    write_environment_to_output(environment[i])
```

with the function defined as

```python
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
```

Part of the output (one line of the environment) in the `output_environment.txt` is shown below and it meets our expectation.

`220.0,221.0,222.0,223.0,226.0,230.0,234.0,238.0,241.0,241.0,242.0,243.0,243.0,243.0,244.0,244.0,245.0,247.0,249.0,250.0,251.0,250.0,250.0,250.0,250.0,250.0,250.0,250.0,250.0,250.0,251.0,252.0,253.0,254.0,254.0,255.0,255.0,254.0,254.0,254.0,254.0,254.0,254.0,254.0,253.0,253.0,253.0,253.0,253.0,253.0,253.0,252.0,252.0,251.0,251.0,251.0,250.0,250.0,249.0,248.0,247.0,247.0,247.0,247.0,248.0,250.0,251.0,252.0,252.0,251.0,249.0,248.0,247.0,246.0,245.0,245.0,244.0,244.0,243.0,242.0,241.0,241.0,240.0,240.0,239.0,238.0,238.0,237.0,236.0,235.0,234.0,233.0,232.0,232.0,232.0,231.0,231.0,230.0,229.0,228.0,227.0,225.0,224.0,223.0,221.0,221.0,220.0,219.0,219.0,218.0,217.0,216.0,215.0,215.0,216.0,215.0,214.0,212.0,210.0,209.0,210.0,210.0,210.0,210.0,210.0,211.0,212.0,212.0,211.0,210.0,208.0,207.0,206.0,205.0,203.0,203.0,201.0,200.0,200.0,199.0,197.0,197.0,195.0,194.0,194.0,193.0,193.0,192.0,191.0,191.0,191.0,191.0,191.0,190.0,190.0,188.0,187.0,186.0,185.0,184.0,184.0,183.0,183.0,184.0,185.0,186.0,188.0,190.0,191.0,193.0,196.0,197.0,199.0,201.0,202.0,204.0,206.0,207.0,207.0,206.0,204.0,202.0,201.0,201.0,201.0,200.0,200.0,200.0,200.0,200.0,200.0,200.0,200.0,199.0,198.0,197.0,196.0,195.0,194.0,194.0,192.0,192.0,191.0,190.0,189.0,189.0,188.0,188.0,187.0,186.0,186.0,185.0,184.0,184.0,183.0,182.0,182.0,181.0,181.0,180.0,179.0,178.0,177.0,176.0,176.0,176.0,175.0,174.0,173.0,172.0,172.0,172.0,172.0,171.0,171.0,169.0,168.0,167.0,166.0,165.0,164.0,163.0,162.0,162.0,161.0,159.0,159.0,157.0,156.0,156.0,155.0,155.0,154.0,154.0,154.0,154.0,153.0,153.0,153.0,152.0,151.0,150.0,149.0,149.0,149.0,149.0,148.0,146.0,145.0,144.0,143.0,143.0,142.0,142.0,141.0,139.0,138.0,136.0,134.0,133.0,133.0,132.0,133.0,133.0,133.0,132.0,132.0,131.0,130.0,130.0,130.0,132.0,132.0,132.0,130.0,129.0,128.0,127.0,127.0,127.0`

---

**Test 4**: We write out the total amount stored by all the agents. Here, the output is obtained after the movement and eating of each iteration. In addition, the output does not contain the initial total amount because it is 0 by default. The code is shown below.

```python
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
    # Uncomment next lines to output total amount stored by all the agents to txt file
    # The output does not contain the initial total amount because it is 0 by default setting
    totalStored = 0
    for i in range(num_of_agents):
        totalStored += agents[i].store
    write_store_to_output("After the movement and eating of step " + str(j) + ", and the total amount stored by all the agents is " + str(totalStored))
 
```

Part of the output (3 steps) is shown below. We can find the the total amount increases 100 each step because there are `num_of_agents = 10` agents and each agent eat 10 each step. Thus, it is correct. 

`After the movement and eating of step 0, and the total amount stored by all the agents is 100.0
After the movement and eating of step 1, and the total amount stored by all the agents is 200.0
After the movement and eating of step 2, and the total amount stored by all the agents is 300.0`

---

**Test 5**: We then define  `__str__(self)` in the agents and print location and stores of each agent. The `__str__(self)` is defined as below.

```python
    def __str__(self):
        return "ID = " + str(self.ID) \
                + ", x=" + str(self.x) \
                + ", y=" + str(self.y) \
                + ", store=" + str(self.store)
```

We then print the information in the `main.py`, and the code is shown below.

```python
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
        # Uncomment next line to print the position of each agent in each step
        print(agents[i])
```

The output is below, and we can find the location and stores of each agent, so it meets our expectation.

`ID = 0, x=96, y=48, store=10
ID = 1, x=4, y=52, store=10
ID = 2, x=64, y=34, store=10
ID = 3, x=52, y=63, store=10
ID = 4, x=60, y=39, store=10
ID = 5, x=73, y=46, store=10
ID = 6, x=65, y=26, store=10
ID = 7, x=37, y=16, store=10
ID = 8, x=97, y=16, store=10
ID = 9, x=80, y=11, store=10
ID = 0, x=95, y=49, store=20
ID = 1, x=3, y=51, store=20
ID = 2, x=63, y=33, store=20
ID = 3, x=51, y=62, store=20
ID = 4, x=61, y=38, store=20
ID = 5, x=72, y=47, store=20
ID = 6, x=64, y=27, store=20
ID = 7, x=36, y=17, store=20
ID = 8, x=96, y=17, store=20
ID = 9, x=79, y=10, store=20
ID = 0, x=94, y=50, store=30
ID = 1, x=4, y=52, store=30
ID = 2, x=64, y=34, store=30
ID = 3, x=50, y=63, store=30
ID = 4, x=60, y=37, store=30
ID = 5, x=73, y=48, store=30
ID = 6, x=63, y=28, store=30
ID = 7, x=37, y=18, store=30
ID = 8, x=95, y=18, store=30
ID = 9, x=78, y=11, store=30`

---

**Test 6**: In the `Agents` class, we use the environment size to randomize agents' starting locations and deal with the boundary conditions. The code in `Agents` class is shown below.

```python
    # Agent setting
    def __init__(self,environment,agents,ID):
        self.environment = environment
        self.store = 0
        
        # Agent position initializing based on the environment size
        self.y = random.randint(0,len(environment))
        self.x = random.randint(0,len(environment[0]))
        
        self.agents = agents
        self.ID = ID
        
    # Alter agent's position randomly
    def move(self):
        # Alter agent's x position
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment[0])
        else:
            self.x = (self.x - 1) % len(self.environment[0])
        
        # Alter agent's y position
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)
```

We visualize the environment and agents together, then we can find that agents can wander around the full environment.

<img src="testfigure/environment_agents_size.png" alt="environment_agents_size" style="zoom:72%;" />

---

**Test 7**: When  there's less than 10 left, the agent will only eat the last few bits, without leaving negative values. In addition, the agents will sick up their store in a location if they've been greedy guts and eaten more than 100 units. The code in `Agents` class is shown below.

```python
    # Eat the environmeny, the agent will not leave negative values and sick up their store
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        if self.store >= 100:
            self.environment[self.y][self.x] += 100
            self.store = 0
```

## Seventh module -- Communicating

**Test 1**: The agent list will be stored in all agents so that they can communicate with each other. The code in `Agents` class is shown below.

```python
    # Agent setting
    def __init__(self,environment,agents,ID):
        self.environment = environment
        self.store = 0
        
        # Agent position initializing based on the environment size
        self.y = random.randint(0,len(environment))
        self.x = random.randint(0,len(environment[0]))
        
        self.agents = agents
        self.ID = ID
```

We then test the original information of `Agent 1` and the information about `Agent 1` from `Agent 0`. The code is shown below.

```python
# Uncomment next lines to test if each agent has the information of other agents.
print("This is the original information from Agent 1:", agents[1])
print("This is the information of Agent 1 from Agent 0:", agents[0].agents[1])
```

We can find the output is the same, so it is correct.

`This is the original information from Agent 1: ID = 1, x=132, y=20, store=0
This is the information of Agent 1 from Agent 0: ID = 1, x=132, y=20, store=0`

---

**Test 2**: Within the required distance, two agents will share the stores with each other, and the code in `Agents` class is shown below, where `distance_between` is the function to measure the distance, and `share_with_neighbours` is the function to share the store with each other. In function `share_with_neighbours`, each agent will not share the store with itself by setting `self.ID != agent.ID`.

```python
    # Measure the distance between two agents
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    # Share the stores with neighbour agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if self.ID != agent.ID:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    print("Original store for Agent A is " + str(self))
                    print("Original store for Agent B is " + str(agent))
                    OverallStore = self.store + agent.store
                    AveStore = OverallStore /2
                    self.store = AveStore
                    agent.store = AveStore
                    
                    # Uncomment next line to print the information from two agents that share the stores
                    print("The distance between Agents " + str(self) + " Agents " + str(agent) \
                          + " is " + str(dist) \
                          + ", so they can share the store within the distance " + str(neighbourhood) \
                          + ", and the average store should be " + str(AveStore))
```

Part of the output is shown below. We can find `Agent 6` and `Agent 9` share their stores because the distance between them `15.297058540778355` is less than `20`. The store for each agent is `10` and `0` before sharing, and the average store after sharing is `5`. Thus, this function works in the `Agents` class.

`Original store for Agent A is ID = 6, x=72, y=257, store=10
Original store for Agent B is ID = 9, x=75, y=272, store=0
The distance between Agents ID = 6, x=72, y=257, store=5.0 Agents ID = 9, x=75, y=272, store=5.0 is 15.297058540778355, so they can share the store within the distance 20, and the average store should be 5.0`

---

**Test 3**: We randomise the order in which agents are processed each iteration, and the code is below. We print the agent in each iteration to see if the order is random.

```python
# Move the agents.
for j in range(num_of_iterations):
    # Uncomment next line to randomise the order of agents
    random.shuffle(agents)
    
    # Uncomment next line to print the step of the movement
    print("It is", j, "step")
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        # Uncomment next line to print the position of each agent in each step
        print(agents[i])
```

Only the output in the first iteration is shown below. We can find the order is random, so the code is correct.

`It is 0 step
ID = 7, x=72, y=145, store=10
ID = 0, x=214, y=198, store=10
ID = 9, x=74, y=273, store=5.0
ID = 3, x=154, y=208, store=10
ID = 2, x=247, y=260, store=10
ID = 5, x=112, y=297, store=10
ID = 6, x=70, y=257, store=10.0
ID = 8, x=127, y=47, store=10
ID = 1, x=131, y=21, store=10
ID = 4, x=182, y=243, store=10`

---

**Test 4**: In order to read model parameters from the command line using `argv`, we need `import sys` first.

```python
import sys
```

The model parameters will be set as follow, so that the model can read  parameters from the command line.

```python
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
```

In command line, we input this command,

`C:\Users\Tao WEN\Desktop\PSC\ABM>python main.py 15 10 20`

and the output is below. We can find there will be 10 iterations, which meets our expectation.

`It is 0 step
It is 1 step
It is 2 step
It is 3 step
It is 4 step
It is 5 step
It is 6 step
It is 7 step
It is 8 step
It is 9 step`

## Eighth module -- Animation/Behaviour

**Test 1**: Some agents can steal more resources from others if their store are low. In the `Agents` class, these agents with lower store can steal more resources from others, that is, 3/4 of the total stores of two agents. The code is below.

```python
    # Share the stores with neighbour agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if self.ID != agent.ID:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    print("Original store for Agent A is " + str(self))
                    print("Original store for Agent B is " + str(agent))
                    OverallStore = self.store + agent.store
                    
                    # Agents with lower store can steal more resources (3/4) from others
                    if self.store > agent.store:
                        agent.store = 3 * OverallStore / 4
                        self.store = OverallStore / 4
                    if self.store < agent.store:
                        agent.store = OverallStore / 4
                        self.store = 3 * OverallStore / 4
                    else:
                        agent.store = OverallStore / 2
                        self.store = OverallStore / 2

                    # Uncomment next line to print the information from two agents that share the stores
                    print("The distance between Agents " + str(self) + " Agents " + str(agent) \
                          + " is " + str(dist) \
                          + ", so they can share the store within the distance " + str(neighbourhood) \
                          + ", and the average store should be " + str(OverallStore / 2))
              
```

Part of the output is below. We can find the store for `Agent A` and `Agent B` is `32.5` and `67.5` before sharing, thus `Agent A` will steal more resources from `Agent B`. The total store of two agents is `100`. Therefore, `Agent A` will obtain `3/4` of the total stores, and it is `75.0` after sharing. `Agent B` has the other `1/4` of the total stores, and it is `25.0` after sharing. So The output below meets our expectation.

`Original store for Agent A is ID = 9, x=68, y=267, store=32.5
Original store for Agent B is ID = 6, x=74, y=255, store=67.5
The distance between Agents ID = 9, x=68, y=267, store=75.0 Agents ID = 6, x=74, y=255, store=25.0 is 13.416407864998739, so they can share the store within the distance 20, and the average store should be 50.0`

---

**Test 2**: These agents with more resources will move quicker in our model. In `Agents` class, these agents whose store is `times_for_move` times the average resource `store_average` will move `2` units each time. The definition in `Agents` class is below.

```python
    # Alter agent's position randomly
    def move(self,times_for_move,store_average):
        if self.store > times_for_move * store_average:
            # Alter agent's x position
            if random.random() < 0.5:
                self.x = (self.x + 2) % len(self.environment[0])
            else:
                self.x = (self.x - 2) % len(self.environment[0])
            
            # Alter agent's y position
            if random.random() < 0.5:
                self.y = (self.y + 2) % len(self.environment)
            else:
                self.y = (self.y - 2) % len(self.environment)
        else:    
            # Alter agent's x position
            if random.random() < 0.5:
                self.x = (self.x + 1) % len(self.environment[0])
            else:
                self.x = (self.x - 1) % len(self.environment[0])
            
            # Alter agent's y position
            if random.random() < 0.5:
                self.y = (self.y + 1) % len(self.environment)
            else:
                self.y = (self.y - 1) % len(self.environment)
```

The code in `main.py` is below.

```python
# Move the agents.
for j in range(num_of_iterations):    
    # Obtain the average store of all agents before actions
    store_total = 0
    for i in range(num_of_agents):
        store_total += agents[i].store
    store_average = store_total/num_of_agents
    
    # Uncomment next line to print the step of the movement
    print("It is", j, "step")
    
    for i in range(num_of_agents):
        agents[i].move(times_for_move,store_average)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        # Uncomment next line to print the position of each agent in each step
        print(agents[i])
```

The output is below. The average store before Step 1 is `10.0`, and only `Agent 9` has higher stores, that is, `15.0 > 1.1 * 10.0` when `times_for_move = 1.1`, so only `Agent 9` moves 2 units in this step. From the output, it meets our expectation because it is `x=73, y=270` in the first step and it is `x=71, y=268` in the second step. Other agents only move 1 units in this step.

`It is 0 step
ID = 0, x=216, y=196, store=10
ID = 1, x=131, y=19, store=10
ID = 2, x=249, y=262, store=10
ID = 3, x=156, y=206, store=10
ID = 4, x=182, y=243, store=10
ID = 5, x=112, y=297, store=10
ID = 6, x=72, y=257, store=7.5
ID = 7, x=70, y=145, store=10
ID = 8, x=127, y=49, store=10
ID = 9, x=73, y=270, store=15.0
Average store for step 1 is 10.0
It is 1 step
ID = 0, x=217, y=197, store=20
ID = 1, x=130, y=20, store=20
ID = 2, x=250, y=261, store=20
ID = 3, x=157, y=205, store=20
ID = 4, x=183, y=242, store=20
ID = 5, x=111, y=298, store=20
ID = 6, x=73, y=258, store=15.0
ID = 7, x=69, y=144, store=20
ID = 8, x=128, y=48, store=20
ID = 9, x=71, y=268, store=30.0`

---

**Test 3**: There will be wolves to eat nearby sheep. Here, the `Wolves` class is defined, and the initial position for wolves is also random (in `__init__` function). They will move quicker than sheep (`unit_step` each iteration) in `move` function. When the distance between wolf and sheep is close than `required_distance`, this sheep will be eaten (in `find_eat` function). When one wolf has eaten more than `wolves_dead_criterion` sheep, this wolf will die. There is a `state` to represent if it is alive. `state = 1` represents the wolf is alive and `state = 0` represents wolf is dead. There will be `new_wolves_partion * alive_number` new wolves born from the living wolves each `born_iteration_wolves` iterations. <u>**Here, we still keep the dead wolves and sheep instead of deleting them, in order to save the position of all wolves and sheep. However, the state of dead wolves and sheep is `0`.**</u>

```python
# Define for wolves
class Wolves():
    
    # Wolves setting
    def __init__(self,wolves,agents,environment,ID):
        self.y = random.randint(0,len(environment))
        self.x = random.randint(0,len(environment[0]))
        self.eatSheep = 0
        self.environment = environment
        self.wolves = wolves
        self.agents = agents
        self.ID = ID
        self.state = 1 # "1" means the sheep is alive, 0 means the sheep is dead 

    def __str__(self):
        return "ID = " + str(self.ID) \
                + ", x=" + str(self.x) \
                + ", y=" + str(self.y) \
                + ", Eat sheep=" + str(self.eatSheep)
                
    # Alter wolves' position randomly
    def move(self,unit_step):
        # Alter agent's x position
        if random.random() < 0.5:
            self.x = (self.x + unit_step) % len(self.environment[0])
        else:
            self.x = (self.x - unit_step) % len(self.environment[0])
        
        # Alter agent's y position
        if random.random() < 0.5:
            self.y = (self.y + unit_step) % len(self.environment)
        else:
            self.y = (self.y - unit_step) % len(self.environment)
            
    # Measure the distance between two agents
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    # Eat sheep when sheep are close to this Wolf
    def find_eat(self, required_distance):
        for agent in self.agents:
            if agent.state == 1 and self.state == 1:
                if self.distance_between(agent) <= required_distance:
                    # Wolf eat sheep
                    self.eatSheep += 1
                    # Sheep dies
                    agent.state = 0
                    # Uncomment next lines to show the distance between Wolf and sheep
                    print("Wolf: " + str(self.ID) \
                          + ", Sheep: " + str(agent.ID) \
                          + ", Distance: " + str(self.distance_between(agent))
                          )
```

The setting in `main.py` is shown below.

```python
	# Move the wolves
    for i in range(num_of_wolves):
        # If eat more than 'wolves_dead_criterion' sheep, this wolf will die
        if wolves[i].eatSheep >= wolves_dead_criterion:
            wolves[i].state = 0
        
        # Wolf eats and moves
        if wolves[i].state == 1:
            wolves[i].move(unit_step_wovle)
            wolves[i].find_eat(required_distance)
            
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
#        print("Current total number of sheep is",num_of_agents)
```



Similarly, there is `state` to represent if sheep is alive. `state = 1` represents the sheep is alive and `state = 0` represents sheep is dead. There will be `new_sheep_partion * alive_number` new sheep born from the living sheep each `born_iteration_sheep` iterations. **All actions are only between wolves and living sheep or between living sheep**, so we add many judgment codes `if agents[i].state == 1` and `if wolves[i].state == 1`. The code for the birth of new sheep is below.

```python
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
        print("Current total number of sheep is",num_of_agents)
```

The output of initial position of all wolves and sheep is below (5 wolves and 10 sheep at the beginning).

`ID = 0, x=215, y=197, Eat sheep=0
ID = 1, x=132, y=20, Eat sheep=0
ID = 2, x=248, y=261, Eat sheep=0
ID = 3, x=155, y=207, Eat sheep=0
ID = 4, x=183, y=244, Eat sheep=0
ID = 0, x=111, y=298, store=0
ID = 1, x=71, y=258, store=0
ID = 2, x=71, y=144, store=0
ID = 3, x=128, y=48, store=0
ID = 4, x=75, y=272, store=0
ID = 5, x=50, y=158, store=0
ID = 6, x=169, y=37, store=0
ID = 7, x=286, y=241, store=0
ID = 8, x=181, y=51, store=0
ID = 9, x=161, y=222, store=0`

We then test if wolves predate sheep in each iteration. If it is, the `ID` of wolf and sheep is printed, as well as their distance. We can find there have been three predation, and details are shown below. The total number of sheep is shown at `step 5`, `step 10`, `step 15`, and `step 20`. The total number of wolves is shown at `step 10` and `step 20`.

`It is 0 step
Wolf: 3, Sheep: 9, Distance: 21.0
It is 1 step
It is 2 step
It is 3 step
It is 4 step
Current total number of sheep is 12
It is 5 step
It is 6 step
It is 7 step
It is 8 step
It is 9 step
Current total number of sheep is 14
Current total number of wolves is 6
It is 10 step
Wolf: 1, Sheep: 0, Distance: 22.02271554554524
It is 11 step
Wolf: 1, Sheep: 13, Distance: 23.259406699226016
It is 12 step
It is 13 step
It is 14 step
Current total number of sheep is 16
It is 15 step
It is 16 step
It is 17 step
It is 18 step
It is 19 step
Current total number of sheep is 19
Current total number of wolves is 7`

We then print the final state of all sheep and visualize the position of all sheep and wolves.

```python
# Uncomment next lines to display environment and agent
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
print("Final states")
for i in range(num_of_agents):
    # Uncomment next lines to print the state for all sheep at the end.
    print("The state for sheep", agents[i].ID, "is", agents[i].state)
    
    if agents[i].state == 1:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'blue')
    else:
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
        
for i in range(num_of_wolves):
    # Uncomment next lines to print the state for all wolves at the end.
    print("Wolf", wolves[i].ID, "eated total", wolves[i].eatSheep, "sheep")
    
    if wolves[i].state == 1:
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'black')
    else:
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color = 'yellow')
matplotlib.pyplot.show()
```

The final states for all sheep are shown below. We can find the states for sheep 0, 9, and 13 are 0 because they have been eaten (shown above). In addition, the number of sheep eaten by each wolf is also shown. Since no wolf has eaten more than `wolves_dead_criterion = 5` sheep, so there is no dead wolf.

`Final states
The state for sheep 0 is 0
The state for sheep 1 is 1
The state for sheep 2 is 1
The state for sheep 3 is 1
The state for sheep 4 is 1
The state for sheep 5 is 1
The state for sheep 6 is 1
The state for sheep 7 is 1
The state for sheep 8 is 1
The state for sheep 9 is 0
The state for sheep 10 is 1
The state for sheep 11 is 1
The state for sheep 12 is 1
The state for sheep 13 is 0
The state for sheep 14 is 1
The state for sheep 15 is 1
The state for sheep 16 is 1
The state for sheep 17 is 1
The state for sheep 18 is 1
Wolf 0 eated total 0 sheep
Wolf 1 eated total 2 sheep
Wolf 2 eated total 0 sheep
Wolf 3 eated total 1 sheep
Wolf 4 eated total 0 sheep
Wolf 5 eated total 0 sheep
Wolf 6 eated total 0 sheep`

The position of all sheep and wolves are shown below. The living and dead sheep are represented by `blue` and `red` points. The living and dead wolves are represented by `black` and `yellow` points. There is no deal wolf, so there is no `yellow` point. We will further test it in a large number of `num_of_iterations`.

<img src="testfigure/wolves.png" alt="wolves" style="zoom:72%;" />

For a large number of iteration `num_of_iterations = 100`, the figure is shown below. The dead wolves are represented by `yellow` points. We can easily find these dead sheep around wolves, and many new sheep and wolves born from the initial `num_of_agents = 10` sheep and initial `num_of_wolves = 5` wolves. With these living wolves, most sheep have been eaten (many `red` rather than `blue` points).

<img src="testfigure/wolves100.png" alt="wolves100" style="zoom:72%;" />

## Ninth module -- GUI/Web scraping

**Test 1**: The code below is used to design GUI.

```python
# =============================================================================
# # GUI Setting
# =============================================================================
# Define the run function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
# Figure initializing
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# GUI design 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# Update rule 
carry_on = True	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    # Plot the environment
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment)
    
    # Move the agents, eat the environment, and share with neighbourhood
    store_total = 0
    for i in range(num_of_agents):
        store_total += agents[i].store
    store_average = store_total/num_of_agents
    
    for i in range(num_of_agents):
        agents[i].move(times_for_move,store_average)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    # Stop condiction based on a random number
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    # Plot the agent
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'red')
		
# Stop condition: (1) Step number (2) Random number
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

tkinter.mainloop()
```

GUI is shown below, so that our code is correct.

<img src="testfigure/GUI_design.png" alt="GUI_design" style="zoom:38%;" />

---

**Test 2**: To read the position of agents from website, we test the code below.

```python
# Uncomment next lines to read the agent position from website
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, i, y, x))
    # Uncomment next line to print the initial position of all agents
    print(agents[i])
```

The definition in the `Agents` class is below.

```python
    # Agent setting
    # Position will be random if do not provide y and x
    def __init__(self,environment,agents,ID,y = None,x = None):
        self.environment = environment
        self.store = 0
        
        # Agent position initializing based on the environment size
        if (y == None):
            self.y = random.randint(0,len(environment))
        else:
            self.y = y
        if (x == None):
            self.x = random.randint(0,len(environment[0]))
        else:
            self.x = x

        self.agents = agents
        self.ID = ID
```

The output of this code is below, and we can find it is the same as the data in the website. Thus, this code is correct.

`ID = 0, x=20, y=73, store=0
ID = 1, x=52, y=91, store=0
ID = 2, x=40, y=52, store=0
ID = 3, x=14, y=93, store=0
ID = 4, x=35, y=48, store=0
ID = 5, x=63, y=11, store=0
ID = 6, x=63, y=70, store=0
ID = 7, x=30, y=19, store=0
ID = 8, x=80, y=42, store=0
ID = 9, x=46, y=20, store=0`