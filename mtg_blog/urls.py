from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
]
