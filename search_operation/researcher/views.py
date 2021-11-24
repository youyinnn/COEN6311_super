from researcher.models import Researcher, ResearchTeam, ResearchTeamAuth
from django.db.utils import IntegrityError
from common.http_response import json_response_builder as response
from common.password import gen as pw_gen, verify as password_verify
from common.jwt import gen as jwt_gen, get_user_id as get_id_from_request
from common.jwt import auth_require, remove_token

def register(request):
    print('---------------')
    postParams = request.POST.dict()
    # request example:
    # {
    #  'username': 'Vito52', 
    #  'password': '123', 
    #  'name': 'Fred King Sr.', 
    #  'email': 'Vivienne83@hotmail.com', 
    #  'area': '[Configuration,Infrastructure, Metrics]'
    #  'title': 'Phd'
    # }
    postParams['password'] = pw_gen(postParams['password'])
    print(postParams)
    try: 
        Researcher.objects.create(
            **postParams  
        )
    except IntegrityError as e:
        stre = str(e)
        if 'UNIQUE' in stre and 'username' in stre:
            return response(1)        
        if 'UNIQUE' in stre and 'email' in stre:
            return response(2)

    return response(0)

def login(request): 
    postParams = request.POST.dict()
    # print(postParams)
    user = Researcher.objects.filter(username=postParams['username'])
    if len(user) == 0:
        return response(1)
    else:
        user = user[0]

    if password_verify(postParams['password'], user.password):
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
    print(postParams)
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
        
    query = Researcher.objects.filter(id = user_id)
    if (len(query) == 0):
        return response(1, "No such user")
    else:
        try:
            Researcher(id = user_id, **newProfile).save(
                update_fields=[*list(newProfile)])
            user = Researcher.objects.filter(id=user_id)[0]
            token = jwt_gen(user_id, {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'area': user.area,
                'name': user.name,
                'title': user.title,
            })
            return response(0, body={
                'new_token': token
            })
        except IntegrityError as e:
            stre = str(e)
            print(stre)
            return response(2, message="This e-mail has been used.")



from common.project_const import const

@auth_require
def create_team(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    team_name = postParams['name']

    query = ResearchTeam.objects.filter(name=team_name, leader_id = user_id)
    
    if len(query) == 0:
        team = ResearchTeam.objects.create(
            name= postParams['name'],
            leader_id = user_id
        )
        print(team.__dict__)
        auth = ResearchTeamAuth.objects.create(
            researcher_id = user_id,
            team_id = team.id,
            state = const.JOINED,
            role_tag= 'leader',
        )
        print(auth.__dict__)
        return response(0)
    else:
        # team exist
        return response(1, message='Team name exist.')

@auth_require
def get_team_list(request):
    user_id = get_id_from_request(request)
    joined_team_list = get_team_list_by_state(user_id, const.JOINED)
    pending_team_list = get_team_list_by_state(user_id, const.PENDING)

    return response(0, body={
        'joined_list': joined_team_list,
        'pending_list': pending_team_list,
    })

@auth_require
def get_team_member(request):
    user_id = get_id_from_request(request)
    getParams = request.GET.dict()

    auth_query = ResearchTeamAuth.objects.filter(
        team_id = getParams['team_id'],
        state = const.JOINED
    )
    if len(auth_query) == 0:
        return response(1, message='No such Team.')

    member_id_list = []
    member_role_tag_map = {}
    for auth in auth_query:
        member_id_list.append(auth.researcher_id)
        member_role_tag_map[auth.researcher_id] = auth.role_tag
    
    member_query = Researcher.objects.filter(
        id__in = [*member_id_list]
    )

    member_list = []
    for researcher in member_query:
        member_list.append({
            'id': researcher.id,
            'name': researcher.name,
            'email': researcher.email,
            'role_tag': member_role_tag_map[researcher.id]
        })

    return response(0, body={
        'member_list': member_list
    })

def get_team_list_by_state(user_id, state):
    team_list = []
    # query auth first
    auth_query = ResearchTeamAuth.objects.filter(
        researcher_id = user_id,
        state = state
    )
    auth_map = {}
    team_id_list = []
    for auth in auth_query:
        team_id_list.append(auth.team_id)
        auth_map[auth.team_id] = auth

    # them query the team
    team_query = ResearchTeam.objects.filter(
        id__in = [*team_id_list]
    )
    for team in team_query:
        team_list.append({
            'auth_id': auth_map[team.id].id, 
            'team_id': team.id,
            'leader_id': team.leader_id,
            'name': team.name,
            'auth_create_time': int(round(auth_map[team.id].create_time.timestamp() * 1000)),
        })
    
    return team_list

@auth_require
def invite_member(request):
    postParams = request.POST.dict()
    user_id = get_id_from_request(request)
    team_id = postParams.get('team_id')
    invitee_email = postParams.get('invitee_email')

    # query the team
    team_query = ResearchTeam.objects.filter(
        id = team_id,
        leader_id = user_id
    )
    print(team_id, user_id)
    if len(team_query) == 0:
        return response(1, message='Not the leader of this team')
    else: 
        # query the invitee
        invitee_query = Researcher.objects.filter(
            email = invitee_email,
        )
        if len(invitee_query) == 0:
            return response(1, message="No such user with this email.")
        else:
            invitee = invitee_query[0]
            # user is leader of the team & invitee email is valid
            invitee_auth_query = ResearchTeamAuth.objects.filter(
                team_id = team_id,
                researcher_id = invitee.id
            )
            if len(invitee_auth_query) == 0:
                # no invite record
                auth = ResearchTeamAuth.objects.create(
                    researcher_id = invitee.id,
                    team_id = team_id,
                    state = const.PENDING,
                )
                return response(0)
            else:
                # invite record exist
                invitee_auth = invitee_auth_query[0]
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

# TODO: icde
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