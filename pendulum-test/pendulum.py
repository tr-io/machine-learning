import gym
import numpy as np

env = gym.make('Pendulum-v0')

episode_num = 1

def run_episode(env, parameters):
    