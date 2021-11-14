from django.db import models


# Create your models here.
class Paper_Metadata(models.Model):
    paper_id = models.IntegerField()
    create_time = models.DateTimeField()
    title = models.TextField()
    author = models.TextField()
    abstract = models.TextField()
    venue = models.TextField()
    year = models.IntegerField()
    citations = models.IntegerField()
    url = models.TextField()


class Paper_Comment(models.Model):
    user_id = models.IntegerField()
    create_time = models.DateTimeField()
    paper_id = models.IntegerField()
    commenter_id = models.IntegerField()
    comment = models.TextField()


class Paper_Like_Dislike(models.Model):
    user_id = models.IntegerField()
    create_time = models.DateTimeField()
    paper_id = models.IntegerField()
    like = models.BooleanField()
    dislike = models.BooleanField()