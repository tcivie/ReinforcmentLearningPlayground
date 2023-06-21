# ReinforcementLearningPlayground
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenAI Gym](https://img.shields.io/badge/OpenAI%20Gym-0081A7?style=for-the-badge&logo=openai&logoColor=white)
![W&B](https://img.shields.io/badge/Weights%20&%20Biases-FE7A16?style=for-the-badge&logo=weights-and-biases&logoColor=white)

Welcome to my Reinforcement Learning Playground! This repository serves as my hands-on lab to explore, understand, and implement reinforcement learning algorithms.

## Project Description

The goal of this project is to create a comprehensive guide to understanding and building reinforcement learning algorithms. The algorithms are demonstrated in the context of the The Farama Foundation's Gym, previously known as OpenAI's Gym. Gym provides a wide variety of environments to test and compare these algorithms' performances.

In this project, we focus on Q-Learning, a simple yet powerful value-based reinforcement learning algorithm. The entire learning process is captured and optimized using Weights and Biases, a tool that allows tracking and visualizing metrics during the training process. This helps in understanding the learning dynamics and optimizing the hyperparameters for the best performance.

## Key Features

Implementation of Q-Learning algorithm: A value-based RL algorithm that learns the optimal policy for decision-making problems.
Hyperparameter tuning: Utilizing Weights and Biases' sweep feature, various hyperparameters for the learning algorithm are experimented with to find the best performing ones.
Performance Metrics: Tracks and visualizes several key performance metrics such as reward per episode, steps per episode, and epsilon (for ε-greedy policy) over the course of learning.
Code modularity: The code is divided into multiple functions for better readability and easy debugging.
## How to use

This project is built and tested in Deepnote, a powerful online Jupyter notebook platform. To run this notebook:

1. Clone the repository to your local machine.
2. Upload the notebook to Deepnote.
3. Ensure that you have the necessary libraries installed (check the import statements at the top of the notebook).
4. Run the cells to train the Q-Learning algorithm.
5. Monitor the training progress and results in the Weights and Biases dashboard.

## 
I invite you to explore this playground and hope it serves as a useful resource in your own reinforcement learning journey! Your suggestions and contributions to improve this guide are most welcome. Enjoy learning!
