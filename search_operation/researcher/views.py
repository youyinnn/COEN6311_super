from researcher.models import Researcher, ResearchTeam, ResearchTeamAuth
from common.http_response import json_response_builder as response
from common.password import gen as pw_gen
from common.jwt import gen as jwt_gen, get_user_id as get_id_from_request
from common.jwt import auth_require, remove_token
from common.project_const import const

from . import user_service
from . import team_service

def register(request):
    postParams = request.POST.dict()
    code = user_service.register(postParams)
    return response(code)

def login(request): 
    postParams = request.POST.dict()
    # print(postParams)
    user = user_service.get_user_by_username(postParams['username'])
    if user == None:
        return response(1)

    if user_service.password_verified(postParams['password'], user.password):
        token = jwt_gen(user.id, {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'area': user.area,
            'name': user.name,
            'title': user.title,
            # 'time': datetime.now()
        })

        return response(0, body={
            'token': token
        })
    else:
        return response(2)
    
@auth_require
def logout(request):
    user_id = get_id_from_request(request)
    remove_token(user_id)
    return response(0)


@auth_require
def update(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    newProfile = {}
    newName = postParams.get('name')
    newPassword = postParams.get('password')
    newEmail = postParams.get('email')
    newArea = postParams.get('area')
    newTitle = postParams.get('title')
    if newName != None:
        newProfile['name'] = newName
    if newPassword != None:
        newProfile['password'] = pw_gen(newPassword)  
    if newArea != None:
        newProfile['area'] = newArea
    if newTitle != None:
        newProfile['title'] = newTitle
    if newEmail != None:
        newProfile['email'] = newEmail
        
    user = user_service.get_user_by_id(user_id)
    if (user == None):
        return response(1, message="No such user")
    else:
        return response(**user_service.user_info_update(user_id, newProfile))




@auth_require
def create_team(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    team_name = postParams['name']
    teamModel = team_service.get_team_by_team_name(team_name)
    
    if teamModel == None:
        team = team_service.create_team(team_name, user_id)
        team_service.create_team_auth(user_id, team.id)
        return response(0, message="Create team " + team_name + " succeeded" )
    else:
        # team exist
        return response(1, message='Team name exist.')

@auth_require
def get_team_list(request):
    user_id = get_id_from_request(request)
    joined_team_list = team_service.get_team_list_by_state(user_id, const.JOINED)
    pending_team_list = team_service.get_team_list_by_state(user_id, const.PENDING)

    return response(0, body={
        'joined_list': joined_team_list,
        'pending_list': pending_team_list,
    })

@auth_require
def get_team_member(request):
    getParams = request.GET.dict()

    auth_query = team_service.joined_team_auth_query(getParams['team_id'])
    if auth_query == None:
        return response(1, message='No such Team.')

    return response(0, body={
        'member_list': team_service.get_team_member_list(auth_query)
    })

@auth_require
def invite_member(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    team_id = postParams.get('team_id')
    invitee_email = postParams.get('invitee_email')

    # query the team
    teamModel = team_service.get_team_by_leader_id_and_team_id(user_id, team_id)

    if teamModel == None:
        return response(1, message='Not the leader of this team')
    else: 
        # query the invitee
        invitee_user_model = user_service.get_user_by_email(invitee_email)
        if invitee_user_model == None:
            return response(1, message="No such user with this email.")
        else:
            invitee = invitee_user_model
            # user is leader of the team & invitee email is valid
            invitee_auth_model = team_service.get_team_auth_by_team_id_and_user_id(team_id, invitee.id)
            if invitee_auth_model == None:
                # no invite record
                team_service.create_pending_team_auth(invitee.id, team_id)
                return response(0)
            else:
                # invite record exist
                invitee_auth = invitee_auth_model
                state = invitee_auth.state
                if state == const.PENDING:
                    return response(2, message='Invitation has been sent.')
                if state == const.JOINED:
                    return response(3, message='Invitee has joined.')
                if state == const.LEFT or state == const.REJECTED:
                    # invite again
                    invitee_auth.state = const.PENDING
                    invitee_auth.save(update_fields=['state'])
                    return response(4, message="Invite user again.")

@auth_require
def handle_invitation(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    auth_id = postParams.get('auth_id')
    # accept: 1, reject: 3
    try:
        decision = int(postParams.get('decision'))
    except ValueError as e:
        return response(1, message="Wrong decision.")

    if decision not in [1, 2, 3]:
        return response(1, message="Wrong decision.")
    else:
        # decision in 1,2,3
        auth_query = ResearchTeamAuth.objects.filter(
            id = auth_id,
            researcher_id = user_id,
        )
        if len(auth_query) == 0:
            return response(2, message="No invitation of this")
        else:
            auth = auth_query[0]
            # decision 1,3: join or reject
            if decision in [1, 3]:
                # only accept decision from state 0
                if auth.state != const.PENDING:
                    return response(3, message="Can make decision 'join' or 'reject' from state which not in 'pending'.")
            else:
                # decision 2: leave the team
                if auth.state != const.JOINED:
                    return response(4, message="Can make decision 'leave' from state which not in 'joined'.")

            # make valid decision
            auth.state = decision
            auth.save(update_fields=['state'])
            return response(0, message="Decision is made.")

@auth_require
def change_team_role_tag(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    auth_id = postParams.get('auth_id')
    role_tag = postParams.get('role_tag')

    auth_query = ResearchTeamAuth.objects.filter(
        id = auth_id,
        researcher_id = user_id,
        state = const.JOINED
    )

    if len(auth_query) == 0:
        return response(1, message='No such team auth')
    else:
        auth = auth_query[0]
        auth.role_tag = role_tag
        auth.save(update_fields=['role_tag'])
        return response(0)