"""
by: Philipp Machácek, Felix Siegmann @ TBS1
"""


class PageNode:
    """
    Class PageNode, represents one page
    """
    def __init__(self, starting_rank: float, 
                id: int,
                incoming: list,
                outgoing: list):
        """
        Constructor of class PageNode
        :param starting_rank: the default rank for this node
        :param id: this node's id
        :param incoming: list of nodes by id who link to this node
        :param outgoing: list of nodes by id this node links to
        """
        self.rank_value = starting_rank
        self.id = id
        self.incoming_ids = incoming
        self.outgoing_ids = outgoing


class Graph:
    """
    Class PageNode, represents a system of interlinked pages
    """
    def __init__(self, nodes: list):
        """
         Constructor of class Graph
         :param nodes: list of nodes this graph contains
         """
        self.nodes = nodes

    def output(self):
        """
        function output
        prints nodes and their values to the screen
        """
        for n in self.nodes:
            print(n.id, n.rank_value, n.incoming_ids, n.outgoing_ids)

    def get_node(self, id:int):
        """
        function get_node
        returns a node contained in this graph by id
        :param id: node id to be searched for
        :return: PageNode with this id
        """
        for node in self.nodes:
            if node.id == id:
                return node


class PageRankApp:
    """
    Class that represents a specific PageRank calculation scenario
    """
    def __init__(self, scenario: list, default_rank: float, dampening_factor: float, iterations: int):
        """
        Constructor of class PageRankApp
        :param scenario: list of lists, each list containing incoming node ids for a node in the scenario
        :param default_rank: Page-Rank nodes start out with
        :param dampening_factor: dampening factor to be applied
        :param iterations: number of iterations to approximate result of system of linear equations for graph
        """
        self.scenario = scenario
        self.default_rank = default_rank
        self.dampening_factor = dampening_factor
        self.graph = Graph(self.build_graph())
        self.graph.output()
        self.iterations = iterations

    def start(self):
        """
        starts execution
        """
        self.iterate(self.iterations, self.dampening_factor)

    def build_graph(self):
        """
        function build_graph
        Initializes list of PageNode-Objects
        sets their rank, id, incoming_ids and outgoing_ids
        :return: list of PageNode-Objects
        """
        nodes = []
        for i in range(len(self.scenario)):
            nodes.append(PageNode(self.default_rank, i, self.scenario[i],
                         [self.scenario.index(n) for n in self.scenario if i in n]))
        return nodes

    def iterate(self, iterations: int, dampening: float):
        """
        function iterate
        function that iterates over system of linear equations a specified amount of times
        uses updated page within each iteration
        """
        # 1) iterate _ times
        for _ in range(iterations):
            # 2) each time, iterate over all nodes in graph
            for node in self.graph.nodes:
                # 3) initialize or reset temp_sum that represents sum of weight of linking nodes
                temp_sum = 0

                # 4) for the current node, iterate over all nodes that link to it
                for id in node.incoming_ids:
                    try:
                        # 5) increment temp_sum by weight of each incoming node
                        temp_sum = temp_sum + self.graph.get_node(id).rank_value / len(self.graph.get_node(id).outgoing_ids)
                        # E) if there are no outgoing links from current node, temp_sum not incremented
                    except ZeroDivisionError:
                        temp_sum = temp_sum

                # 6) update rank for current node using Page-Rank formula using dampening factor
                #    round to the 8th decimal
                node.rank_value = round((1 - dampening) + dampening * temp_sum, 8)


def main():
    """
    main function
    contains test scenarios
    scenarios are represented by list of lists, each list representing a node and containing all ids that link to it
    """
    graph_one = [[1], [0]]
    graph_two = [[1], [0], [2]]
    graph_three = [[1], [0], [0, 1]]
    graph_four = [[], [0], [1]]
    # 1) Initialize specific PageRank-Scenario
    #    params in order: scenario, starting rank for all nodes, dampening factor, iterations)
    app = PageRankApp(graph_three, 99999, 0.85, 15)
    # 2) Start Execution)
    app.start()


if __name__ == "__main__":
    main()