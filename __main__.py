import networkx as nx
from cdlib import algorithms as al
from cdlib import readwrite as io
import argparse, sys, json

parser=argparse.ArgumentParser()

# parser.add_argument("--network", help="Network edgelist filename")
parser.add_argument("--alg", help="Community detection algorithm")
parser.add_argument("--params", help="dictionary of parameters for the algorithm", default="{}")

args=parser.parse_args()

params = json.loads(args.params, parse_float=float, parse_int=int)

print(f"Params: {params}, type: {type(params)}")

g = nx.read_edgelist("network.csv")
alg = getattr(al, args.alg)
coms = alg(g, **params)
io.write_community_json(coms, "communities.json")