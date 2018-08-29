from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm
