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

    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert b'Red Aggro' in response.content

def test_topic_list_view(self):

    Topic.objects.create(name='Favourite Art', slug='favourite-art')
    Topic.objects.create(name='MTG Lore', slug='mtg-lore')

    response = self.client.get('/topics/')

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Favourite Art')
    self.assertContains(response, 'MTG Lore')

    topics = response.context['topic_list']
    self.assertEqual(topics[0].name, 'Favourite Art')
    self.assertEqual(topics[1].name, 'MTG Lore')