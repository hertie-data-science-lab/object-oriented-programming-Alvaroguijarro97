# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np
import random
#from Creatures import Bear
#from Creatures import Fish

class River:
    
    def __init__(self, n_room, ecosystem = []):
        self.n_room = n_room
        self.ecosystem = ecosystem

    def initialize(self):
        for i in range(self.n_room):
            self.ecosystem.append(random.choice(["Bear", "Fish", None]))
        return self.ecosystem

    def display(self):
        print("===================", "\n")
        print("Number of positions:", self.n_room, "\n")
        print("Ecosystem status:", self.ecosystem, "\n")
        print("===================")








