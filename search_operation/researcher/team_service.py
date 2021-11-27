from researcher.models import Researcher, ResearchTeam, ResearchTeamAuth
from common.project_const import const

def get_team_by_team_name(team_name):
    query = ResearchTeam.objects.filter(name=team_name)
    if len(query) == 0:
        return None
    else:
        return query[0] 

def create_team(team_name, leader_id):
    return ResearchTeam.objects.create(
        name= team_name,
        leader_id = leader_id
    )

def create_team_auth(researcher_id, team_id):
    ResearchTeamAuth.objects.create(
        researcher_id = researcher_id,
        team_id = team_id,
        state = const.JOINED,
        role_tag= 'leader',
    )

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

def get_team_by_leader_id_and_team_id(leader_id, team_id):
    query = ResearchTeam.objects.filter(
        id = team_id,
        leader_id = leader_id
    )
    if len(query) == 0:
        return None
    else:
        return query[0]


def joined_team_auth_query(team_id):
    query = ResearchTeamAuth.objects.filter(
        team_id = team_id,
        state = const.JOINED
    )
    if len(query) == 0:
        return None
    else:
        return query

def get_team_member_list(auth_query):
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

    return member_list

def get_team_auth_by_team_id_and_user_id(team_id, user_id):
    query = ResearchTeamAuth.objects.filter(
        team_id = team_id,
        researcher_id = user_id
    )
    if len(query) == 0:
        return None
    else:
        return query[0]

def create_pending_team_auth(invitee_id, team_id):
    ResearchTeamAuth.objects.create(
        researcher_id = invitee_id,
        team_id = team_id,
        state = const.PENDING,
    )
