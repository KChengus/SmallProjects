import random
class Vertices:
    def __init__(self, val=-1, neighbors=[]):
        self.val = val
        self.neighbors = neighbors



def create():
    length = random.randint(2, 5)
    values = [random.randint(1, 10) for _ in range(length)]
    neighbors = [set([random.randrange(0, length) for _ in range(2)]) for _ in range(length)]
    print(values, neighbors)
    return values, neighbors

def finalize(values, neighbors):
    for i in range(len(values)):
        values[i] = Vertices(values[i])
    # values list will only consist of Verticies instances
    for i in range(len(values)):
        values[i].neighbors = [values[neighborIndex] for neighborIndex in neighbors[i]]
    return values
values, neighbors = create()
graph = finalize(values, neighbors)

for vertex in graph:
    print("Value: " + str(vertex.val) + " Neighbors: ", end="")
    
    for neighbor in vertex.neighbors:
        print(str(neighbor.val), end=" ")
    print()
