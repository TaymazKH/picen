from baseconv import base2, base16
from util.functions import extend_number, xor


def run(block: str):
    pass


def key_schedule(main_key: str):
    keys = []
    last_key = [main_key[:32], main_key[32:64], main_key[64:96], main_key[96:]]
    for i in range(10):
        # calculate the modified last 32-bit word by shifting, subtracting and xor-ing with r_i
        modified_last_word = [last_key[3][8:16], last_key[3][16:24], last_key[3][24:], last_key[3][:8]]
        for j in range(4):
            modified_last_word[j] = _get_from_s_box(modified_last_word[j])
        modified_last_word[0] = xor(modified_last_word[0], extend_number(2 ** i, 8))
        # start calculation of the round key
        new_key = [xor(last_key[0], modified_last_word[0] + modified_last_word[1] + modified_last_word[2] + modified_last_word[3])]
        for j in range(3):
            new_key.append(xor(last_key[j + 1], new_key[j]))
        # add the round key to the list of keys and prepare for next iteration
        keys.append(new_key[0] + new_key[1] + new_key[2] + new_key[3])
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


def add_round_key(matrix: list):
    pass


def _get_from_s_box(byte: str):
    return base2.encode(base16.decode(
        s_box[
            int(base2.decode(byte[0:4]))
        ][
            int(base2.decode(byte[4:8]))
        ]
    ))


s_box = [
    ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
    ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
    ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
    ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
    ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
    ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
    ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
    ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
    ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
    ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
    ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
    ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
    ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
    ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
    ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
    ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
]

m_matrix = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]
