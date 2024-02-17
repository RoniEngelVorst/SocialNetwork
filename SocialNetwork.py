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
        print(f"The social network {self.name} was created!\n")
    def sign_up(self, username, password):
        for user in self.listOfUsers:
            if user._username == username:
                raise ValueError("Username is already taken")
        if len(password) > 8 or len(password) < 4:
            raise ValueError("Password not valid")
        else:
            user = User(username, password)
            self.listOfUsers.append(user)

    def log_out(self, name):
        for user in self.listOfUsers:
            if user._username == name:
                user._active = False
                print(f"{name} disconnected")

    def log_in(self, name, password):
        for user in self.listOfUsers:
            if user._username == name and user._password == password:
                user._active = True
                print(f"{name} connected")

    def __str__(self):
        s = ""
        for user in self.listOfUsers:
            s = s + str(user) + "\n"
        return s
