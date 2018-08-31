from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Board, Post, Topic
from ..views import reply_topic


class ReplyTopicTestCase(TestCase):
    '''
    Base de teste usado em todos os reply_topics views
    '''

    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(
            username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(
            subject='Hello World', board=self.board, starter=user)
        Post.objects.create(message='Lorem', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={
                           'pk': self.board.pk, 'topic_pk': self.topic.pk})


class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    print('LoginRequiredReplyTopicTests')


class ReplyTopicTests(ReplyTopicTestCase):
    print('ReplyTopicTests')


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    print('SuccessfulReplyTopicTests')


class InvalidReplyTopicTests(ReplyTopicTestCase):
    print('InvalidReplyTopicTests')
