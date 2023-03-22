import click
from picen import encrypt, decrypt, generate_key

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
    encrypt(in_stream, out_stream, key, mode_name)


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', required=True, type=str,
              help='The key used for decryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
def dec(in_stream, out_stream, key, mode_name):
    decrypt(in_stream, out_stream, key, mode_name)


@cli.command()
@click.option('-b', '--base', default='16', type=click.Choice(['2', '16', '64']))
def gen(base):
    generate_key(base)


if __name__ == '__main__':
    cli()
