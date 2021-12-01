from researcher.team_service import get_team_list_by_state
from common.project_const import const
from icde import models as ICDE
from icde.models import IcdeRecord
from researcher.models import ResearchTeamAuth
from django.db import connection

def access_paper_share_count(paper_id): 
    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        operation_type =  const.PAPER_SHARE,
        paper_id = paper_id
    ))

    return {
        'total_shared': len(icde_record_list),
    }

def access_paper_team_share_records(user_id, paper_id):
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

    return {
        'joined_team_list' : joined_team_list,
        'icde_record_list' : icde_record_list
    }

def access_user_activities(user_id):
    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        user_id = user_id
    ))

    icde_record_list.sort(reverse=True, key=lambda record : record['create_time'])
    
    return {
        'records': icde_record_list,
    }

def access_team_member_activities(team_id):

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

    return {
        'records': new_list,
    }


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def access_search_term_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, input_text from icde_icde_record 
            where operation_type = %s group by input_text order by count desc
            limit 30
        ''', [const.PAPER_SEARCH])
        row = dictfetchall(cursor)
    
    return row

def access_click_rate_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type in (%s, %s) group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_DETAIL_CLICK, const.PAPER_ORIGIN_CLICK])
        row = dictfetchall(cursor)
    
    return row


def access_like_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_LIKE_CLICK])
        row = dictfetchall(cursor)
    
    return row

def access_dislike_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_DISLIKE_CLICK])
        row = dictfetchall(cursor)
    
    return row
    
def access_share_trending_list():

    with connection.cursor() as cursor:
        cursor.execute('''
            select count(1) as count, paper_id, paper_title from icde_icde_record 
            where operation_type = %s group by paper_id order by count desc
            limit 30
        ''', [const.PAPER_SHARE])
        row = dictfetchall(cursor)
    
    return row