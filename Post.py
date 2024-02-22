from abc import ABC, abstractmethod
class Post(ABC):
    _likes = []


    def __init__(self, user):
        self._user = user

    def like(self, user):
        #checking that a user does not do like to itself and that there is no double like
        if self._user != user and user not in self._likes:
            #adding the notification to the user who posted the post that someone liked its post
            self._user.listOfNotifications.append(f"{user.username()} liked your post")
            #printing the notification to all the network
            print(f"notification to {self._user.username()}: {user.username()} liked your post")



    def comment(self, user, content):
        #adding notification and printing
        self._user.listOfNotifications.append(f"{user.username()} commented on your post")
        print(f"notification to {self._user.username()}: {user.username()} commented on your post: {content}")

