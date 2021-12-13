from collections import defaultdict


class Day12:
    def __init__(self, input="src/input/day12.txt"):
        self.INPUT = input

    def read_input(self):
        graph = defaultdict(list)
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()
            for line in lines:
                x, y = line.strip().split("-")
                graph[x].append(y)
                graph[y].append(x)
        return graph

    def find_all_paths_part1(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if (node.islower() and node not in path) or node.isupper():
                newpaths = self.find_all_paths_part1(graph, node, end, path[:])
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def part1(self):
        graph = self.read_input()
        paths = self.find_all_paths_part1(graph, "start", "end")
        return len(paths)

    def count_of_node_in_path(self, node, path):
        count = 0
        for existing_node in path:
            if existing_node == node:
                count += 1
        return count

    def find_all_paths_part2(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            count = self.count_of_node_in_path(node, path)

            expand = False
            if node.isupper():
                expand = True
            else:
                if count == 0:
                    expand = True
                elif count == 1:
                    if node == "start" or node == "end":
                        continue
                    expand = True
                    existing_nodes = []
                    for existing_node in path:
                        if existing_node.islower():
                            if existing_node not in existing_nodes:
                                existing_nodes.append(existing_node)
                            else:
                                expand = False
                                break

            if expand:
                newpaths = self.find_all_paths_part2(graph, node, end, path[:])
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def part2(self):
        graph = self.read_input()
        paths = self.find_all_paths_part2(graph, "start", "end")
        return len(paths)

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day12().execute()
