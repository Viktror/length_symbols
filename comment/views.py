from django.shortcuts import render

from django.views import generic

from comment.forms import CommentForm
from comment.utils import count_letters
from .models import *


# Create your views here.

class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = 'index.html'


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            symbols = str(comment.text).split()
            all_symbols = len(''.join(symbols))
            tuple_answ = count_letters(''.join(symbols))
            vowels = tuple_answ[0]
            consonants = tuple_answ[1]
            comment.save()
            return render(request, 'info_comment.html', context={'all_symbols': all_symbols, 'vowels': vowels,
                                                                 'consonants': consonants})
    else:
            form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})


def info_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    symbols = str(comment.text).split()
    all_symbols = len(''.join(symbols))
    tuple_answ = count_letters(''.join(symbols))
    vowels = tuple_answ[0]
    consonants = tuple_answ[1]
    return render(request, 'info_comment.html', context={'all_symbols': all_symbols, 'vowels': vowels,
                                                         'consonants': consonants})
