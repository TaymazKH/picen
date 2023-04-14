from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_next_block(self, block: str):
        pass

    @abstractmethod
    def write_entry(self, init):
        pass

    @abstractmethod
    def write_end(self, end):
        pass
