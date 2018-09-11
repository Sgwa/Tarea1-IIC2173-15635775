from django.db import models
from datetime import datetime


class Comment(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    ip = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __repr__(self):
        return 'Comment: ' + str({'Id': self.id, 'Date': self.date, 'Ip': self.ip, 'Content': self.content})
