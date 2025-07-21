from django.urls import path
from . import views

app_name = 'mtg_blog_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
]
