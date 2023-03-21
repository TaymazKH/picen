from modes import *
from util.functions import random_binary_string

global_key = None


def enc(in_stream, out_stream, key, mode):
    pass


def dec(in_stream, out_stream, key):
    pass


def gen(set_global_key):
    pass


def set_global_key():
    pass


def _get_mode(name: str):
    return {
        'ofb': ofb,
        'ctr': ctr
    }.get(name)
