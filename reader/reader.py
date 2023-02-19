from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def has_unread_block(self) -> bool:
        pass

    @abstractmethod
    def get_next_block(self) -> str:
        pass
