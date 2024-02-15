from enum import Enum

class PostType(Enum):
    TEXT = "txt"
    IMAGE = "image"
    SALE = "sale"

class PostFactory:
    def create_post(self, post_type):
        if post_type == PostType.TEXT:
            return textPost()
        elif post_type == PostType.IMAGE:
            return imagePost()
        elif post_type == PostType.SALE:
            return salePost()
        else:
            raise ValueError("Invalid post type")