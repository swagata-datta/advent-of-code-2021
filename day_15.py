'''Advent of Code 2021: day 15

https://adventofcode.com/2021/day/15

12/24/21'''

from collections import defaultdict
from toolkit import *
from graph_utility import *
import numpy as np

exam = np.array([[1,2,3],
                [4,5,6]])

edges = get_edges_from_arr(exam)
graph = Graph(edges)
graph_dict = graph.graph_dict
print(graph_dict)

def dijkstra(graph_dict, start, dist_dict = defaultdict(lambda: 0)):
    




def test():
    str_ = inputfile('input_files/test_files/day_15.txt')
    arr = list_to_arr(str_)

    edges = get_edges_from_arr(arr)
    graph = Graph(edges)
    graph_dict = graph.graph_dict

    print(graph_dict)

#test()