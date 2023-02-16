from baseconv import base2


def _extend_number(str_num: str, digit_count: int):
    return '0' * (digit_count - len(str_num)) + str_num


def pixel_to_string(pixel, mode):
    if mode == '1':
        return str(pixel)
    elif mode == 'L':
        return _extend_number(base2.encode(pixel), 8)
    elif mode == 'RGB' or mode == 'RGBA':
        output = ''
        for num in pixel:
            output += _extend_number(base2.encode(num), 8)
        return output
    else:
        raise ValueError(f'unsupported image mode: {mode}')
