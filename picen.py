import click
from baseconv import base2
from modes import *
from reader import *
from writer import *
from util.constants import base16, base64
from util.functions import extend_number, random_binary_string
from util.validators import is_base2_string, is_base16_string, is_base64_string


def encrypt(in_stream, out_stream, key, mode_name):
    if not is_base2_string(key) or len(key) != 128:
        if is_base16_string(key) and len(key) == 32:
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_base64_string(key) and len(key) == 22:
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            click.echo('Invalid key!')
            raise ValueError('Invalid key!')
    reader = ImageReader(in_stream)
    writer = ImageFileWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.encrypt(reader, writer, key)


def decrypt(in_stream, out_stream, key, mode_name):
    if not is_base2_string(key) or len(key) != 128:
        if is_base16_string(key) and len(key) == 32:
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_base64_string(key) and len(key) == 22:
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            click.echo('Invalid key!')
            raise ValueError('Invalid key!')
    reader = ImageFileReader(in_stream)
    writer = ImageWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.decrypt(reader, writer, key)


def generate_key(base):
    key = random_binary_string()
    if base == '16':
        key = extend_number(base16.encode(base2.decode(key)), 32)
    elif base == '64':
        key = extend_number(base64.encode(base2.decode(key)), 22)
    elif base != '2':
        raise ValueError(f'Base must be either 2, 16, or 64. Not {base}')
    return key


def _get_mode(name: str):
    return {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)


if __name__ == '__main__':
    click.secho("Welcome to picen!", fg='green', bold=True, italic=True)
    click.echo("This is the main module.")
    click.echo("From here you can import and call '", nl=False)
    click.secho("encrypt", fg='yellow', nl=False)
    click.echo("', '", nl=False)
    click.secho("decrypt", fg='yellow', nl=False)
    click.echo("' and '", nl=False)
    click.secho("generate_key", fg='yellow', nl=False)
    click.echo("' functions.")
    click.echo("If you want to use picen as a stand-alone application, run '", nl=False)
    click.secho("python picen_cli.py", fg='yellow', nl=False)
    click.echo("'.")
