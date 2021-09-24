class PageNode:

    def __init__(self, starting_rank: float, 
                id: int,
                incoming: list):
        self.rank_value = starting_rank
        self.id = id
        self.incoming_ids = incoming


class Graph:

    def __init__(self, nodes: list):
        self.nodes = nodes

    def output(self):
        for n in self.nodes:
            print(n.id, n.rank_value, n.incoming_ids)


class PageRankApp:
    def __init__(self, scenario: list, default_rank: float, dampening_factor: float):
        nodes = []
        for i in range(len(scenario)):
            nodes.append(PageNode(default_rank, i, scenario[i]))
        self.graph = Graph(nodes)
        self.iterate(10, dampening_factor)


    def iterate(self, iterations: int, dampening: float):
        for node in self.graph.nodes:
            temp_sum = 0
            temp_sum = temp_sum + node.rank_value / len(node.incoming_ids)
            new_rank = (1 - dampening) + dampening * temp_sum
            print(f"FOR NODE {node.id}: {temp_sum}, OLD RANK: {node.rank_value}, NEW RANK: {new_rank}")

            node.rank_value = new_rank

def main():
    graph_one =  [[1], [0]]
    app = PageRankApp(graph_one, 1, 0.85)

if __name__ == "__main__":
    main()