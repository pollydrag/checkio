def create_graph(network):
    graph = {}
    for link in network:
        n1, n2 = tuple(link.split('-'))

        graph[n1] = graph.get(n1, [])
        graph[n2] = graph.get(n2, [])

        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


def check_connection(network, first, second):
    graph = create_graph(network)
    visited = set()

    def walk(item):
        visited.add(item)
        for link in graph[item]:
            if link not in visited:
                walk(link)

    walk(first)

    return second in visited


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
