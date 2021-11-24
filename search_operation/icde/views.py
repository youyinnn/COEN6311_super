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
    paper_id =  getParams.get('paper_id')
    joined_team_list = get_team_list_by_state(user_id, const.JOINED)

    print(paper_id)

    icde_record_list = ICDE.query_to_list(IcdeRecord.objects.filter(
        operation_type =  const.PAPER_SHARE,
        paper_id = paper_id
    ))

    print(icde_record_list)

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
