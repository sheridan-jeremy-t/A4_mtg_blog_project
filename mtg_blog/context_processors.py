from django.db.models import Count
from .models import Topic

def topic_context(request):
    topics = (Topic.objects
    .annotate(num_posts=Count('posts'))
    .order_by('-num_posts')[:10]
)

    return {'topics' : topics}