from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class imagePost(Post):
    def __init__(self, postType, postImage):
        self._postImage = postImage

    def display(self):
        image = mpimg.imread(imagePost)
        plt.imshow(image)
        plt.axis('off')  # Turn off axis
        plt.show()