import json
from django.http import HttpResponse

def json_response_builder(code, headers={}, message=None, body=None):
    headers['Content-Type'] = 'application/json'
    return HttpResponse(json_builder(code, message, body), headers=headers)

def json_builder(code, message=None, body=None):
    obj = {
        'code': code,
        'message': message,
        'body': body
    }

    if message == None:
        del obj['message']
    if body == None:
        del obj['body']

    return json.dumps(obj)