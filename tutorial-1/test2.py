# tutorial from https://www.oreilly.com/learning/introduction-to-reinforcement-learning-and-openai-gym

import gym
import numpy as np

env = gym.make("Taxi-v2")
env.reset()

Q = np.zeros([env.observation_space.n, env.action_space.n])

G = 0 # total accumulated reward
alpha = 0.618 # learning rate

for episode in range(1, 1001):
    done = False
    G, reward = 0,0
    state = env.reset()
    
    while done != True:
        action = np.argmax(Q[state]) #1
        state2, reward, done, info = env.step(action) #2
        Q[state,action] += alpha * (reward + np.max(Q[state2]) - Q[state,action]) #3
        G += reward
        state = state2

    if episode % 50 == 0:
        print('Episode {} Total Reward: {}'.format(episode,G))
