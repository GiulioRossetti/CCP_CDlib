import networkx as nx
from cdlib import algorithms as al
from cdlib import readwrite as io
import argparse, sys, json


def parameters_formatter(params):
    
    params = args.params[1:-1].split(",")

    parameters = {}
    for p in params:
        l = p.replace(" ", "").split(":")

        if l[1] == "True":
            value = True
        elif l[1] == "False":
            value = False
        elif l[1] == "None":
            value = None
        else:
            try:
                value = float(l[1])
            except ValueError:
                try:
                    value = int(l[1])
                except ValueError:
                    value = l[1]
        
        parameters[l[0]] = value
    return parameters


parser=argparse.ArgumentParser()

parser.add_argument("--alg", help="Community detection algorithm")
parser.add_argument("--params", help="dictionary of parameters for the algorithm", default="{}")

args=parser.parse_args()
parameters = parameters_formatter(args.params)

g = nx.read_edgelist("network.csv", delimiter=",")

alg = getattr(al, args.alg)
coms = alg(g, **parameters)
io.write_community_json(coms, "communities.json")