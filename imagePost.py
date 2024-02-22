from Post import Post
import matplotlib.pyplot as plt



class imagePost(Post):
    def __init__(self, user, postImage):
        super().__init__(user)
        self._postImage = postImage

    def display(self):
        image_rgb = plt.imread(self._postImage)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self._user.username()} posted a picture\n"