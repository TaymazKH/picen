# Picen

**Pic**ture **en**cryption and decryption program, written in python.

## Algorithms

This program uses block ciphers to encrypt and decrypt images.<br>
The main algorithms are the OFB and CTR modes.<br>
AES-128 is used as the PRP.

## Setup

Install the package from PyPI:

```shell
$ pip install picen
```

## Usage

Picen can be used in both ways:

- If you want to use it as a package in your own project, just import `encrypt`, `decrypt` and `generate_key`
  functions from `picen`.

- If you want to use it as a stand-alone application, run
  `python -m picen`.

In both cases, the functions'/commands' parameters are mostly the same.

### Encryption

```
encrypt(in_stream, out_stream, key, mode_name)
```

```
python -m picen enc <in_stream> <out_stream> (--key=<str>) [--mode=<str>] [--quiet]
```

- `in_stream` is the path to the image that you want to encrypt.
- `out_stream` is the path in which the encrypted text will be stored.
- `-k` or `--key` is the key that will be used in encryption. It can be 128 digits (base 2), 32 digits (base 16) or 22
  digits (base 64).
- `-m` or `--mode` is the block cipher encryption mode. It can be either `ofb` or `ctr`. Default is `ofb`.
- `-q` or `--quiet` is a flag that indicates to suppress the terminal output. Available only in cli.

### Decryption

```
decrypt(in_stream, out_stream, key, mode_name)
```

```
python -m picen dec <in_stream> <out_stream> (--key=<str>) [--mode=<str>] [--quiet]
```

Mainly same as encryption but:

- `in_stream` is the path to the encrypted text.
- `out_stream` is the path in which the decrypted image will be stored.

### Key Generation

```
generate_key(base)
```

```
python -m picen gen [--base=<str>] [--quiet]
```

- `-b` or `--base` is the number base in which the key is outputted. It can be 2 (128 digits), 16 (32 digits) or 64 (22
  digits). Default is 16.

## Links

- [GitHub](https://github.com/TaymazKH/picen)
- [Trello](https://trello.com/b/7QRmgQuH/picen)
