def run(block: str):
    pass


def generate_matrix(block: str):
    matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(block[32 * i + 8 * j: 32 * i + 8 * j + 8])
        matrix.append(row)
    return matrix


def sub_bytes(matrix: list):
    pass


def shift_rows(matrix: list):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i].append(matrix[i].pop(0))


def mix_columns(matrix: list):
    pass


def add_round_key(matrix: list):
    pass
