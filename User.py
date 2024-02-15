from PostFactory import PostFactory


class User:
    def __init__(self, username,password):
        self._username = username
        self._password = password
        self._followers = []
        self._posts = []
        self._active = True
    def follow(self, userToFollow):
        if(userToFollow in self._followers):
            pass
        else:
            userToFollow._followers.append(self)

    def unfollow(self, userToStopFollowing):
        if(self in userToStopFollowing._followers):
            userToStopFollowing._followers.remove(self)

    def publish_post(self, PostType, PostContent):
        new_post = PostFactory.create_post(PostType.PostType)
        self._posts.append(new_post)

    def update(self):
        pass