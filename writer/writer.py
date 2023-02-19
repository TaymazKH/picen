from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_next_block(self, block: str):
        pass

    @abstractmethod
    def write_init(self, init: str):
        pass

    @abstractmethod
    def write_end(self, end: str):
        pass
