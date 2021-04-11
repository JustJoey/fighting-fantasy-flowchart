import networkx as nx
import matplotlib.pyplot as plt
import json 

class FlowchartGenerator:

    def __init__(self, datafile: str) -> None:

        with open(datafile, "r") as read_file:
            self.data = json.load(read_file)
        self.flowchart = nx.DiGraph()
        self.data_to_flowchart()

    def data_to_flowchart(self):
        self.generate_nodes()
        self.generate_edges() 

    def generate_nodes(self):
        for node in self.data:
            self.flowchart.add_node(node['id'])

    def generate_edges(self):
        for node in self.data:
            for destination in node['paths']:
                self.flowchart.add_edge(node['id'], destination)

    def display_flowchart(self):
        nx.drawing.nx_pylab.draw_networkx(
            self.flowchart, 
            pos=nx.spectral_layout(G)
        )
        plt.savefig("output.png")

if __name__ == "__main__":

    example_file = "assassins_of_allansia.json"

    fg = FlowchartGenerator(example_file)
    print(fg.data)
    
    fg.display_flowchart()