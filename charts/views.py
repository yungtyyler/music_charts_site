from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Chart, Song

def songs(request):
    query = request.GET.get('query', '')
    chart_id = request.GET.get('chart', 0)
    songs = Song.objects.all().order_by('title').values()
    charts = Chart.objects.all()

    if chart_id:
        songs = songs.filter(decade_id=chart_id)

    if query:
        songs = songs.filter(Q(title__icontains=query) | Q(artist__icontains=query))

    return render(request, 'charts/songs.html', {
        'songs': songs,
        'query': query,
        'charts': charts,
        'chart_id': int(chart_id),
    })

def detail(request, pk):
    chart = get_object_or_404(Chart, pk=pk)
    related_songs = Song.objects.filter(decade_id=chart.id).order_by('-rank').values()

    return render(request, 'charts/detail.html', {
        'chart': chart,
        'songs': related_songs,
    })