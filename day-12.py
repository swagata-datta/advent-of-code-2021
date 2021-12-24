'''Advent of Code 2021: Day 12

https://adventofcode.com/2021/day/12

12/24/21'''

from toolkit import *
from graph_utility import *
from collections import Counter

def get_edges(inp):
    """returns a list of tuple with connected nodes"""
    inp = [tuple(i.split('-')) for i in inp]
    return inp


def treat_graph_dict(graph_dict):
    """Gets rid of start from the value and end as key"""
    del graph_dict['end']
    for key in graph_dict:
        graph_dict[key] = [i for i in graph_dict[key] if i != 'start']
    return graph_dict


def get_paths(start, end, graph_dict, path = []):
    """Gets the paths between start and end"""
    path = path + [start]

    if start == end:
        return [path]
    
    if start not in graph_dict:
        return []

    all_paths = []
    for node in graph_dict[start]:
        if node.islower():
            if node not in path:
                new_path = get_paths(node, end, graph_dict, path)
                for p in new_path:
                    all_paths.append(p)
        else:
            new_path = get_paths(node, end, graph_dict, path)
            for p in new_path:
                all_paths.append(p)
    
    return all_paths


def paths_part2(start, end, graph_dict, path = []):
    """Gets the paths between start and end"""
    path = path + [start]

    if start == end:
        return [path]
    
    if start not in graph_dict:
        return []

    all_paths = []
    for node in graph_dict[start]:
        if node.islower():
            check_lower = [i for i in path if i.islower()]
            check_dict = Counter(check_lower)
            if max(check_dict.values()) == 2:
                if node not in path:
                    new_path = paths_part2(node, end, graph_dict, path)
                    for p in new_path:
                        all_paths.append(p)
            else:
                new_path = paths_part2(node, end, graph_dict, path)
                for p in new_path:
                    all_paths.append(p)
        else:
            new_path = paths_part2(node, end, graph_dict, path)
            for p in new_path:
                all_paths.append(p)

    return all_paths

def test_1():
    teststring = inputfile('input_files/test_files/day_12.txt')
    test_edges = get_edges(teststring)

    test_graph = Graph(test_edges, directed=False)
    graph_dict = test_graph.graph_dict
    graph_dict = treat_graph_dict(graph_dict)
    print(graph_dict)
    paths = get_paths('start', 'end', graph_dict)

    score_1 = len(paths)

    paths2 = paths_part2('start', 'end', graph_dict)
    score_2 = len(paths2)
    
    return (score_1, score_2)

#print(test_1())
assert test_1() == (10, 36)

def main():
    inp = inputfile('input_files/day_12.txt')
    inp_edges = get_edges(inp)

    inp_graph = Graph(inp_edges, directed=False)
    graph_dict = inp_graph.graph_dict
    graph_dict = treat_graph_dict(graph_dict)

    paths = get_paths('start', 'end', graph_dict)
    paths2 = paths_part2('start', 'end', graph_dict)
    print('Part 1:', len(paths))

    print('Part 2:', len(paths2))

main()
