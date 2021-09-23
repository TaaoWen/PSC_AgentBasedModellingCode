# agentframework.py
import random

# Define for sheep
class Agent():
    
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
        self.state = 1 # "1" means the sheep is alive, 0 means the sheep is dead 
        
    def __str__(self):
        return "ID = " + str(self.ID) \
                + ", x=" + str(self.x) \
                + ", y=" + str(self.y) \
                + ", store=" + str(self.store)
    
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
        
    # Measure the distance between two agents
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    # Share the stores with neighbour agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if self.ID != agent.ID:
                if agent.state == 1:
                    dist = self.distance_between(agent)
                    if dist <= neighbourhood:
#                        print("Original store for Agent A is " + str(self))
#                        print("Original store for Agent B is " + str(agent))
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
    
# =============================================================================
#                         # Uncomment next line to print the information from two agents that share the stores
#                         print("The distance between Agents " + str(self) + " Agents " + str(agent) \
#                               + " is " + str(dist) \
#                               + ", so they can share the store within the distance " + str(neighbourhood) \
#                               + ", and the average store should be " + str(OverallStore / 2))
# =============================================================================


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
                    # Sheep dies; Please comment this line when do not consider the predation
                    agent.state = 0
#                    # Uncomment next lines to show the distance between Wolf and sheep
#                    print("Wolf: " + str(self.ID) \
#                          + ", Sheep: " + str(agent.ID) \
#                          + ", Distance: " + str(self.distance_between(agent))
#                          )
