from Observer import Sender
from PostFactory import PostFactory, PostType


class User:
    def __init__(self,username, password):
        self._username = username
        self._password = password
        self._followers = []
        self._posts = []
        self._active = True
        self.sender = Sender()
        self.listOfNotifications = []

    def username(self):
        return self._username
    def password(self):
        return self._password
    def follow(self, userToFollow):
        if self._active == True:
            if(self in userToFollow._followers):
                pass
            else:
                userToFollow._followers.append(self)
                userToFollow.sender.register(self)
                print(f"{self._username} started following {userToFollow._username}")

    def unfollow(self, userToStopFollowing):
        if self._active == True:
            if(self in userToStopFollowing._followers):
                userToStopFollowing._followers.remove(self)
                userToStopFollowing.sender.unregister(self)
                print(f"{self._username} unfollowed {userToStopFollowing._username}")

    def publish_post(self, post_type, *args):
        if self._active == True:
            if(post_type == "Text"):
                new_post = PostFactory.create_post(PostType.TEXT, self,*args)
                self._posts.append(new_post)
            if(post_type == "Image"):
                new_post = PostFactory.create_post(PostType.IMAGE, self,*args)
                self._posts.append(new_post)
            if(post_type == "Sale"):
                new_post = PostFactory.create_post(PostType.SALE, self, *args)
                self._posts.append(new_post)
        print(str(self._posts[-1]))
        self.sender.notify(f"{self._username} has a new post")
        return self._posts[-1]

    def update(self, content):
        self.listOfNotifications.append(content)



    def __str__(self):
        return f"User name: {self._username}, Number of posts: {len(self._posts)}, Number of followers: {len(self._followers)}"

    def print_notifications(self):
        print(f"{self._username}'s notifications:")
        for item in self.listOfNotifications:
            print(item)