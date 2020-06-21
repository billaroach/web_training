from django.shortcuts import render, get_object_or_404
from .models import Beer, Comments
from .forms import CommentForm, AddBeerForm
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.template.context_processors import csrf


def index(request):

    num_articles = Beer.objects.all().count()
    return render(request, 'Beer/index.html',
                  context={'num_articles': num_articles})


def all_beer(request):

    beers = Beer.objects.all()
    return render(request, 'Beer/beer_list.html', {'beers': beers})


def black_beer(request):

    beers = Beer.objects.filter(color__contains='Темное') | Beer.objects.filter(
            color__contains='Тёмное')
    return render(request, 'Beer/beer_list.html', {'beers': beers})


def light_beer(request):

    beers = Beer.objects.filter(color__contains='Светлое')
    return render(request, 'Beer/beer_list.html', {'beers': beers})


def details_beer(request, pk=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['beer'] = Beer.objects.get(id=pk)
    args['comments'] = Comments.objects.filter(comments_article=pk)
    args['form'] = comment_form
    return render(request, 'Beer/details_beer.html', args)


def add_comment(request, pk):

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Beer.objects.get(id=pk)
            form.save()
    return redirect('/all_beer/%s' % pk)


def add_beer(request):

    if request.POST:
        form = AddBeerForm(request.POST)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.save()
            return redirect('all_beer')

    else:
        form = AddBeerForm()

    return render(request, 'Beer/add_beer.html', {'form': form})






