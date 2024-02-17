from PostFactory import PostFactory
from SocialNetwork import SocialNetwork


class User:
    def __init__(self, username,password):
        self._username = username
        self._password = password
        self._followers = []
        self._posts = []
        self._active = True
    def follow(self, userToFollow):
        if self._active == True:
            if(userToFollow in self._followers):
                pass
            else:
                userToFollow._followers.append(self)
                print(f"{self._username} started following {userToFollow._username}")

    def unfollow(self, userToStopFollowing):
        if self._active == True:
            if(self in userToStopFollowing._followers):
                userToStopFollowing._followers.remove(self)
                print(f"{self._username} unfollowed {userToStopFollowing._username}")

    def publish_post(self, PostType, PostContent):
        if self._active == True:
            new_post = PostFactory.create_post(PostType.PostType)
            self._posts.append(new_post)
            print(str(self._posts[-1]))

    def update(self):
        pass

    def notifyFollowerActivity(self):
        pass

    def notifyOnMyPosts(self):
        pass

    def __str__(self):
        return f"User name: {self._username}, Number of posts: {len(self._posts)}, Number of followers: {len(self._followers)}"

    def printAllNotifications(self):
        pass