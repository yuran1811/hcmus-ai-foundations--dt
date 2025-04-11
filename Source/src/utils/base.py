def in_bounds(r: int, c: int, nrows: int, ncols: int):
    return 0 <= r < nrows and 0 <= c < ncols


def comb(n: int, k: int, lits: list[int]):
    clauses: set[frozenset[int]] = set()
    for state in range(2**n):
        sum = 0
        true_pos = []
        for i in range(n):
            x = (state >> i) & 1
            w = 1 + (i & 1)
            sum += w * x

            if x:
                true_pos.append(i)

        valid = True
        for i in range(0, len(true_pos) - 1):
            if true_pos[i + 1] - true_pos[i] == 1 and true_pos[i] & 1 == 0:
                valid = False
                break

        if valid and sum == k:
            x = ""
            for i in range(n):
                x += str((state >> i) & 1)
            clauses.add(frozenset([lits[_] for _ in true_pos]))

    return [list(x) for x in list(clauses)]
