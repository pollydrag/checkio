# Solution for "Radiation search"
# https://checkio.org/mission/radiation-search/

MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(matrix, start):
    area = []
    queue = [start]
    while queue:
        field = queue.pop(0)
        area.append(field)
        neighbors = [(field[0] + x[0], field[1] + x[1]) for x in MOVE]
        neighbors = list(filter(
            lambda x: 0 <= x[0] < len(matrix) and
                      0 <= x[1] < len(matrix[x[0]]) and
                      matrix[x[0]][x[1]] == matrix[start[0]][start[1]],
            neighbors
        ))
        for n in set(neighbors) - set(queue + area):
            queue.append(n)
    return area


def checkio(matrix):
    areas = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in sum(areas, []):
                areas.append(bfs(matrix, (i, j)))

    m = max(areas, key=len)
    return [len(m), matrix[m[0][0]][m[0][1]]]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
