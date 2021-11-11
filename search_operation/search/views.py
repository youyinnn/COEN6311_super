from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from search.models import Paper_Metadata
import urllib.request
import json
import datetime

paper_id_list = [0]


# Create your views here.
def search_papers(request, keywords, number):
    print(type(keywords), keywords)
    print(type(number), number)
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
