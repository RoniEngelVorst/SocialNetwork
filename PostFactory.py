from enum import Enum

from imagePost import imagePost
from salePost import salePost
from textPost import textPost


class PostType(Enum):
    TEXT = "Text"
    IMAGE = "Image"
    SALE = "Sale"

class PostFactory:
    def create_post(self, post_type, *args):
        if post_type == PostType.TEXT:
            return textPost(*args)
        elif post_type == PostType.IMAGE:
            return imagePost(*args)
        elif post_type == PostType.SALE:
            return salePost(*args)
        else:
            raise ValueError("Invalid post type")