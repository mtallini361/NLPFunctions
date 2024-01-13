from functions.similarity import minimal_edit_distance


minimal_edit_matrix = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 6, 7, 8],
    [2, 3, 4, 5, 6, 7, 8, 7, 8, 7],
    [3, 4, 5, 6, 7, 8, 7, 8, 9, 8],
    [4, 3, 4, 5, 6, 7, 8, 9, 10, 9],
    [5, 4, 5, 6, 7, 8, 9, 10, 11, 10],
    [6, 5, 6, 7, 8, 9, 8, 9, 10, 11],
    [7, 6, 7, 8, 9, 10, 9, 8, 9, 10],
    [8, 7, 8, 9, 10, 11, 10, 9, 8, 9],
    [9, 8, 9, 10, 11, 12, 11, 10, 9, 8]
]


def test_minimal_edit_distance(string1, string2):
    result = minimal_edit_distance(string1, string2)

    assert len(minimal_edit_matrix) == len(result)
    for i in range(len(minimal_edit_matrix)):
        assert len(minimal_edit_matrix[i]) == len(result[i])

    for i in range(len(minimal_edit_matrix)):
        for j in range(len(minimal_edit_matrix[i])):
            assert minimal_edit_matrix[i][j] == result[i][j]