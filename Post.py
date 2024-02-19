from abc import ABC, abstractmethod
class Post(ABC):
    _likes = []
    _likes_counter = 0
    _comment = []

    def __init__(self, user):
        self._user = user

    def like(self, user):
        if self._user != user and user not in self._likes:
            # self._likes.append(user)
            # self._likes_counter = self._likes_counter+1
            self._user.listOfNotifications.append(f"{user.username()} liked your post")
            print(f"notification to {self._user.username()}: {user.username()} liked your post")



    def comment(self, user, content):
        # new_comment = Comment(user, content)
        # self._comment.append(new_comment)
        self._user.listOfNotifications.append(f"{user.username()} commented on your post")
        print(f"notification to {self._user.username()}: {user.username()} commented on your post: {content}")



class Comment():
    def __init__(self, user, content):
        self._user = user
        self._content = content

    def __str__(self):
        return f"{self._user} published a post:\n{self._content}"
