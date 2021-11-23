from django.db import models
from common import models as common
from common.project_const import const

# Create your models here.

class IcdeRecord(common.Record):

    user_id = models.BigIntegerField('id of the user', unique=True, null=False)
    paper_id = models.BigIntegerField('id of the paper', unique=True, null=True)
    input_text = models.CharField('operation input text', max_length=32768, null=False)
    operation_type = models.CharField('the type of the operation', max_length=64, null=False)

    class Meta:
        db_table = 'icde' + '_' + 'icde_record'

def paper_search_record(user_id, search_term):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_SEARCH,
        input_text = search_term
    )

def paper_detail_click_record(user_id, paper_id):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_DETAIL_CLICK,
        paper_id = paper_id
    )

def paper_origin_click_record(user_id, paper_id):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_ORIGIN_CLICK,
        paper_id = paper_id
    )

def paper_like_click_record(user_id, paper_id):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_LIKE_CLICK,
        paper_id = paper_id
    )
    
def paper_dislike_click_record(user_id, paper_id):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_DISLIKE_CLICK,
        paper_id = paper_id
    )

def paper_share_click_record(user_id, paper_id):
    IcdeRecord.objects.create(
        user_id = user_id,
        operation_type =  const.PAPER_SHARE,
        paper_id = paper_id
    )

