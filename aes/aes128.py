from baseconv import base2
from util.functions import extend_number, xor, nested_list_to_string


def run(block: str, round_keys: list, iter_count: int = 10):
    matrix = generate_matrix(block)
    add_round_key(matrix, round_keys[0])
    for i in range(iter_count - 1):
        _inner_iteration(matrix, round_keys[i + 1])
    sub_bytes(matrix)
    shift_rows(matrix)
    add_round_key(matrix, round_keys[iter_count])
    return nested_list_to_string(matrix)


def _inner_iteration(matrix: list, round_key: list):
    sub_bytes(matrix)
    shift_rows(matrix)
    mix_columns(matrix)
    add_round_key(matrix, round_key)


def key_schedule(main_key: str, iter_count: int = 10):
    keys = [generate_matrix(main_key)]
    last_key = [main_key[:32], main_key[32:64], main_key[64:96], main_key[96:]]
    for i in range(iter_count):
        # calculate the modified last 32-bit word by shifting, subtracting and xor-ing with r_i
        last_word = [last_key[3][8:16], last_key[3][16:24], last_key[3][24:], last_key[3][:8]]
        for j in range(4):
            last_word[j] = _get_from_s_box(last_word[j])
        last_word[0] = xor(last_word[0], extend_number(base2.encode(2 ** i), 8))
        # start calculation of the round key
        new_key = [xor(last_key[0], nested_list_to_string(last_word))]
        for j in range(3):
            new_key.append(xor(last_key[j + 1], new_key[j]))
        # add the round key to the list of keys and prepare for next iteration
        keys.append(generate_matrix(nested_list_to_string(new_key)))
        last_key = new_key
    return keys


def generate_matrix(block: str):
    matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(block[32 * i + 8 * j: 32 * i + 8 * j + 8])
        matrix.append(row)
    return matrix


def sub_bytes(matrix: list):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = _get_from_s_box(matrix[i][j])


def shift_rows(matrix: list):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i].append(matrix[i].pop(0))


def mix_columns(matrix: list):
    new_matrix = []
    for i in range(4):
        new_matrix.append([None] * 4)
    for i in range(4):
        for j in range(4):
            ans = 0
            for k in range(4):
                ans += m_matrix[i][k] * int(base2.decode(matrix[k][j]))
            new_matrix[i][j] = extend_number(base2.encode(ans % 256), 8)
    for i in range(4):
        matrix[i] = new_matrix[i]


def add_round_key(matrix: list, round_key: list):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = xor(matrix[i][j], round_key[i][j])


def _get_from_s_box(byte: str):
    return s_box[
        int(base2.decode(byte[0:4]))
    ][
        int(base2.decode(byte[4:8]))
    ]


s_box = [
    ['01100011', '01111100', '01110111', '01111011', '11110010', '01101011', '01101111', '11000101', '00110000',
     '00000001', '01100111', '00101011', '11111110', '11010111', '10101011', '01110110'],
    ['11001010', '10000010', '11001001', '01111101', '11111010', '01011001', '01000111', '11110000', '10101101',
     '11010100', '10100010', '10101111', '10011100', '10100100', '01110010', '11000000'],
    ['10110111', '11111101', '10010011', '00100110', '00110110', '00111111', '11110111', '11001100', '00110100',
     '10100101', '11100101', '11110001', '01110001', '11011000', '00110001', '00010101'],
    ['00000100', '11000111', '00100011', '11000011', '00011000', '10010110', '00000101', '10011010', '00000111',
     '00010010', '10000000', '11100010', '11101011', '00100111', '10110010', '01110101'],
    ['00001001', '10000011', '00101100', '00011010', '00011011', '01101110', '01011010', '10100000', '01010010',
     '00111011', '11010110', '10110011', '00101001', '11100011', '00101111', '10000100'],
    ['01010011', '11010001', '00000000', '11101101', '00100000', '11111100', '10110001', '01011011', '01101010',
     '11001011', '10111110', '00111001', '01001010', '01001100', '01011000', '11001111'],
    ['11010000', '11101111', '10101010', '11111011', '01000011', '01001101', '00110011', '10000101', '01000101',
     '11111001', '00000010', '01111111', '01010000', '00111100', '10011111', '10101000'],
    ['01010001', '10100011', '01000000', '10001111', '10010010', '10011101', '00111000', '11110101', '10111100',
     '10110110', '11011010', '00100001', '00010000', '11111111', '11110011', '11010010'],
    ['11001101', '00001100', '00010011', '11101100', '01011111', '10010111', '01000100', '00010111', '11000100',
     '10100111', '01111110', '00111101', '01100100', '01011101', '00011001', '01110011'],
    ['01100000', '10000001', '01001111', '11011100', '00100010', '00101010', '10010000', '10001000', '01000110',
     '11101110', '10111000', '00010100', '11011110', '01011110', '00001011', '11011011'],
    ['11100000', '00110010', '00111010', '00001010', '01001001', '00000110', '00100100', '01011100', '11000010',
     '11010011', '10101100', '01100010', '10010001', '10010101', '11100100', '01111001'],
    ['11100111', '11001000', '00110111', '01101101', '10001101', '11010101', '01001110', '10101001', '01101100',
     '01010110', '11110100', '11101010', '01100101', '01111010', '10101110', '00001000'],
    ['10111010', '01111000', '00100101', '00101110', '00011100', '10100110', '10110100', '11000110', '11101000',
     '11011101', '01110100', '00011111', '01001011', '10111101', '10001011', '10001010'],
    ['01110000', '00111110', '10110101', '01100110', '01001000', '00000011', '11110110', '00001110', '01100001',
     '00110101', '01010111', '10111001', '10000110', '11000001', '00011101', '10011110'],
    ['11100001', '11111000', '10011000', '00010001', '01101001', '11011001', '10001110', '10010100', '10011011',
     '00011110', '10000111', '11101001', '11001110', '01010101', '00101000', '11011111'],
    ['10001100', '10100001', '10001001', '00001101', '10111111', '11100110', '01000010', '01101000', '01000001',
     '10011001', '00101101', '00001111', '10110000', '01010100', '10111011', '00010110']
]

m_matrix = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]
