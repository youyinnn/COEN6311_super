from researcher.models import Researcher, ResearchTeam
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from common.http_response import json_response_builder as response

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
    postParams['password'] = make_password(postParams['password'])
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
