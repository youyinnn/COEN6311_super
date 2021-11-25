from common.http_response import json_response_builder as response
from icde import models as ICDE

from common.jwt import get_user_id as get_id_from_request
from common.jwt import auth_require

from common.project_const import const
from icde.models import IcdeRecord
from icde.capture import icde_capture
from researcher.views import get_team_list_by_state
from researcher.models import ResearchTeamAuth

@auth_require
@icde_capture(const.PAPER_SHARE)
def share_paper(request):
    return response(0)

@icde_capture(const.PAPER_SEARCH)
def search_paper(request):
    return response(0)

@icde_capture(const.PAPER_ORIGIN_CLICK)
def go_paper_origin(request):
    return response(0)

@icde_capture(const.PAPER_DETAIL_CLICK)
def go_paper_detail_page(request):
    return response(0)

@auth_require
def get_paper_team_share_records(request):
    getParams = request.GET.dict()
    user_id = get_id_from_request(request)
    paper_id = getParams.get('paper_id')
    joined_team_list = get_team_list_by_state(user_id, const.JOINED)

    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        operation_type =  const.PAPER_SHARE,
        paper_id = paper_id
    ))

    for team in joined_team_list:
        shared = False
        for icde_record in icde_record_list:
            if icde_record['team_id'] == team['team_id'] and icde_record['user_id'] == user_id:
                shared = True
        team['shared'] = shared

    return response(0, body={
        'total_shared': len(icde_record_list),
        'joined_team_list' : joined_team_list,
        'icde_record_list' : icde_record_list
    })


@auth_require
def get_user_activities(request):
    user_id = get_id_from_request(request)
    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        user_id = user_id
    ))

    # icde_record_list = user_icde_record_filter(icde_record_list)

    icde_record_list.sort(reverse=True, key=lambda record : record['create_time'])
    
    return response(0, body={
        'records': icde_record_list,
    })

# def user_icde_record_filter(records):
#     new_list = []
#     previous_record = None
#     for record in records:
#         if previous_record == None:
#             previous_record = record
#         else:
#             if (record['operation_type'] == const.PAPER_DETAIL_CLICK and previous_record['operation_type'] == const.PAPER_DETAIL_CLICK) and (record['paper_id'] == previous_record['paper_id']):
#                 continue
#         new_list.append(record)
#         previous_record = record

#     return new_list


@auth_require
def get_team_member_activities(request):
    getParams = request.GET.dict()
    team_id = getParams.get('team_id')

    auth_query = ResearchTeamAuth.objects.filter(
        team_id = team_id,
        state = const.JOINED
    ).values()

    team_member_id_list = [auth['researcher_id'] for auth in auth_query]

    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        user_id__in = team_member_id_list
    ))

    icde_record_list.sort(reverse=True, key=lambda record : record['create_time'])

    new_list = []

    def team_icde_record_filter(record, team_id):
        if record['operation_type'] == const.PAPER_SHARE and record['team_id'] != int(team_id):
            return False
        return True

    for record in icde_record_list:
        if team_icde_record_filter(record, team_id):
            new_list.append(record)

    return response(0, body={
        'records': new_list,
    })



from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_search_term_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, input_text from icde_icde_record 
            where operation_type = %s group by input_text order by count desc
            limit 30
        ''', [const.PAPER_SEARCH])
        row = dictfetchall(cursor)
    
    return row

def get_click_rate_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type in (%s, %s) group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_DETAIL_CLICK, const.PAPER_ORIGIN_CLICK])
        row = dictfetchall(cursor)
    
    return row


def get_like_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_LIKE_CLICK])
        row = dictfetchall(cursor)
    
    return row

def get_dislike_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_DISLIKE_CLICK])
        row = dictfetchall(cursor)
    
    return row
    
def get_share_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_SHARE])
        row = dictfetchall(cursor)
    
    return row


def get_all_trending_list(request):

    searh_term_trending = get_search_term_trending_list()
    click_rate_trending = get_click_rate_trending_list()
    like_trending = get_like_trending_list()
    dislike_trending = get_dislike_trending_list()
    share_trending = get_share_trending_list()
    
    return response(0, body={
        'tranding_list': [
            searh_term_trending, 
            click_rate_trending, 
            like_trending, 
            dislike_trending,
            share_trending
        ]
    })