import gym
import numpy as np
import random

env = gym.make("BipedalWalker-v2")

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range (500):
        env.render()
        action = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

# Hill climbing test

def hill_climbing():
    noise_scaling = 0.1
    parameters = random.uniform(-1.0, 1.0)
    bestreward = 0

    for _ in range (10000):
        newparams = parameters + (random.uniform(-1, 1))*noise_scaling
        reward = 0
        reward = run_episode(env, newparams)
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            print("Best reward: " + str(bestreward))
            if reward == 300:
                break
        
        print("Previous reward: " + str(reward))

while True:
    hill_climbing()