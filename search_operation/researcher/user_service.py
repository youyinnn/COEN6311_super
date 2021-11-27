from researcher.models import Researcher, ResearchTeam, ResearchTeamAuth
from common.password import gen as pw_gen, verify as password_verify
from django.db.utils import IntegrityError
from common.jwt import gen as jwt_gen, get_user_id as get_id_from_request

def register(postParams):
    postParams['password'] = pw_gen(postParams['password'])
    try: 
        Researcher.objects.create(
            **postParams  
        )
    except IntegrityError as e:
        stre = str(e)
        if 'UNIQUE' in stre and 'username' in stre:
            return 1       
        if 'UNIQUE' in stre and 'email' in stre:
            return 2

    return 0

def get_user_by_username(username):
    user_query = Researcher.objects.filter(username = username)
    if len(user_query) == 0:
        return None
    else:
        return user_query[0]

def get_user_by_id(user_id):
    user_query = Researcher.objects.filter(id = user_id)
    if len(user_query) == 0:
        return None
    else:
        return user_query[0]

def get_user_by_email(email):
    query = Researcher.objects.filter(
        email = email,
    )
    if len(query) == 0:
        return None
    else:
        return query[0]

def password_verified(plainPassword, encryptedPassword):
    return password_verify(plainPassword, encryptedPassword);

def user_info_update(user_id, newProfile):
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
        return {
            'code': 0, 
            'body': {
                'new_token': token
            }
        }
    except IntegrityError as e:
        return {
            'code': 2, 
            "message":"This e-mail has been used."
        }