import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mtg_blog.models import Topic, Post

@pytest.mark.django_db
def test_home_view_renders_topic(client):
    user = User.objects.create_user(username='testuser', password='pass')
    topic1 = Topic.objects.create(name='Red Aggro')
    post = Post.objects.create(
        title='Fast Win',
        content='...',
        author = user,
    )
    post.topics.add(topic1)

    response = client.get(reverse('mtg_blog_app:home'))
    assert response.status_code == 200
    assert b'Red Aggro' in response.content
@pytest.mark.django_db
def test_topic_list_view(client, db):

    Topic.objects.create(name='Favourite Art', slug='favourite-art')
    Topic.objects.create(name='MTG Lore', slug='mtg-lore')

    response = client.get(reverse('mtg_blog_app:topic_list'))
    assert response.status_code == 200
    assert 'Favourite Art' in response.content.decode()
    assert 'MTG Lore' in response.content.decode()

    topics = response.context['topic_list']
    assert topics[0].name, 'Favourite Art'
    assert topics[1].name, 'MTG Lore'