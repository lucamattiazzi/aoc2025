with open("./day11/input1.txt") as f:
    lines = f.readlines()

nodes = {}
starting_nodes = []

for line in lines:
    node, connections = line.strip().split(":")
    connections = connections.strip().split(" ")
    if node == "svr":
        starting_nodes.append(node)
    nodes[node] = {"connections": connections, "node": node}

total_roads = 0


def does_go_out(node, road=[]):
    global total_roads
    connections = node["connections"]
    if "out" in connections:
        if "dac" in road and "fft" in road:
            total_roads += 1
    else:
        for connection in connections:
            does_go_out(nodes[connection], [*road, node["node"]])
    return False


for starting_node in starting_nodes:
    node = nodes[starting_node]
    goes_out = does_go_out(node)

print(total_roads)
