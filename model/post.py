from datetime import datetime
from model.user import User
import uuid


class Post:

    def __init__(self, id: uuid.UUID, title: str, author: User,  content: str):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        # self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'content': self.content
        }
