import sys

def flush():
    sys.stdout.flush()

def query(start, s):
    print(f"? {start} {len(s)} {' '.join(map(str, s))}")
    flush()
    resp = input()
    if resp == "-1":
        exit(0)
    return int(resp)

def solve_portals(n):
    todos = list(range(1, n+1))

    max_len = -1
    start_node = 1
    for i in todos:
        resp = query(i, todos)
        if resp > max_len:
            max_len = resp
            start_node = i

    path = [start_node]
    candidates = set(todos) - {start_node}

    while len(path) < max_len:
        found = False
        for portal in list(candidates):
            resp = query(start_node, path + [portal])
            if resp == len(path) + 1:
                path.append(portal)
                candidates.remove(portal)
                found = True
                break
        if not found:
            portal = candidates.pop()
            path.append(portal)

    print(f"! {len(path)} {' '.join(map(str, path))}")
    flush()

t = int(input())
for _ in range(t):
    n = int(input())
    solve_portals(n)
