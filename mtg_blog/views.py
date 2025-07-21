from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import Topic

def home(request):
    topics = (
        Topic.objects
        .annotate(
            num_posts = Count('posts'))
        .order_by('-num_posts')[:10]
    )
    return render(request, 'mtg_blog_app/home.html', {'topics': topics})

class TopicListView(ListView):
    '''List all topics alphabetically'''

    model = Topic
    template_name = 'mtg_blog_app/topic_list.html'
    context_object_name = 'topic_list'

    def get_query(self):
        return Topic.objects.all().order_by('name')