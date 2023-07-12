import networkx as nx
from cdlib import algorithms as al
from cdlib import readwrite as io
import ast, argparse, sys

parser=argparse.ArgumentParser()

# parser.add_argument("--network", help="Network edgelist filename")
parser.add_argument("--alg", help="Community detection algorithm")
parser.add_argument("--params", help="dictionary of parameters for the algorithm", default="{}")

args=parser.parse_args()

print(args)
print(args.params)
params = ast.literal_eval(args.params)

g = nx.read_edgelist("network.csv", delimiter=",")

alg = getattr(al, args.alg)
coms = alg(g, **params)
io.write_community_json(coms, "communities.json")
