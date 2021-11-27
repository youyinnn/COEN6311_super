from common.http_response import json_response_builder as response

from common.jwt import get_user_id as get_id_from_request
from common.jwt import auth_require

from common.project_const import const
from icde.capture import icde_capture

from . import access as icde_access

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
    icde_access.access_paper_team_share_records

    return response(0, body=icde_access.access_paper_team_share_records(user_id, paper_id))

@auth_require
def get_user_activities(request):
    user_id = get_id_from_request(request)

    return response(0, body=icde_access.access_user_activities(user_id))

@auth_require
def get_team_member_activities(request):
    getParams = request.GET.dict()
    team_id = getParams.get('team_id')

    return response(0, body=icde_access.access_team_member_activities(team_id))

def get_all_trending_list(request):
    searh_term_trending = icde_access.access_search_term_trending_list()
    click_rate_trending = icde_access.access_click_rate_trending_list()
    like_trending = icde_access.access_like_trending_list()
    dislike_trending = icde_access.access_dislike_trending_list()
    share_trending = icde_access.access_share_trending_list()
    
    return response(0, body={
        'tranding_list': [
            searh_term_trending, 
            click_rate_trending, 
            like_trending, 
            dislike_trending,
            share_trending
        ]
    })