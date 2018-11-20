# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import PostForm
 
from blogs import models as m
from blogs.forms import PostForm    
    
def index(request):
    two_days_ago = datetime.utcnow() - timedelta(days=2)
 
    # Retrieve a list of posts that are created less than two days ago
    recent_posts = m.Post.objects.filter(created_at__gt=two_days_ago).all()
 
    # Load the template myblog/templates/index.html
    template = loader.get_template('index.html')
 
    # Context is a normal Python dictionary whose keys can be accessed in the template index.html
    context = dict({
        'post_list': recent_posts
    })
 
    return HttpResponse(template.render(context))

def postdetail(request, post_id):
    try:
        post = m.Post.objects.get(pk=post_id)
    except m.Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'post/detail.html', {'post': post})

def post_upload(request):
    if request.method == 'GET':
        return render(request, 'post/upload.html', {})
    elif request.method == 'POST':
        post = m.Post.objects.create(content=request.POST['content'],
                                     created_at=datetime.utcnow())
        # No need to call post.save() at this point -- it's already saved.
        return HttpResponseRedirect(reverse('postdetail', kwargs={'post_id': post.id}))


def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content,
                                         created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
 
    return render(request, 'post/post_form_upload.html', {
        'form': form,
    })

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})