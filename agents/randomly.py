import os
import time
import random
from argparse import ArgumentParser
import numpy as np
from agents.agent import Agent



KEYS = ['score', 'step']


class Randomly(Agent):
    
    def __init__(self, env, **kwargs):
        super().__init__(env)

    def get_action(self):
        return self.action_space.sample()

    def play(self, render=False, verbose=False, delay=0, ep_label=0, test=True):
        done = False
        score = 0.
        step = 0
        self.env.reset()
        if render:
            self.env.render()
        while not done:            
            time.sleep(delay)
            action = self.get_action()
            if verbose:
                stamp = '[EP%dT%d] [Rew] %.2f' % (ep_label, step, score)
                act_temp = ('{:.3f} ' * len(action)).format(*action)
                print(stamp, act_temp, end='\r', flush=True)
            _, rew, done, info = self.env.step(action)
            step += 1
            score += rew
            if render:
                self.env.render()
        stat = {
            'score': score,
            'step': step,
        }
        if 'end' in info:
            stat['end'] = info['end']
        return stat
    
    def load_model(self, path=None):
        pass

    def save_model(self, path=None):
        pass