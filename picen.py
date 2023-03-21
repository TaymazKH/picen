import click
from baseconv import base2
from modes import *
from reader import *
from writer import *
from util.constants import base16, base64
from util.functions import extend_number, random_binary_string
from util.validators import is_base2_string, is_base16_string, is_base64_string

context_settings = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=context_settings)
@click.version_option(version='0')
def cli():
    pass


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', required=True, type=str,
              help='The key used for encryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
def enc(in_stream, out_stream, key, mode_name):
    if not is_base2_string(key) or len(key) != 128:
        if is_base16_string(key) and len(key) == 32:
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_base64_string(key) and len(key) == 22:
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            click.echo('Invalid key!')
            raise click.Abort()
    reader = ImageReader(in_stream)
    writer = ImageFileWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.encrypt(reader, writer, key)


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', required=True, type=str,
              help='The key used for decryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
def dec(in_stream, out_stream, key, mode_name):
    if not is_base2_string(key) or len(key) != 128:
        if is_base16_string(key) and len(key) == 32:
            key = extend_number(base2.encode(base16.decode(key)), 128)
        elif is_base64_string(key) and len(key) == 22:
            key = extend_number(base2.encode(base64.decode(key)), 128)
        else:
            click.echo('Invalid key!')
            raise click.Abort()
    reader = ImageFileReader(in_stream)
    writer = ImageWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.decrypt(reader, writer, key)


@cli.command()
@click.option('-b', '--base', default='16', type=click.Choice(['2', '16', '64']))
def gen(base):
    key = random_binary_string()
    if base == '16':
        key = extend_number(base16.encode(base2.decode(key)), 32)
    elif base == '64':
        key = extend_number(base64.encode(base2.decode(key)), 22)
    click.echo(f'Generated random key in base {base}:\n{key}')


def _get_mode(name: str):
    return {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)


if __name__ == '__main__':
    cli()
