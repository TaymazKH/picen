import click
from modes import *
from reader import *
from writer import *
from util.functions import random_binary_string
from util.validators import is_binary_string


@click.group()
def cli():
    pass


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', default=None, type=str)
@click.option('-m', '--mode', 'mode_name', default='ofb', type=click.Choice(['ofb', 'ctr'], case_sensitive=False))
def enc(in_stream, out_stream, key, mode_name):
    if is_binary_string(key) and len(key) == 128:
        reader = ImageReader(in_stream)
        writer = ImageFileWriter(out_stream)
        mode = _get_mode(mode_name)
        mode.encrypt(reader, writer, key)


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', default=None, type=str)
@click.option('-m', '--mode', 'mode_name', default='ofb', type=click.Choice(['ofb', 'ctr'], case_sensitive=False))
def dec(in_stream, out_stream, key, mode_name):
    if is_binary_string(key) and len(key) == 128:
        reader = ImageFileReader(in_stream)
        writer = ImageWriter(out_stream)
        mode = _get_mode(mode_name)
        mode.decrypt(reader, writer, key)


@cli.command()
def gen():
    key = random_binary_string()
    print(key)


def _get_mode(name: str):
    return {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)
