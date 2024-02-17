from User import User


class SocialNetwork:
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     # If an instance does not exist, create one
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         if args or kwargs:  # Check if arguments are provided
    #             cls._instance.__init__(*args, **kwargs)  # Call __init__ with arguments
    #     return cls._instance
    def __new__(cls, *args, **kwargs):
        # If an instance does not exist, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'name'):  # Check if instance is already initialized
            self.name = name
            self.listOfUsers = []
            print(f"The social network {self.name} was created!")

    def sign_up(self, username, password):
        if(len(self.listOfUsers) != 0):
            for user in self.listOfUsers:
                if user._username == username:
                    raise ValueError("Username is already taken")
        if len(password) > 8 or len(password) < 4:
            raise ValueError("Password not valid")
        else:
            new_user = User(username, password)
            self.listOfUsers.append(new_user)
            return new_user

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
