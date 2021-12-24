

from collections import defaultdict

routes = [(1,2), (2,3), (1,5), (2,4), (4,5)]

class Graph:
    """"""

    def __init__(self, edges, directed = True):
        self.edges = edges
        self.graph_dict = defaultdict(lambda: [])
        if directed == True:
            for i in edges:
                key, value = i[0], i[1]
                self.graph_dict[key].append(value)
        elif directed == False:
            for i in edges:
                key, value = i[0], i[1]
                self.graph_dict[key].append(value)
                self.graph_dict[value].append(key)

    
    def get_routes(self, start, end, path = [], all_paths = []):
        """Returns list of all routes between start and end"""
        path = path + [start]

        dict_ = self.graph_dict

        if start == end:
            return [path]
        
        if start not in dict_:
            return []
        
        all_paths = []
        
        for node in dict_[start]:
            if node not in set(path):
                new_path = self.get_routes(node, end, path)
                for p in new_path:
                    all_paths.append(p)
                              

        return all_paths





#graph = Graph(routes, directed=False)
##print(graph.graph_dict)
#paths = graph.get_routes(1,4)

#print(paths)


