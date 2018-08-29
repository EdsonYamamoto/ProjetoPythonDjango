from django.shortcuts import get_object_or_404, render
from .models import Topic
from .models import Board

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})