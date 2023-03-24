import click
from picen import encrypt, decrypt, generate_key
from util.exceptions import PicenException

context_settings = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=context_settings)
@click.version_option(version='0')
def cli():
    pass


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', required=True, type=str, prompt='Enter key',
              help='The key used for encryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
def enc(in_stream, out_stream, key, mode_name):
    try:
        encrypt(in_stream, out_stream, key, mode_name)
        click.secho('Done!', fg='green')
    except PicenException as e:
        click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho(f'An unknown exception occurred:\n{e}', fg='red')


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True))
@click.argument('out_stream', type=click.Path())
@click.option('-k', '--key', required=True, type=str, prompt='Enter key',
              help='The key used for decryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
def dec(in_stream, out_stream, key, mode_name):
    try:
        decrypt(in_stream, out_stream, key, mode_name)
        click.secho('Done!', fg='green')
    except PicenException as e:
        click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho(f'An unknown exception occurred:\n{e}', fg='red')


@cli.command()
@click.option('-b', '--base', default='16', type=click.Choice(['2', '16', '64']))
def gen(base):
    try:
        click.echo(f'Generated random key in base {base}:\n{generate_key(base)}')
    except PicenException as e:
        click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho(f'An unknown exception occurred:\n{e}', fg='red')


if __name__ == '__main__':
    cli()
