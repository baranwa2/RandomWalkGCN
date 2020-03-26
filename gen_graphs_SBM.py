# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:37:04 2020

@author: mayank
"""

import networkx as nx
import numpy as np
import random

p1, p2, q = 0.6, 0.3, 0.1
tau = 0.05

k1, k2 = 0.4, 0.6

n = 1000

for i in range(100):
    sizes = [int(k1*n), int(k2*n)]
    probs = [[p1, q], [q, p2]]
    
    g = nx.stochastic_block_model(sizes, probs, seed=random.randint(0, 20000))
    nx.write_gpickle(g, 'graph_' + str(i+1) + '.gpickle')
    
for i in range(100,200):
    sizes = [int(k1*n), int(k2*n)]
    probs = [[p1+tau/k1, q-tau/k2], [q-tau/k2, p2+tau*k1/(k2*k2)]]
    
    g = nx.stochastic_block_model(sizes, probs, seed=random.randint(0, 20000))
    nx.write_gpickle(g, 'graph_' + str(i+1) + '.gpickle')