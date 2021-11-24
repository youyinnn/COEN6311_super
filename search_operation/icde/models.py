from django.db import models
from common import models as common
from common.project_const import const

# Create your models here.

class IcdeRecord(common.Record):

    user_id = models.BigIntegerField('id of the user', null=False)
    paper_id = models.CharField("external paper id", max_length=1024, null=False)
    team_id = models.BigIntegerField('id of the team', null=True)
    team_name = models.CharField('name of the team', max_length=1024, null=True)
    input_text = models.CharField('operation input text', max_length=32768, null=False)
    operation_type = models.CharField('the type of the operation', max_length=64, null=False)
    paper_title = models.CharField("name of the paper", max_length=1024, null=False)

    class Meta:
        db_table = 'icde' + '_' + 'icde_record'

def paper_search_record(user_id, search_term):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_SEARCH,
        input_text = search_term
    )

def paper_detail_click_record(user_id, paper_id, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_DETAIL_CLICK,
        paper_id = paper_id,
        paper_title = paper_title
    )

def paper_origin_click_record(user_id, paper_id, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_ORIGIN_CLICK,
        paper_id = paper_id,
        paper_title = paper_title,
    )

def paper_like_click_record(user_id, paper_id, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_LIKE_CLICK,
        paper_id = paper_id,
        paper_title = paper_title,
    )
    
def paper_dislike_click_record(user_id, paper_id, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_DISLIKE_CLICK,
        paper_id = paper_id,
        paper_title = paper_title,
    )

def paper_share_click_record(user_id, paper_id, team_id, team_name, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_SHARE,
        paper_id = paper_id,
        paper_title = paper_title,
        team_id = team_id,
        team_name = team_name,
    )

def paper_comment_record(user_id, paper_id, paper_title):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_COMMENT,
        paper_id = paper_id,
        paper_title = paper_title,
    )

def query_to_list(query):
    list = []
    for record in query:
        list.append({
            'id' : record.id,
            'create_time': int(round(record.create_time.timestamp() * 1000)),
            'user_id': record.user_id,
            'paper_id': record.paper_id,
            'paper_title': record.paper_title,
            'team_id': record.team_id,
            'team_name': record.team_name,
            'operation_type': record.operation_type,
            'input_text': record.input_text
        })
    return list
