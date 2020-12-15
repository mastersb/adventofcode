def main():
    graph = {}
    global_to_visit = set()
    global_visited = set()
    global_contains_color = set()
    global_search_stack = ['shiny gold']

    with open('input.txt', 'r') as f:
        for line in f:
            # print(line, end='')
            partition1 = line.partition(' bags contain ')
            key = partition1[0]
            contains = partition1[2].split(',')
            bags = []
            for bag in contains:
                bag = bag.strip()
                if bag == 'no other bags.':
                    bags.append(None)
                    global_visited.add(key)
                else:
                    bags.append(make_node(bag))
                    global_to_visit.add(key)

            graph[key] = bags

    # Part 1
    while len(global_search_stack) > 0:
        color = global_search_stack.pop()
        global_to_visit = global_to_visit.difference(global_visited)
        for node in global_to_visit:
            if node not in global_visited:
                result = search_neighbors(graph, node, color)
                if result:
                    global_visited.add(node)
                    # global_to_visit.remove(node)
                    global_contains_color.add(node)
                    global_search_stack.append(node)

    # print(global_contains_color)
    print(f'Part 1: {len(global_contains_color)}')

    # Part 2
    bag_total = dfs(graph, 'shiny gold', 1)
    print(f'Part 2: {bag_total - 1}')


def dfs(graph, color, parent_amt):
    # print(color, graph[color], parent_amt)
    neighbor_stack = []
    neighbor_stack.append(parent_amt)
    for neighbor in graph[color]:
        if neighbor:
            name = list(neighbor.keys())[0]
            amount = int(neighbor[name])
            amount *= parent_amt
            neighbor_stack.append(dfs(graph, name, amount))
        else:
            return parent_amt

    return sum(neighbor_stack)


def make_node(bag_info):
    bag_info = bag_info.split(' ')
    bag_name = bag_info[1] + ' ' + bag_info[2]
    return {bag_name: bag_info[0]}


def search_neighbors(graph, node, color):
    for neighbor in graph[node]:
        name = list(neighbor.keys())[0]
        if name == color:
            return True

    return False


def bag_sum(graph, node):
    total = 0
    for bag in graph[node]:
        if bag:
            name = list(bag.keys())[0]
            total += int(bag[name])  # number of these bags inside the node's bag

    return total


if __name__ == '__main__':
    main()
