from graphviz import Digraph
import json 

class FlowchartGenerator:

    def __init__(self, datafile: str) -> None:

        with open(datafile, "r") as read_file:
            self.data = json.load(read_file)
        self.flowchart = Digraph(comment=datafile)
        self.flowchart.attr('node', shape='box', style='rounded')
        self.data_to_flowchart()

    def data_to_flowchart(self):
        self.generate_nodes()
        self.generate_edges() 

    def generate_nodes(self):
        for node in self.data:
            self.flowchart.node(node['id'], self.generate_label(node))

    def generate_edges(self):
        for node in self.data:
            for destination in node['paths']:
                label = destination['label'] if 'label' in destination else ''
                self.flowchart.edge(node['id'], destination['id'], label=label)

    def generate_label(self, label_dict: dict) -> str:
        label = f"<<b>{label_dict['id']}</b>"
        if 'notes' in label_dict:
            for note in sorted(label_dict['notes']):
                label += "<br/>" + self.formatted_label(note)
        label += ">"
        return label

    @staticmethod
    def formatted_label(label: str) -> str:
        if ',' in label:
            return f"<font color='blue'>{label}</font>"
        if label[0] == '+':
            return f"<font color='green'>{label}</font>"
        if label[0] == '-':
            return f"<font color='red'>{label}</font>"
        if label == "Test Your Luck":
            return f"<i>{label}</i>"
        return f"<font color='purple'>{label}</font>"

    def display_flowchart(self):
        self.flowchart.render('output', view=False)

if __name__ == "__main__":

    example_file = "assassins_of_allansia.json"

    fg = FlowchartGenerator(example_file)
    # print(fg.data)
    
    fg.display_flowchart()