from django.db import models
from common import models as common

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


class Paper_Comment(common.Record):
    # user_id = models.IntegerField()
    # create_time = models.DateTimeField()
    paper_id = models.CharField("external paper id", max_length=1024, null=True)
    commenter_id = models.IntegerField()
    commenter_name = models.CharField('user fullname', max_length=64, null=True)
    commenter_email = models.CharField('user email', max_length=256, null=True)
    comment = models.TextField()

class Paper_Like_Dislike(common.Record):
    user_id = models.IntegerField()
    # create_time = models.DateTimeField()
    paper_id = models.CharField("external paper id", max_length=1024, null=True)
    like = models.BooleanField()
    # dislike = models.BooleanField()