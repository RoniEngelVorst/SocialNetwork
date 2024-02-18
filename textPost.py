from Post import Post


class textPost(Post):
    def __init__(self, user, postContent):
        super(self, user)
        self._postContent = postContent
    def __str__(self):
        return f"{self._user.username()} published a post\n{self._postContent}\n"