from User import User


class SocialNetwork:
    _instance = None
    listOfUsers = []

    def __new__(cls):
        # If an instance does not exist, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, name):
        self.name = name
    def sign_up(self, username, password):
        user = User(username, password)
        self.listOfUsers.append(user)
