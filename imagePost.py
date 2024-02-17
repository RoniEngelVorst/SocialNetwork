from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class imagePost(Post):
    def __init__(self, user, postImage):
        self._postImage = postImage
        self._user = user

    def display(self):
        # image = mpimg.imread(imagePost)
        # plt.imshow(image)
        # plt.axis('off')  # Turn off axis
        # plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self._user.username()} posted a picture\n"