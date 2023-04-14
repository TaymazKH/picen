import click
from .picen import encrypt, decrypt, generate_key
from .util.exceptions import PicenException

context_settings = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=context_settings)
@click.version_option(version='0.2')
def cli():
    pass


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True), metavar='<in_stream>')
@click.argument('out_stream', type=click.Path(), metavar='<out_stream>')
@click.option('-k', '--key', required=True, type=str, prompt='Enter key', metavar='STRING',
              help='The key used for encryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
@click.option('-q', '--quiet', is_flag=True, default=False, show_default=True,
              help='Only print short feedback messages.')
def enc(in_stream, out_stream, key, mode_name, quiet):
    """
    Encrypts an image to a text file.

    \b
    <in_stream> is the path to the image that you want to encrypt.
    <out_stream> is the path in which the encrypted text will be stored.
    """
    try:
        encrypt(in_stream, out_stream, key, mode_name)
        click.secho('Done!', fg='green')
    except PicenException as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An unknown exception occurred:\n{e}', fg='red')


@cli.command()
@click.argument('in_stream', type=click.Path(exists=True), metavar='<in_stream>')
@click.argument('out_stream', type=click.Path(), metavar='<out_stream>')
@click.option('-k', '--key', required=True, type=str, prompt='Enter key', metavar='STRING',
              help='The key used for decryption. Must be 128 / 32 / 22 digits long for bases 2 / 16 / 64 respectively.')
@click.option('-m', '--mode', 'mode_name', default='ofb', show_default=True,
              type=click.Choice(['ofb', 'ctr'], case_sensitive=False), help='Block cipher mode used for encryption.')
@click.option('-q', '--quiet', is_flag=True, default=False, show_default=True,
              help='Only print short feedback messages.')
def dec(in_stream, out_stream, key, mode_name, quiet):
    """
    Decrypts a text file to an image.

    \b
    <in_stream> is the path to the encrypted text.
    <out_stream> is the path in which the decrypted image will be stored.
    """
    try:
        decrypt(in_stream, out_stream, key, mode_name)
        click.secho('Done!', fg='green')
    except PicenException as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An unknown exception occurred:\n{e}', fg='red')


@cli.command()
@click.option('-b', '--base', default='16', type=click.Choice(['2', '16', '64']),
              help='Number base in which the key is outputted.')
@click.option('-q', '--quiet', is_flag=True, default=False, show_default=True,
              help='Only print short feedback messages.')
def gen(base, quiet):
    """
    Generates a key to be used in encryption and decryption.
    """
    try:
        key = generate_key(base)
        click.echo(f'Generated random key in base {base}:')
        click.secho(key, fg='cyan')
    except PicenException as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An exception occurred:\n{e}', fg='red')
    except Exception as e:
        click.secho('Failed!', fg='red')
        if not quiet:
            click.secho(f'An unknown exception occurred:\n{e}', fg='red')


if __name__ == '__main__':
    cli()
