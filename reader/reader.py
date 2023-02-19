from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def has_unread_block(self):
        pass

    @abstractmethod
    def get_next_block(self):
        pass
