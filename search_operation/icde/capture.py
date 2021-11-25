# decorator
from functools import wraps
from common.project_const import const
from common.jwt import get_user_id as get_id_from_request
from icde import models as ICDE

def icde_capture(operation_type):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kw):
            if operation_type == const.PAPER_COMMENT:
                capture_comment_activity(*args, **kw)
            if operation_type == const.PAPER_LIKE_CLICK or operation_type == const.PAPER_DISLIKE_CLICK:
                capture_like_or_dislike_activity(*args, **kw)            
            if operation_type == const.PAPER_SHARE:
                capture_share_activity(*args, **kw)            
            if operation_type == const.PAPER_SEARCH:
                capture_search_activity(*args, **kw)            
            if operation_type == const.PAPER_ORIGIN_CLICK:
                capture_go_to_origin_activity(*args, **kw)            
            if operation_type == const.PAPER_DETAIL_CLICK:
                capture_go_to_detail_activity(*args, **kw)
            return func(*args, **kw)
        return inner
    return decorator

def capture_comment_activity(request):
    postParams = request.POST.dict()
    paper_id = postParams.get('paper_id')
    user_id = get_id_from_request(request)
    paper_title = postParams.get('paper_title')
    ICDE.paper_comment_record(user_id, paper_id, paper_title)

def capture_like_or_dislike_activity(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    paper_id = postParams.get('paper_id')
    paper_title = postParams.get('paper_title')
    like = False if postParams.get('like') == '0' else True
    if like: 
        ICDE.paper_like_click_record(user_id, paper_id, paper_title)
    else:
        ICDE.paper_dislike_click_record(user_id, paper_id, paper_title)

def capture_share_activity(request):
    user_id = get_id_from_request(request)
    postParams = request.POST.dict()
    team_id = postParams.get('team_id')
    team_name = postParams.get('team_name')
    paper_id =  postParams.get('paper_id')
    paper_title =  postParams.get('paper_title')
    ICDE.paper_share_click_record(user_id, paper_id, team_id, team_name, paper_title)

def capture_search_activity(request):
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

def capture_go_to_origin_activity(request):
    postParams = request.POST.dict()
    is_login = postParams.get('is_login') == 'true'
    paper_id = postParams.get('paper_id')
    paper_title = postParams.get('paper_title')

    if is_login:
        user_id = get_id_from_request(request)
        ICDE.paper_origin_click_record(user_id, paper_id, paper_title)
    else:
        ICDE.paper_search_record(-1, paper_id, paper_title)

def capture_go_to_detail_activity(request):
    postParams = request.POST.dict()
    is_login = postParams.get('is_login') == 'true'
    paper_id = postParams.get('paper_id')
    paper_title = postParams.get('paper_title')
    if is_login:
        user_id = get_id_from_request(request)
        ICDE.paper_detail_click_record(user_id, paper_id, paper_title)
    else:
        ICDE.paper_detail_click_record(-1, paper_id, paper_title)