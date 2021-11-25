"""search_operation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path as urlPath
from search.views import search_papers, delete_objects, view_paperdb
from search.views import comment_paper, like_paper, get_paper_user_attitude
from search.views import get_paper_comments, get_paper_like_count
from researcher.views import register, login, logout
from researcher.views import update
from researcher.views import create_team, get_team_list, get_team_member
from researcher.views import invite_member, handle_invitation
from researcher.views import change_team_role_tag
from icde.views import get_paper_team_share_records, share_paper
from icde.views import search_paper, go_paper_origin, go_paper_detail_page
from icde.views import get_user_activities, get_team_member_activities
from icde.views import get_all_trending_list

from django.conf import settings

def pathWithContext(path, pattern):
    return urlPath(settings.CONTEXT + '/' + path, pattern)

urlpatterns = [
    pathWithContext('user', register),
    pathWithContext('user/login', login),
    pathWithContext('user/logout', logout),
    pathWithContext('user/update', update),

    # TODO: with restful respect
    pathWithContext('team/create', create_team),
    pathWithContext('team/list', get_team_list),
    pathWithContext('team/member/list', get_team_member),
    pathWithContext('team/invite', invite_member),
    pathWithContext('team/invite/handle', handle_invitation),
    pathWithContext('team/role-tag', change_team_role_tag),

    urlPath('paper/search/input=<str:keywords>&<int:number>', search_papers),
    urlPath('paper/search/delete_all_objects', delete_objects),
    urlPath('paper/search/test/show_paper_db', view_paperdb),
    pathWithContext('paper/comment', comment_paper),
    pathWithContext('paper/comments', get_paper_comments),
    pathWithContext('paper/like', like_paper),
    pathWithContext('paper/like/user', get_paper_user_attitude),
    pathWithContext('paper/like/count', get_paper_like_count),

    pathWithContext('icde/capture/share-paper', share_paper),
    pathWithContext('icde/capture/search-paper', search_paper),
    pathWithContext('icde/capture/go-paper-origin', go_paper_origin),
    pathWithContext('icde/capture/go-paper-detail-page', go_paper_detail_page),
    pathWithContext('icde/access/shared-team-list', get_paper_team_share_records),
    pathWithContext('icde/access/user-activities', get_user_activities),
    pathWithContext('icde/access/team-activities', get_team_member_activities),

    pathWithContext('icde/access/all-trending', get_all_trending_list),
]
