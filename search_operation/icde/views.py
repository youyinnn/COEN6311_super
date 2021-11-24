from icde.models import IcdeRecord
from common.http_response import json_response_builder as response
from icde import models as ICDE

from common.jwt import get_user_id as get_id_from_request
from common.jwt import auth_require

from researcher.views import get_team_list_by_state
from common.project_const import const

@auth_require
def share_paper(request):
    user_id = get_id_from_request(request)
    postParams = request.POST.dict()
    team_id = postParams.get('team_id')
    paper_id =  postParams.get('paper_id')
    ICDE.paper_share_click_record(user_id, paper_id, team_id)
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


def search_paper(request):
    postParams = request.POST.dict()
    is_login = postParams.get('is_login') == 'true'
    query = postParams.get('query').split(' ')
    if is_login:
        user_id = get_id_from_request(request)
        for text in query:
            ICDE.paper_search_record(user_id, text)
    else:
        for text in query:
            ICDE.paper_search_record(-1, text)
    return response(0)

def go_paper_origin(request):
    postParams = request.POST.dict()
    is_login = postParams.get('is_login') == 'true'
    paper_id = postParams.get('paper_id')
    if is_login:
        user_id = get_id_from_request(request)
        ICDE.paper_origin_click_record(user_id, paper_id)
    else:
        ICDE.paper_search_record(-1, paper_id)
    return response(0)

def go_paper_detail_page(request):
    postParams = request.POST.dict()
    is_login = postParams.get('is_login') == 'true'
    paper_id = postParams.get('paper_id')
    if is_login:
        user_id = get_id_from_request(request)
        ICDE.paper_detail_click_record(user_id, paper_id)
    else:
        ICDE.paper_detail_click_record(-1, paper_id)
    return response(0)

@auth_require
def like_paper(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    paper_id = postParams.get('paper_id')
    like = False if postParams.get('like') == '0' else True
    if like: 
        ICDE.paper_like_click_record(user_id, paper_id)
    else:
        ICDE.paper_dislike_click_record(user_id, paper_id)
    return response(0)

@auth_require
def comment_paper(request):
    postParams = request.POST.dict()
    paper_id = postParams.get('paper_id')
    user_id = get_id_from_request(request)
    ICDE.paper_comment_record(user_id, paper_id)


