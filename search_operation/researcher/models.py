from django.db import models
from common import models as common
from django.core import serializers
import json

# Create your models here.

class Researcher(common.Record):

    username = models.CharField('user nickname', max_length=128, unique=True, null=False)
    password = models.CharField('user password', max_length=512, null=False)
    name = models.CharField('user fullname', max_length=64, null=False)
    title = models.CharField('user title', max_length=64, default='')
    email = models.CharField('user email', max_length=256, unique=True, null=False)
    area = models.JSONField('user research area')


class ResearchTeam(common.Record):

    name = models.CharField('team name', max_length=512, null=False)
    leader_id = models.BigIntegerField('id of the leader', null=False)

    class Meta:
        db_table = Researcher._meta.app_label + '_' + 'research_team'

class TokenPool(common.Record):

    holder_id = models.BigIntegerField('id of the token holder', unique=True, null=False)
    token = models.CharField('token', max_length=2048, null=False)

    class Meta:
        db_table = Researcher._meta.app_label + '_' + 'token_pool'

