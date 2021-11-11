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
