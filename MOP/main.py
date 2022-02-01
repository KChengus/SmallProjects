

from Functions.functions import compareTo
from MOP.countries_information import *

"""
Continue Working on this project in the future

Areas of improvement and additional features:

* Make a GUI
* Create a file that displays all the routes of each and every single country in countries_information file
* Learn about how to use APIs in order to get information from the web about flight durations

"""
class CountryNode:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

class Main:

    def neighbor_to_node(self, name_node):
        # all countries at this point have been asigned a node
        for country_name, country_node in name_node.items():
            node_neighbors = list()
            for neighbor in country_and_path[country_name]:
                node_neighbors.append(name_node[neighbor])
            country_node.neighbors = node_neighbors
        return name_node

    def make_country_nodes(self):
        # visited {name : node}
        name_node = {}
        # get first value in country_and_path
        # remember that lists are passed as references and not as values unlike other data
        # types such as int, str etc.
        # this seach can use both the stack and queue algorithm
        stack = [next(iter(country_and_path))]
        while (stack):
            length = len(stack)
            for _ in range(length):
                #  TODO -- clean this portion of code --

                # country name and its neighbors
                country_name = stack.pop(-1)
                country_neighbors = country_and_path[country_name]
                # check for unvisited countries
                for country_neighbor in country_neighbors:
                    if (country_neighbor not in name_node):
                        stack.append(country_neighbor)

                # create a node with empty neighbors, neighbors will be added later
                # add it to the visited dictionary along with its neighbors
                new_node = CountryNode(country_name, None)
                name_node[country_name] = new_node

        return self.neighbor_to_node(name_node)

    def determine_travel_time(self, cur_location, destination):
        if (len(cur_location) < 2 or len(destination) < 2):
            raise Exception(f"The length of {cur_location} or {destination} is too short thus creating this error message")
        cur_location = cur_location[:2].upper()
        destination = destination[:2].upper()
        if (compareTo(cur_location, destination) > 0):
            # destination comes before cur_location
            ret = f"{destination}-{cur_location}"
        else:
            ret = f"{cur_location}-{destination}"

        return travel_distance[ret]

    def search(self, name_node, cur_location, target_location, total_travel_time, max_flights, flight_count):
        temp = list()
        def BTS(cur_location, total_travel_time, flight_count):
            # recursive
            if (cur_location == target_location):
                return total_travel_time
            elif (flight_count >= max_flights):
                return -1

            for neighbor_node in name_node[cur_location].neighbors:
                destination = neighbor_node.name
                travel_time = self.determine_travel_time(cur_location, destination)
                ret_time = BTS(destination, total_travel_time + travel_time, flight_count + 1)
                if (ret_time != -1 and ret_time):
                    temp.append(ret_time)
        BTS(cur_location, total_travel_time, flight_count)
        if (not temp):
            temp.append(0)
        return temp


if __name__ == "__main__":
    # {name : node}
    # node have a name and neighbor
    main = Main()
    name_node = main.make_country_nodes()


    cur_location = "Sweden"
    destination = "China"
    total_travel_time = 0
    flight_count = 0
    time = main.search(name_node, cur_location, destination, total_travel_time, max_flights, flight_count)

    #print(time)
    print(f"From {cur_location} to {destination}: ", end="")
    print(min(time), "hours")



