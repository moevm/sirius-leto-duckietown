#!/usr/bin/env python
# manual

"""
TBD - описание
"""
# Модули сторонних библиотек
from PIL import Image
from PIL import ImageFilter
import argparse
import sys
#import pandas as pd
import gym
import cv2
import numpy as np
import pyglet
from pyglet.window import key
import apriltag
# Модули DuckieTown
from gym_duckietown.envs import DuckietownEnv


# Модули наших рук
from graph.compose_full_path import compose_full_path
from detector.moments import get_action, get_contour_equation
from wrappers import small_right_turn
from wrappers import small_left_turn
from wrappers import wide_right_turn
from wrappers import wide_left_turn
from detector.detector_by_bgr import detector_by_bgr
parser = argparse.ArgumentParser()
#parser.add_argument("--env-name", default=None)
#Duckietown-udem1-v0'
parser.add_argument("--env-name", default='Duckietown-udem1-v0')
parser.add_argument("--map-name", default="udem1")
#parser.add_argument("--env-name", default='MultiMap-v0')
#parser.add_argument("--map-name", default="robotarium1")
parser.add_argument("--distortion", default=False, action="store_true")
parser.add_argument("--camera_rand", default=False, action="store_true")
parser.add_argument("--draw-curve", action="store_true", help="draw the lane following curve")
parser.add_argument("--draw-bbox", action="store_true", help="draw collision detection bounding boxes")
parser.add_argument("--domain-rand", action="store_true", help="enable domain randomization")
parser.add_argument("--dynamics_rand", action="store_true", help="enable dynamics randomization")
parser.add_argument("--frame-skip", default=1, type=int, help="number of frames to skip")
parser.add_argument("--seed", default=1, type=int, help="seed")
args = parser.parse_args()

if args.env_name and args.env_name.find("Duckietown") != -1:
    env = DuckietownEnv(
        seed=args.seed,
        max_steps=10000,
        map_name=args.map_name,
        draw_curve=args.draw_curve,
        draw_bbox=args.draw_bbox,
        domain_rand=args.domain_rand,
        frame_skip=args.frame_skip,
        distortion=args.distortion,
        camera_rand=args.camera_rand,
        dynamics_rand=args.dynamics_rand,
    )
else:
    env = gym.make(args.env_name)



#top_down
#human
RENDER_PARAM = 'human'




env.reset()
env.render(RENDER_PARAM)


@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
    """
    This handler processes keyboard commands that
    control the simulation
    """

    if symbol == key.BACKSPACE or symbol == key.SLASH:
        print("RESET")
        env.reset()
        env.render(RENDER_PARAM)
    elif symbol == key.PAGEUP:
        env.unwrapped.cam_angle[0] = 0
    elif symbol == key.ESCAPE:
        env.close()
        sys.exit(0)

# Register a keyboard handler
key_handler = key.KeyStateHandler()
env.unwrapped.window.push_handlers(key_handler)

action = np.array([0.0, 0.0])
forward_counter = 0



def check_vertexes(pos):
    if 0.7 < pos[0] < 1.22 and 1.8 < pos[2] < 2.35:
        return 1
    if 1.78 < pos[0] < 2.35 and 0 < pos[2] < 1.20:
        return 2
    if 1.78 < pos[0] < 2.35 and 1.77 < pos[2] < 2.35:
        return 3
    if 1.75 < pos[0] < 2.35 and 2.90 < pos[2] < 3.40:
        return 4
    return -1


def update(dt):
    """
    This function is called at every frame to handle
    movement/stepping and redrawing
    """
    wheel_distance = 0.102
    min_rad = 0.08
    global action
    global forward_counter
    
    #action = np.array([0.0, 0.0])

    if key_handler[key.UP]:
        action += np.array([0.44, 0.0])
    if key_handler[key.DOWN]:
        action -= np.array([0.44, 0])
    if key_handler[key.LEFT]:
        action += np.array([0, 1])
    if key_handler[key.RIGHT]:
        action -= np.array([0, 1])
    if key_handler[key.SPACE]:
        action = np.array([0, 0])
    

    # if key_handler[key.E]:
    #     action += np.array([0.2, -1])
    if key_handler[key.Q]:
        wide_left_turn(action)
    if key_handler[key.E]:
        wide_right_turn(action)
    if key_handler[key.D]:
        small_right_turn(action)
    if key_handler[key.A]:
        small_left_turn(action)
    
    # v1 = action[0]
    # v2 = action[1]
    # # Limit radius of curvature
    # if v1 == 0 or abs(v2 / v1) > (min_rad + wheel_distance / 2.0) / (min_rad - wheel_distance / 2.0):
    #     # adjust velocities evenly such that condition is fulfilled
    #     delta_v = (v2 - v1) / 2 - wheel_distance / (4 * min_rad) * (v1 + v2)
    #     v1 += delta_v
    #     v2 -= delta_v

    # action[0] = v1
    # action[1] = v2


    # Speed boost
    if key_handler[key.LSHIFT]:
        action *= 1.5

    
    obs, reward, done, info = env.step(action)
    action = np.array([0.0, 0.0])
    if env.unwrapped.step_count % 5 == 1:

        im = Image.fromarray(obs)
        im = np.asarray(im)
        im = im[:,:,::-1].copy()

        


        y_max = im.shape[0]
        x_max = im.shape[1]
        im = im[int(y_max/2):y_max]


        #жёлтый
        im = detector_by_bgr(im, [10, 100, 100], [150, 250, 250], True, [150, 100, 250])
        #красный
        im = detector_by_bgr(im, [0,0,140], [150,115,230], True, [100,200,100])


        coords = get_action(im)

        get_contour_equation(im)

        if coords[0] != 0 and coords[0] is not None:
            cv2.circle(im, coords, 5, (255, 255, 255), -1)






        print(compose_full_path())
        



        y_max = im.shape[0]
        x_max = im.shape[1]
        obr = im[int(y_max/3):y_max]
        cv2.imwrite(f"screenshots/frame_{int(env.unwrapped.step_count / 10)}.png", im)
        
    if forward_counter > 0:
        forward_counter -= 1
        action[0] = 1
        action[1] = 1





    if done:
        print("done!")
        env.reset()
        env.render(RENDER_PARAM)

    env.render(RENDER_PARAM)


pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)


#pyglet.clock.schedule_interval(update, 0.01)


pyglet.app.run()

env.close()



# def compute():
