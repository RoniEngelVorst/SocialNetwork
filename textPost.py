from Post import Post


class textPost(Post):
    def __init__(self, user, postContent):
        self._postContent = postContent
        self._user = user
    def __str__(self):
        return f"{self._user.username()} published a post\n{self._postContent}\n"