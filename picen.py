from modes import *
from reader import *
from writer import *
from util.functions import random_binary_string

global_key = None


def enc(in_stream, out_stream, key, mode_name):
    reader = ImageReader(in_stream)
    writer = ImageFileWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.encrypt(reader, writer, key)


def dec(in_stream, out_stream, key, mode_name):
    reader = ImageFileReader(in_stream)
    writer = ImageWriter(out_stream)
    mode = _get_mode(mode_name)
    mode.decrypt(reader, writer, key)


def gen(set_global_key):
    key = random_binary_string()
    if set_global_key:
        global global_key
        global_key = key


def keys():
    pass


def _get_mode(name: str):
    return {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)
