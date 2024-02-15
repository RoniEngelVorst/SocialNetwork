from PostFactory import PostFactory


class User:
    def __init__(self, username,password):
        self._username = username
        self._password = password
        self._followers = []
        self._posts = []
    def follow(self, userToFollow):
        userToFollow._followers.append(self)
    def publish_post(self, PostType, PostContent):
        new_post = PostFactory.create_post(PostType.PostType, PostContent)
        self._posts.append(new_post)