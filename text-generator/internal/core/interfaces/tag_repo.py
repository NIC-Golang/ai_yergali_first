from abc import ABC, abstractmethod

class TagRepositoryInterface(ABC):
    @abstractmethod
    def save_tags(self, book_id: int, tags: list):
        pass