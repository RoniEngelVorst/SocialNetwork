from Post import Post


class textPost(Post):
    def __init__(self, postType, postContent):
        self._postContent = postContent