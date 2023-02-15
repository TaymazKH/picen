def _dec_to_bin(num: int):
    bn = bin(num)[2:]
    return '0' * (8 - len(bn)) + bn


def _bin_to_dec(binary_num: str):
    num = 0
    power = 1
    for i in range(8):
        num += int(binary_num[7 - i]) * power
        power *= 2
    return num


def pixel_to_string(pixel, mode):
    if mode == '1':
        return str(pixel)
    elif mode == 'L':
        return _dec_to_bin(pixel)
    elif mode == 'RGB' or mode == 'RGBA':
        output = ''
        for num in pixel:
            output += _dec_to_bin(num)
        return output
    else:
        raise ValueError(f'unsupported image mode: {mode}')
