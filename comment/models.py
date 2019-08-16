from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    text = models.TextField(max_length=500)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
