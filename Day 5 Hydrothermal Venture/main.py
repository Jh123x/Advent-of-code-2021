from typing import Generator

class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_node(self, x:int, y:int) -> None:
        if (x,y) not in self.graph:
            self.graph[(x,y)] = 0
        self.graph[(x,y)] += 1

    def get_danger(self) -> int:
        return len(list(filter(lambda x: x > 1, self.graph.values())))

    def __str__(self) -> str:
        return str(self.graph)

    def __len__(self) -> int:
        return len(self.graph)


def process_coords(x1:int, y1:int, x2:int, y2:int) -> Generator:
    if x1 == x2:
        if y2 < y1:
            y1, y2, = y2, y1
        return ((x1, y) for y in range(y1, y2+1))
    elif y1 == y2:
        if x2 < x1:
            x1, x2, = x2, x1
        return ((x, y1) for x in range(x1, x2+1))
    
    y_step = 1
    x_step = 1
    if x1 > x2:
        x_step = -1 
    if y1 > y2:
        y_step = -1
    curr_x, curr_y = x1, y1
    curr = [(x2, y2)]
    while curr_x != x2 or curr_y != y2:
        curr.append((curr_x, curr_y))
        curr_x += x_step
        curr_y += y_step
    return curr
    

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    graph = Graph()
    for line in lines:
        coord1, coord2 = map(lambda x: x.strip(), line.split("->"))
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        for x, y in process_coords(x1, y1, x2, y2):
            graph.add_node(x, y)
    print(graph.get_danger())
        

