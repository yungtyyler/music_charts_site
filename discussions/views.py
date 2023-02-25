from django.shortcuts import render, get_object_or_404, redirect
from charts.models import Chart
from .models import Post, Topic
from charts.models import Chart
from .forms import TopicForm, TopicPostForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    topics = Topic.objects.all()
    charts = Chart.objects.all()

    return render(request, 'discussions/index.html', {
        'topics': topics,
        'charts': charts
    })


@login_required
def new_topic(request, chart_pk):
    chart = get_object_or_404(Chart, id=chart_pk)

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.decade = chart
            topic.created_by = request.user
            topic.save()

            return redirect('discussions:index')
    else:
        form = TopicForm()

    return render(request, 'discussions/new.html', {
        'chart': chart,
        'form': form
    })

@login_required
def new_discussion_post(request, topic_pk):
    topic = get_object_or_404(Topic, id=topic_pk)
    
    if request.method == 'POST':
        form = TopicPostForm(request.POST)

        if form.is_valid():
            topic_post = form.save(commit=False)
            topic_post.topic = topic
            topic_post.created_by = request.user
            topic_post.save()

            return redirect('discussions:index')
        
    else:
        form = TopicPostForm()
    
    return render(request, 'discussions/new_post.html', {
        'form': form
    })
    
@login_required
def user_posts(request):
    topics = Topic.objects.filter(created_by=request.user).order_by('-created_at')
    charts = Chart.objects.all()
    posts = Post.objects.filter(created_by=request.user).order_by('-created_at')

    return render(request, 'discussions/user_posts.html', {
        'topics': topics,
        'charts': charts,
        'posts': posts
    })

@login_required
def topic_posts(request, topic_pk):
    topic = get_object_or_404(Topic, id=topic_pk)
    posts = Post.objects.filter(topic=topic)
    charts = Chart.objects.all()

    return render(request, 'discussions/topic_posts.html', {
        'topic': topic,
        'posts': posts,
        'charts': charts,
    })