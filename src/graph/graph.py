from graph.relationship import Relationship
from graph.node import Node


class Graph:

    def __init__(self, vector, nodes, connections):
        self.vector = vector
        self.name = vector.name
        self.nodes = nodes
        self.connections = connections
        pass

    def add_node(self, node):
        self.nodes.append(node)

    def add_connector(self, relationship):
        self.connections.append(relationship)

    # other setters and getters
