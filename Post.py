from abc import ABC, abstractmethod
class Post(ABC):
    _likes = []
    _likes_counter = 0
    _comment = []

    def __init__(self):
        pass

    def like(self, user):
        self._likes.append(user)
        self._likes_counter = self._likes_counter+1

    def comment(self, user, content):
        new_comment = Comment(user, content)
        self._comment.append(new_comment)



class Comment():
    def __init__(self, user, content):
        self._user = user
        self._content = content
