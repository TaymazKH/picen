from baseconv import base2


def pixel_to_string(pixel, mode):
    if mode == '1':
        return str(pixel)
    elif mode == 'L':
        return extend_number(base2.encode(pixel), 8)
    elif mode == 'RGB' or mode == 'RGBA':
        output = ''
        for num in pixel:
            output += extend_number(base2.encode(num), 8)
        return output
    else:
        raise ValueError(f'unsupported image mode: {mode}')


def string_to_pixel(string):
    pass


def extend_number(str_num: str, digit_count: int):
    return '0' * (digit_count - len(str_num)) + str_num


def xor(str1: str, str2: str):
    output = ''
    for i in range(len(str1)):
        output += '0' if str1[i] == str2[i] else '1'
    return output


def nested_list_to_string(nested_list: list):
    return nested_list.__str__().replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '')
