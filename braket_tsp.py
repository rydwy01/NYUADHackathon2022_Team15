import boto3
from braket.aws import AwsDevice
from braket.ocean_plugin import BraketSampler, BraketDWaveSampler
import numpy as np
import networkx as nx
import dimod
import dwave_networkx as dnx
from dimod.binary_quadratic_model import BinaryQuadraticModel
from dwave.system.composites import EmbeddingComposite
import matplotlib.pyplot as plt
from collections import defaultdict
import itertools
import pandas as pd
from utils_tsp import get_distance, traveling_salesperson
!/usr/bin/env python
coding: utf-8

# ## IMPORTS AND SETUP


# fix random seed for reproducibility
seed = 1
np.random.seed(seed)


def run_braket_tsp(map_file):
    # load dataset
    data = pd.read_csv(map_file, sep='\s+', header=None)

    # distance between two example cities
    idx_city1 = 0
    idx_city2 = 1
    distance = data[idx_city1][idx_city2]
    print('Distance between city {} and city {} is {}.'.format(
        idx_city1, idx_city2, distance))

    # get number of cities
    number_cities = data.shape[0]
    print('Total number of cities:', number_cities)

    # ## SET UP GRAPH

    G = nx.from_pandas_adjacency(data)
    pos = nx.spring_layout(G, seed=seed)

    nodes = G.nodes()
    edges = G.edges()
    weights = nx.get_edge_attributes(G, 'weight')

    # print weights of graph
    print('Weights of graph:', weights)

    # show graph with weights
    plt.axis('off')
    nx.draw_networkx(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    # get QUBO for TSP
    tsp_qubo = dnx.algorithms.tsp.traveling_salesperson_qubo(G)

    lagrange = None
    weight = 'weight'

    # get corresponding QUBO step by step
    N = G.number_of_nodes()

    if lagrange is None:
        # If no lagrange parameter provided, set to 'average' tour length.
        # Usually a good estimate for a lagrange parameter is between 75-150%
        # of the objective function value, so we come up with an estimate for
        # tour length and use that.
        if G.number_of_edges() > 0:
            lagrange = G.size(weight=weight) * \
                G.number_of_nodes()/G.number_of_edges()
        else:
            lagrange = 2

    print('Default Lagrange parameter:', lagrange)

    # In[16]:

    # create list around default value for HPO
    lagrange_list = list(np.arange(int(0.8*lagrange), int(1.1*lagrange)))
    print('Lagrange parameter for HPO:', lagrange_list)

    # run TSP with imported TSP routine
    sampler = BraketDWaveSampler(
        device_arn='arn:aws:braket:::device/qpu/d-wave/DW_2000Q_6')
    sampler = EmbeddingComposite(sampler)

    # set parameters
    num_shots = 1000
    start_city = 0
    best_distance = sum(weights.values())
    best_route = [None]*len(G)

    # run HPO to find route
    for lagrange in lagrange_list:
        print('Running quantum annealing for TSP with Lagrange parameter=', lagrange)
        route = traveling_salesperson(G, sampler, lagrange=lagrange,
                                      start=start_city, num_reads=num_shots, answer_mode="histogram")
        # print route
        print('Route found with D-Wave:', route)

        # print distance
        total_dist, distance_with_return = get_distance(route, data)

        # update best values
        if distance_with_return < best_distance:
            best_distance = distance_with_return
            best_route = route

    print('---FINAL SOLUTION---')
    print('Best solution found with D-Wave:', best_route)
    print('Total distance (including return):', best_distance)

    with open("braket_solution.txt", "w") as f:
        f.write("optimal route: " + best_route)
        f.write("optimal distance: " + best_distance)
    return "braket_solution.txt"
