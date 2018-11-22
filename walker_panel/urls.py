from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^task/$', views.task_page, name='task'),
    re_path(r'^task/(?P<task_id>[0-9]+)/$', views.task_page, name='task'),
    re_path(r'^remove-task/(?P<task_id>[0-9]+)/$', views.remove_task, name='remove_task'),
    re_path(r'^change-task-status/(?P<task_id>[0-9]+)/$', views.change_task_status, name='change_task_status'),
    re_path(r'^logs/$', views.logs, name='logs'),
    re_path(r'^settings/$', views.settings, name='settings'),
    re_path(r'^sign-up/$', views.sign_up, name='sign_up'),
    re_path(r'^sign-in/$', views.sign_in, name='sign_in'),
    re_path(r'^sign-out/$', views.sign_out, name='sign_out'),
]