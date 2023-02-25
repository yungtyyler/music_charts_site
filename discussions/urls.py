from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.index, name='index'),
    path('topic-posts/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('user-posts/', views.user_posts, name='user_posts'),
    path('new-discussion-post/<int:topic_pk>/', views.new_discussion_post, name='new_discussion_post'),
    path('new/<int:chart_pk>/', views.new_topic, name='new'),
]