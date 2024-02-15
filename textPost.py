from Post import Post


class textPost(Post):
    def __init__(self, postType, postContent, user):
        self._postContent = postContent
        self._user = user
    def __str__(self):
        return f"{self.user._username} published a post\n{self._postContent}"