from gym.envs import box2d
import gym
import base64
import numpy as np

class LunarLander:
    def __init__(self):
        self.env = gym.make("LunarLander-v2")
        self.observation = self.env.reset()

    def step(self, action):
        self.observation, reward, done, info = self.env.step(action)
        return self.observation, reward, done, info

    def reset(self):
        self.observation = self.env.reset()

    def render(self):
        return self.env.render()


lunar_lander = LunarLander()
