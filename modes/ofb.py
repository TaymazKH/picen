from aes import aes128
from reader.reader import Reader
from writer.writer import Writer
from util.functions import xor


def encrypt(reader: Reader, writer: Writer, key: str, iv: str):
    previous_output = iv
    round_keys = aes128.key_schedule(key)
    writer.write_next_block(iv)
    while reader.has_unread_block():
        e_block = aes128.run(previous_output, round_keys)
        m_block = reader.get_next_block()
        c_block = xor(e_block, m_block)
        writer.write_next_block(c_block)
        previous_output = e_block

def decrypt(reader: Reader, writer: Writer, key: str):
    pass
