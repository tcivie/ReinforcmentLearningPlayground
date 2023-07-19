import gym
import cv2
import base64
import numpy as np

class LunarLander:
    def __init__(self):
        self.env = gym.make("LunarLander-v2", render_mode='rgb_array')
        self.observation = self.env.reset()
        self.reward = 0

    def step(self, action):
        self.observation, reward, self.done, _ = self.env.step(action)
        self.reward += reward

    def get_state(self):
        # Convert the game frame to JPEG
        frame = self.env.render()
        _, buffer = cv2.imencode('.jpg', frame)
        jpeg_image = base64.b64encode(buffer).decode()

        return {
            'image': jpeg_image,
            'reward': self.reward
        }

    def reset(self):
        self.observation = self.env.reset()
        self.reward = 0

lunar_lander = LunarLander()
