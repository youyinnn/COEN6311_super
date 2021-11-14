from researcher.models import Researcher, ResearchTeam
from django.db.utils import IntegrityError
from common.http_response import json_response_builder as response
from common.password import gen as pw_gen, verify as password_verify
from common.jwt import gen as jwt_gen, get_user_id as get_id_from_request
from common.jwt import auth_require, remove_token
from datetime import datetime

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
        jwt = jwt_gen(user.id, {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'area': user.area,
            'name': user.name,
            # 'time': datetime.now()
        })

        return response(0, headers={
            'Authorization': jwt
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
    newArea = postParams.get('area')
    if newName != None:
        newProfile['name'] = newName
    if newPassword != None:
        newProfile['password'] = pw_gen(newPassword)  
    if newArea != None:
        newProfile['area'] = newArea
        
    query = Researcher.objects.filter(id = user_id)
    if (len(query) == 0):
        return response(1, "No such user")
    else:
        Researcher(id = user_id, **newProfile).save(
            update_fields=[*list(newProfile)])
        # TODO: exoire token if update password
        print('password' in newProfile)
        return response(0)
