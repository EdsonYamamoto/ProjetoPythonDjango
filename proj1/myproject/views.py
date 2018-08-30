from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from .models import Board, Topic

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
