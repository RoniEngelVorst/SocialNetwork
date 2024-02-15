from abc import ABC, abstractmethod
class Post(ABC):
    def __init__(self, postContent):
        self._postContent = postContent