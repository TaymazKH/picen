from ..aes import aes128
from ..reader.reader import Reader
from ..writer.writer import Writer
from ..util.functions import xor, random_binary_string


def encrypt(reader: Reader, writer: Writer, key: str):
    iv = random_binary_string()
    previous_output = iv
    round_keys = aes128.key_schedule(key)
    writer.write_entry(reader.get_entry())
    writer.write_next_block(iv)
    while reader.has_unread_block():
        e_block = aes128.run(previous_output, round_keys)
        m_block = reader.get_next_block()
        c_block = xor(e_block, m_block)
        writer.write_next_block(c_block)
        previous_output = e_block
    writer.write_end(reader.get_end())


def decrypt(reader: Reader, writer: Writer, key: str):
    writer.write_entry(reader.get_entry())
    previous_output = reader.get_next_block()
    round_keys = aes128.key_schedule(key)
    while reader.has_unread_block():
        e_block = aes128.run(previous_output, round_keys)
        c_block = reader.get_next_block()
        m_block = xor(e_block, c_block)
        writer.write_next_block(m_block)
        previous_output = e_block
    writer.write_end(reader.get_end())
