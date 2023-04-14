from baseconv import base2
from ..aes import aes128
from ..reader.reader import Reader
from ..writer.writer import Writer
from ..util.functions import xor, random_binary_string


def encrypt(reader: Reader, writer: Writer, key: str):
    iv = random_binary_string()
    counter = int(base2.decode(iv))
    base = int(base2.decode('1' + '0' * 128))
    round_keys = aes128.key_schedule(key)
    writer.write_entry(reader.get_entry())
    writer.write_next_block(iv)
    while reader.has_unread_block():
        counter += 1
        if counter == base:
            counter = 0
        e_block = aes128.run(base2.encode(counter), round_keys)
        m_block = reader.get_next_block()
        c_block = xor(e_block, m_block)
        writer.write_next_block(c_block)
    writer.write_end(reader.get_end())


def decrypt(reader: Reader, writer: Writer, key: str):
    writer.write_entry(reader.get_entry())
    iv = reader.get_next_block()
    counter = int(base2.decode(iv))
    base = int(base2.decode('1' + '0' * 128))
    round_keys = aes128.key_schedule(key)
    while reader.has_unread_block():
        counter += 1
        if counter == base:
            counter = 0
        e_block = aes128.run(base2.encode(counter), round_keys)
        c_block = reader.get_next_block()
        m_block = xor(e_block, c_block)
        writer.write_next_block(m_block)
    writer.write_end(reader.get_end())
