import click
from baseconv import base2
from .modes import *
from .reader import *
from .writer import *
from .util.constants import base16, base64
from .util.exceptions import InvalidKeyValueException, InvalidBCModeException, InvalidValueException
from .util.functions import extend_number, random_binary_string
from .util.validators import is_length128_base2_string, is_length32_base16_string, is_length22_base64_string


def encrypt(in_stream, out_stream, key: str, mode_name: str = 'ofb'):
    """
    Encrypts an image to a text file.

    Args:
        in_stream: Path to the image that you want to encrypt.
        out_stream: Path in which the encrypted text will be stored.
        key: The key that will be used in encryption.
          It can be 128 digits (base 2), 32 digits (base 16) or 22 digits (base 64).
        mode_name: Block cipher encryption mode.
          It can be either ofb or ctr. Default is ofb.
    """
    if not is_length128_base2_string(key):
        if is_length32_base16_string(key):
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_length22_base64_string(key):
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            raise InvalidKeyValueException(key)
    mode = _get_mode(mode_name)
    reader = ImageReader(in_stream)
    writer = ImageFileWriter(out_stream)
    mode.encrypt(reader, writer, key)


def decrypt(in_stream, out_stream, key: str, mode_name: str = 'ofb'):
    """
        Decrypts a text file to an image.

        Args:
            in_stream: Path to the encrypted text.
            out_stream: Path in which the decrypted image will be stored.
            key: The key that will be used in encryption.
              It can be 128 digits (base 2), 32 digits (base 16) or 22 digits (base 64).
            mode_name: Block cipher encryption mode.
              It can be either ofb or ctr. Default is ofb.
        """
    if not is_length128_base2_string(key):
        if is_length32_base16_string(key):
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_length22_base64_string(key):
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            raise InvalidKeyValueException(key)
    mode = _get_mode(mode_name)
    reader = ImageFileReader(in_stream)
    writer = ImageWriter(out_stream)
    mode.decrypt(reader, writer, key)


def generate_key(base='16'):
    """
    Generates a key to be used in encryption and decryption.

    Args:
        base: The number base in which the key is outputted.
          It can be 2 (128 digits), 16 (32 digits) or 64 (22 digits).
          Default is 16.
    """
    key = random_binary_string()
    base = str(base)
    if base == '16':
        key = extend_number(base16.encode(base2.decode(key)), 32)
    elif base == '64':
        key = extend_number(base64.encode(base2.decode(key)), 22)
    elif base != '2':
        raise InvalidValueException(['base'], [base], 'Base must be either 2, 16, or 64.')
    return key


def _get_mode(name: str):
    mode = {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)
    if mode is None:
        raise InvalidBCModeException(name)
    return mode


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
