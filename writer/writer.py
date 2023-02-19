from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_next_block(self, block: str):
        pass
