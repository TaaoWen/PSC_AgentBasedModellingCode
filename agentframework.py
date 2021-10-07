# agentframework.py
'''
Agent Based Modelling
This Python code is a used as the practicals (Agent Based Modelling) for the module "Programming for Social Science".
This is the definition for Agents classes that are used in "main.py". More detail can be found in comments below.

@author: Tao Wen
@Version: Final
'''

import random

# Definition of sheep
class Agent():

    def __init__(self,environment,agents,ID,y = None,x = None):
        """
        Agent setting (define)
        Position will be random if do not input y and x, that is, type "agentframework.Agent(environment,agents,ID)"
        
        Parameters
        ----------
        environment: list
            The input environment matrix
                        
        agents: list
            The list of agents
                        
        ID: float
            The ID of agents
                        
        y: float, optional (default=None)
            The position of the agent in y axis
                        
        x: float, optional (default=None)
            The position of the agent in x axis
        """
        self.environment = environment # environment input
        self.store = 0 # initial store input
        
        # Agent position initializing based on the environment size
        if (y == None): # no input -- randomization
            self.y = random.randint(0,len(environment))
        else: # input
            self.y = y
        if (x == None):# no input -- randomization
            self.x = random.randint(0,len(environment[0]))
        else: # input
            self.x = x

        self.agents = agents # agent list input
        self.ID = ID # agent ID input
        self.state = 1 # the state of this sheep, "1" means the sheep is alive, 0 means the sheep is dead 
        
    def __str__(self):
        """
        print the information of the agent, including ID, x and y positio, as well as the store
        """
        return "ID = " + str(self.ID) \
                + ", x=" + str(self.x) \
                + ", y=" + str(self.y) \
                + ", store=" + str(self.store)
    
    def move(self,times_for_move,store_average):
        """
        Alter agent's position randomly
        Sheep move more quickly if their store is "times_for_move" times the average storage
        Store is high --> move 2 units each step
        Store is low --> move 1 unit each step
        Agents that leave the top of an area come in at the bottom, and come in on the right when they leave left. 
        This effectively makes the space into a giant doughnut shape, or "torus".
        
        Parameters
        ----------
        times_for_move: float
            The threshold that we defined to move faster
                        
        store_average: float
            Average store of all agents
        """
        if self.store > times_for_move * store_average: # store is high --> move 2 units each step
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
        else: # store is low --> move 1 unit each step
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
    
    def eat(self):
        """
        Eat the environment, the agent will not leave negative values and sick up their store
        Sheep return store under insufficient environmental store
        Sheep return store if they have too much (>=100)
        """
        if self.environment[self.y][self.x] > 10: # eat normally, +10
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: # Insufficient environmental store, sheep return store  
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        if self.store >= 100: # sheep return store if they have too much (>=100)
            self.environment[self.y][self.x] += 100
            self.store = 0
        
    def distance_between(self, agent):
        """
        Obtain the distance between current agent with another agent based on the Euclidean Distance
        
        Parameters
        ----------
        agent: agentframework.Agent
            The framework of one agent
            
        Returns
        -------
        distance_obtain: float
            The distance between two agents based on Euclidean distance
        """
        distance_obtain = (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        return distance_obtain
    
    def share_with_neighbours(self, neighbourhood):
        """
        Share the stores with neighbour agents within the distance "neighbourhood"
        The agent with lower store can steal more resources (3/4 of the overall store) from the other one
        The agent with higher store can only obtain the minor part (1/4) of the overall store
        If two agents have the same store, both of them obtain 1/2 of the overall store
        
        Parameters
        ----------
        neighbourhood: float
            The distance that agents can share the stores
        """
        for agent in self.agents: # each agent
            if self.ID != agent.ID: # non-self
                if agent.state == 1: # Only two living sheep can share
                    dist = self.distance_between(agent) # obtain the distance between them, refer to the function "distance_between"
                    if dist <= neighbourhood: # share within the distance
#                        # Uncomment next lines to show the store for two agents
#                        print("Original store for Agent A is " + str(self))
#                        print("Original store for Agent B is " + str(agent))
                        OverallStore = self.store + agent.store # Overall store
                        
                        # Agents with lower store can steal more resources (3/4) from others
                        if self.store > agent.store:
                            agent.store = 3 * OverallStore / 4
                            self.store = OverallStore / 4
                        if self.store < agent.store:
                            agent.store = OverallStore / 4
                            self.store = 3 * OverallStore / 4
                        else: # the store of two agents is the same
                            agent.store = OverallStore / 2
                            self.store = OverallStore / 2
    
# =============================================================================
#                         # Uncomment next line to print the information from two agents that share the stores
#                         print("The distance between Agents " + str(self) + " Agents " + str(agent) \
#                               + " is " + str(dist) \
#                               + ", so they can share the store within the distance " + str(neighbourhood) \
#                               + ", and the average store should be " + str(OverallStore / 2))
# =============================================================================


# Definition of wolves
class Wolves():
    
    # Wolves setting
    def __init__(self,wolves,agents,environment,ID):
        """
        Agent setting (define)
        Position will be random if do not input y and x, that is, type "agentframework.Agent(environment,agents,ID)"
        
        Parameters
        ----------             
        wolves: list
            The list of wolves
                        
        agents: list
            The list of sheep

        environment: list
            The input environment matrix
            
        ID: float
            The ID of wolves
        """
        self.y = random.randint(0,len(environment)) # Agent y position initializing (randomization) based on the environment size
        self.x = random.randint(0,len(environment[0])) # Agent x position initializing (randomization) based on the environment size
        self.eatSheep = 0 # The number of sheep that this wolf has already eaten (it is 0 at the beginning)
        self.environment = environment  # environment input
        self.wolves = wolves # wolves list input
        self.agents = agents # sheep list input
        self.ID = ID # agent ID
        self.state = 1 # the state of this wolf, "1" means the sheep is alive, 0 means the sheep is dead 

    def __str__(self):
        """
        print the information of the wolf, including ID, x and y positio, as well as the number of sheep that this wolf has already eaten
        """
        return "ID = " + str(self.ID) \
                + ", x=" + str(self.x) \
                + ", y=" + str(self.y) \
                + ", Eat sheep=" + str(self.eatSheep)
                
    # Alter wolves' position randomly
    def move(self,unit_step):
        """
        Alter wolf's position randomly
        wolf move "unit_step" units each step
        Agents that leave the top of an area come in at the bottom, and come in on the right when they leave left. 
        This effectively makes the space into a giant doughnut shape, or "torus".
        
        Parameters
        ----------
        unit_step: float
            The wolf moves "unit_step" units each step
        """
        # Alter wolf's x position
        if random.random() < 0.5:
            self.x = (self.x + unit_step) % len(self.environment[0])
        else:
            self.x = (self.x - unit_step) % len(self.environment[0])
        
        # Alter wolf's y position
        if random.random() < 0.5:
            self.y = (self.y + unit_step) % len(self.environment)
        else:
            self.y = (self.y - unit_step) % len(self.environment)
            
    def distance_between(self, agent):
        """
        Obtain the distance between current wolf and one sheep based on the Euclidean Distance
        
        Parameters
        ----------
        agent: agentframework.Agent
            The framework of one sheep
            
        Returns
        -------
        distance_obtain: float
            The distance between one wolf and one sheep based on Euclidean distance
        """
        distance_obtain = (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        return distance_obtain

    def find_eat(self, required_distance):
        """
        Wolf eats sheep when sheep are close to this Wolf (within the distance "required_distance")
        
        Parameters
        ----------
        required_distance: float
            The distance that the wolf can eat the sheep
        """
        for agent in self.agents: # each sheep
            if agent.state == 1 and self.state == 1: # if sheep and wolf are alive
                if self.distance_between(agent) <= required_distance: # within the distance
                    self.eatSheep += 1 # This wolf eat sheep
                    agent.state = 0 # Sheep dies
#                    # Uncomment next lines to show the distance between Wolf and sheep
#                    print("Wolf: " + str(self.ID) \
#                          + ", Sheep: " + str(agent.ID) \
#                          + ", Distance: " + str(self.distance_between(agent))
#                          )
