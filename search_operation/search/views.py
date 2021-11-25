from django.shortcuts import render
from django.http import HttpResponse
from search.models import Paper_Metadata, Paper_Comment, Paper_Like_Dislike
import urllib.request
import json
import datetime

paper_id_list = [0]


# Create your views here.
def search_papers(request, keywords, number):
    number = str(number)
    query_url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=' + keywords + '&fields=title,abstract,venue,authors,year,url,citationCount&limit=' + number

    with urllib.request.urlopen(query_url) as url:
        s = url.read()
    s = json.loads(s)

    paper_dict_list = []
    now_time = datetime.datetime.now()
    last_paper_id = paper_id_list[-1]
    count = 0

    for i in range(len(s['data'])):
        author_list = []
        for author in range(len(s['data'][i]['authors'])):
            author_list.append(s['data'][i]['authors'][author]['name'])
        # print(s['data'][i]['url'])
        new_paper = {'title': s['data'][i]['title'], 'abstract': s['data'][i]['abstract'],
                     'venue': s['data'][i]['venue'], 'authors': author_list, 'year': s['data'][i]['year'],
                     'n_citations': s['data'][i]['citationCount']}
        if not Paper_Metadata.objects.filter(title=s['data'][i]['title']):
            count = count + 1
            Paper_Metadata.objects.create(paper_id=count + last_paper_id, create_time=now_time,
                                          title=s['data'][i]['title'],
                                          author=author_list,
                                          abstract=s['data'][i]['abstract'],
                                          venue=s['data'][i]['venue'], year=s['data'][i]['year'],
                                          citations=s['data'][i]['citationCount'], url=s['data'][i]['url'])
            paper_id_list.append(count)
        paper_dict_list.append(new_paper)
        json_rlt = json.dumps(paper_dict_list)

    return HttpResponse(json_rlt)


def delete_objects(request):
    Paper_Metadata.objects.all().delete()
    return HttpResponse('Delete_all_objects')


def view_paperdb(request):
    paper_list_obj = Paper_Metadata.objects.all()
    print(Paper_Metadata.objects.all())
    return render(request, 'papermeta.html', {'li': paper_list_obj})

from common.http_response import json_response_builder as response
from django.views.decorators.http import require_http_methods
from common.jwt import auth_require
from common.jwt import get_user_id as get_id_from_request
from common.jwt import get_user_name as get_name_from_request
from common.jwt import get_user_email as get_email_from_request
from common.project_const import const
from icde.capture import icde_capture

@auth_require
@require_http_methods(["POST"])
@icde_capture(const.PAPER_COMMENT)
def comment_paper(request):
    paper_id = request.POST.get('paper_id')
    comment = request.POST.get('comment')
    commenter_id = get_id_from_request(request)
    commenter_name = get_name_from_request(request)
    commenter_email = get_email_from_request(request)
    Paper_Comment.objects.create(
        paper_id = paper_id, 
        commenter_id = commenter_id,
        commenter_name = commenter_name,
        commenter_email = commenter_email,
        comment = comment
    )
    return response(0)

@auth_require
@require_http_methods(["POST"])
@icde_capture(const.PAPER_LIKE_CLICK)
def like_paper(request):
    paper_id = request.POST.get('paper_id')
    like = False if request.POST.get('like') == '0' else True
    user_id = get_id_from_request(request)

    attitude_query = Paper_Like_Dislike.objects.filter(
        user_id=user_id,
        paper_id=paper_id,
    )

    if len(attitude_query) == 0:
        Paper_Like_Dislike.objects.create(
            user_id = user_id,
            paper_id = paper_id,
            like = like
        )
    else:
        attitude = attitude_query[0]
        old_like = attitude.like
        if (old_like == like):
            return response(1, message="Same attitude.")
        else:
            attitude.like = like
            attitude.save(update_fields=['like'])
    return response(0)

@require_http_methods(["GET"])
def get_paper_comments(request):
    paper_id = request.GET.get('paper_id')
    comment_list = []
    query = Paper_Comment.objects.filter(
        paper_id = paper_id
    )
    if len(query) == 0:
        # no comment
        return response(0, body={
        'comment_list': comment_list
    })
    for comment in query:
        comment_list.append({
            'time': int(round(comment.create_time.timestamp() * 1000)),
            'content': comment.comment,
            'name': comment.commenter_name,
            'email': comment.commenter_email,
            'u_id': comment.commenter_id,
        })
    return response(0, body={
        'comment_list': comment_list
    })

@require_http_methods(["GET"])
def get_paper_like_count(request):
    paper_id = request.GET.get('paper_id')
    result = {
        'like': 0,
        'dislike': 0
    }

    query = Paper_Like_Dislike.objects.filter(
        paper_id = paper_id
    )

    for attitude in query:
        if (attitude.like == True): 
            result['like'] = result['like'] + 1
        else:
            result['dislike'] = result['dislike'] + 1

    return response(0, body={
        'result': result
    })

@auth_require
@require_http_methods(["GET"])
def get_paper_user_attitude(request):
    user_id = get_id_from_request(request)
    paper_id = request.GET.get('paper_id')
    query = Paper_Like_Dislike.objects.filter(
        paper_id = paper_id,
        user_id = user_id
    )

    if len(query) == 0:
        body={
            'exist': False
        }
    else:
        body={
            'exist': True,
            'like': query[0].like
        }
    return response(0, body=body)