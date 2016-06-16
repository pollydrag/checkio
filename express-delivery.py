import itertools

ACTIONS = {(0, -1): 'L', (0, 1): 'R', (-1, 0): 'U', (1, 0): 'D', (0, 0): 'B'}


def bfs(field_map, start, goal):
    queue = [(start, [start])]
    while queue:
        (field, path) = queue.pop(0)
        neighbors = [(field[0] + x[0], field[1] + x[1]) for x in ACTIONS.keys() if x != (0, 0)]
        neighbors = list(filter(
            lambda x: 0 <= x[0] < len(field_map) and 0 <= x[1] < len(field_map[x[0]]) and field_map[x[0]][x[1]] != 'W',
            neighbors
        ))
        for next in set(neighbors) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(field_map, start, goal):
    return next(bfs(field_map, start, goal))


def search_poi(field_map, poi):
    for i in range(len(field_map)):
        for j in range(len(field_map[i])):
            if field_map[i][j] == poi:
                yield i, j


def checkio(field_map):
    s = next(search_poi(field_map, 'S'))
    e = next(search_poi(field_map, 'E'))
    boxes = list(search_poi(field_map, 'B'))

    paths = [shortest_path(field_map, s, e)]

    for pair_box in itertools.permutations(boxes, 2):
        paths += [
            shortest_path(field_map, s, pair_box[0]) + ['B'] +
            shortest_path(field_map, pair_box[0], pair_box[1])[1:] + ['B'] +
            shortest_path(field_map, pair_box[1], e)[1:]
        ]

    path = min(
        paths,
        key=lambda x: len(x[1:]) * 2 if 'B' not in x else len(x[1:]) + x[1:].index('B') + x[1:][::-1].index('B')
    )

    # build string path
    r = ''
    pstep = None
    for step in path:
        if isinstance(step, str):
            r += step
        else:
            if pstep:
                r += ACTIONS[(step[0] - pstep[0], step[1] - pstep[1])]
            pstep = step

    return r

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing

    def check_solution(func, max_time, field):
        ACTIONS = {
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "D": (1, 0),
            "B": (0, 0)
        }

        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False


    assert check_solution(checkio, 11, ["SB....BE"]), "0st Example"
    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
