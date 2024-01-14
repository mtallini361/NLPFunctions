def minimal_edit_distance(string1, string2):
    n = len(string1) + 1
    m = len(string2) + 1

    D = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(1, n):
        D[i][0] = D[i - 1][0] + 1

    for j in range(1, m):
        D[0][j] = D[0][j - 1] + 1

    for i in range(1, n):
        for j in range(1, m):
            sub_cost = 0
            if string1[i - 1] != string2[j - 1]:
                sub_cost += 2

            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i - 1][j - 1] + sub_cost,
                D[i][j - 1] + 1
            )

    return D[n][m]
