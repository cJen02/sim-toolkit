import os
import sys
import time
import math
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="gymnasium")

import numpy as np              # type: ignore
import pandas as pd             # type: ignore
import matplotlib.pyplot as plt # type: ignore
print(f"Python: {sys.version}\n")

import mujoco                   # type: ignore
import myosuite                 # type: ignore
import gymnasium as gym         # type: ignore
# import stable_baselines3        # type: ignore

# import torch                    # pyright: ignore[reportMissingImports]
# import torch.nn as nn           # pyright: ignore[reportMissingImports]
# import torch.optim as optim     # pyright: ignore[reportMissingImports]

print("MuJoCo:", mujoco.__version__)
print("Myosuite:", myosuite.__version__)
print("Gymnasium:", gym.__version__)
# print("Stable Baselines3:", stable_baselines3.__version__)
# print("PyTorch:", torch.__version__)
# print("GPU:", torch.cuda.is_available())

env = gym.make("CartPole-v0")

print(f"Observation space: {env.observation_space}")
print(f"Action space:      {env.action_space}")

obs, _ = env.reset()
env.render()

print(f"\nObservation shape: {obs.shape}")
print(f"First 6 values:    {obs[:6].round(4)}")

time.sleep(10)
env.close()