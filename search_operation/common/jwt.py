import jwt
from django.conf import settings
from django.http import HttpRequest
from researcher.models import TokenPool

def gen(holder_id, payload):
    query = TokenPool.objects.filter(holder_id = holder_id)
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    if (len(query) == 0):
        TokenPool(holder_id = holder_id, token=token).save()
    else:
        query[0].token = token
        query[0].save(update_fields=['token'])
    return token

# carrier can be token str or HttpRequest
def get_user_id(carrier):
    return get_value(carrier, 'id')

def get_user_name(carrier):
    return get_value(carrier, 'name')
    
def get_user_email(carrier):
    return get_value(carrier, 'email')



def get_value(carrier, param_key, secret=settings.JWT_SECRET):
    # carrier is str
    if isinstance(carrier, str):
        return jwt.decode(carrier, secret, algorithms=["HS256"])[param_key]
    # carrier is HttpRequest
    if isinstance(carrier, HttpRequest):
        rawToken = carrier.headers.get('Authorization')
        token = rawToken.split(' ')[1]
        return jwt.decode(token, secret, algorithms=["HS256"])[param_key]


def remove_token(holder_id):
    query = TokenPool.objects.filter(holder_id = holder_id)
    if (len(query) != 0):
        query[0].delete()
    return 

# decorator
import functools
from . import http_response

def auth_require(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        request = args[0]
        rawToken = request.headers.get('Authorization')
        if (rawToken != None) :
            token = rawToken.split(' ')[1]
            try: 
                holder_id = get_value(token, 'id')
            except jwt.exceptions.DecodeError as e:
                # not jwt
                return http_response.notJwtAuthResponse
            if (holder_id == None):
                # no id in payload
                return http_response.unvalidAuthResponse
            if (len(TokenPool.objects.filter(holder_id = holder_id)) == 0):
                # token expired
                return http_response.expiredTokenAuthResponse
            
            # valid token
            return func(*args, **kw)
        else:
            return http_response.unAuthResponse
    return wrapper
    