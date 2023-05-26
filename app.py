import numpy as np
import random 

rewards = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, -1, -1],
    [0, -1, -1, -1, -1, 100],
])

def set_initial_state():
    return np.random.randint(0, 6)

set_initial_state()

def get_action(current_state, reward_matrix):
    available_action = []
    print("reward_matrix","\n",reward_matrix)    
    for action in enumerate(reward_matrix[current_state]):     
        if action[1]!= -1:            
            available_action.append(action[0]) 
    choose_action = random.choice(available_action)
    print("Random choice of action from",available_action,"is", choose_action)           
    return choose_action


#Call a get_action function
current_state = 3

action = get_action(current_state, rewards)
print(action)




current_state = 4


action = get_action(current_state, rewards)
print(action)