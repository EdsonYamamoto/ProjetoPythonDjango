from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Topic, Post
from ..views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='novo board Django.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(
            username=self.username, email='123@123.com', password=self.password)
        self.topic = Topic.objects.create(
            subject='Hello, world', board=self.board, starter=user)
        self.post = Post.objects.create(
            message='asdqwe', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk})


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class UnauthorizedPostUpdateViewTest(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        username = 'zxczxczxczxczxc'
        password = '231'
        user = User.objects.create_user(
            username=username, email='aksndkasndk@adasd.vc', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 404)


# class PostUpdateViewTests(PostUpdateViewTestCase):

# class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):

# class InvalidPostUpdateViewTests(PostUpdateViewTestCase):
