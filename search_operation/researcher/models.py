from django.db import models
from common import models as common
from .apps import ResearcherConfig
import json

# Create your models here.

class Researcher(common.Record):

    username = models.CharField('user nickname', max_length=128, unique=True, null=False)
    password = models.CharField('user password', max_length=512, null=False)
    name = models.CharField('user fullname', max_length=64, null=False)
    email = models.CharField('user email', max_length=256, unique=True, null=False)
    area = models.JSONField('user research area')

    def __str__(self):
        return json.dumps(self)

class ResearchTeam(common.Record):

    name = models.CharField('team name', max_length=512, null=False)
    leaderId = models.BigIntegerField('id of the leader', null=False)

    def __str__(self):
        return json.dumps(self)

    class Meta:
        db_table = Researcher._meta.app_label + '_' + 'research_team'

