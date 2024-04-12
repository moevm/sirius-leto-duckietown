import numpy as np
def small_right_turn(action):
    action += np.array([0.2, -1])
def small_left_turn(action):
    action += np.array([0.2, 1])
def wide_right_turn(action):
    action += np.array([0.38, -1])
def wide_left_turn(action):
    action += np.array([0.38, 1])