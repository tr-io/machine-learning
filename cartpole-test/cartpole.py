import gym
import numpy as np

env = gym.make('CartPole-v0')

episode_num = 1

def run_episode(env, parameters):  
    """Runs the env for a certain amount of steps with the given parameters. Returns the reward obtained"""
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        env.render()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

# Random search: try random parameters between -1 and 1, see how long the game lasts with those parameters
def random_search():
    global episode_num
    bestparams = None
    bestreward = 0  
    for _ in range(10000):  
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(env,parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            print("Best reward: " + str(bestreward) + " on episode #" + str(episode_num))
            # considered solved if the agent lasts 200 timesteps
            if reward == 200:
                print("Solved in " + str(episode_num) + " episodes")
                break
            
        episode_num += 1

# Hill climbing algo: add noise to weights
def hill_climbing():
    global episode_num
    episodes_per_update = 10
    noise_scaling = 0.1
    parameters = np.random.rand(4) * 2 - 1
    bestreward = 0
    
    for _ in range(10000):
        newparams = parameters + (np.random.rand(4) * 2 - 1) * noise_scaling
        reward = 0
        
        for _ in range(episodes_per_update):
            run = run_episode(env, newparams)
            reward += run
            episode_num += 1

        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            print("Best reward: " + str(bestreward) + " on episode #" + str(episode_num))
            if reward >= 200:
                print("Solved in " + str(episode_num) + " episodes")
                break

        #episode_num += episodes_per_update

# Policy gradient algo


while True:
    hill_climbing()
    episode_num = 1