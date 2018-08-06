#tutorial from https://www.oreilly.com/learning/introduction-to-reinforcement-learning-and-openai-gym
import gym
import numpy as np

env = gym.make("MsPacman-v0")
state = env.reset()

reward, info, done = None, None, None

while done != True:
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()