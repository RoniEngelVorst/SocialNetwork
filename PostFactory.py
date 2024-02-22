from enum import Enum

from imagePost import imagePost
from salePost import salePost
from textPost import textPost


class PostType(Enum):
    TEXT = 'Text'
    IMAGE = 'Image'
    SALE = 'Sale'

class PostFactory:
    #a factory that creates posts
    @staticmethod
    def create_post(post_type, user, *args):
        if post_type == PostType.TEXT:
            return textPost(user, *args)
        elif post_type == PostType.IMAGE:
            return imagePost(user, *args)
        elif post_type == PostType.SALE:
            return salePost(user, *args)
        else:
            raise ValueError("Invalid post type")