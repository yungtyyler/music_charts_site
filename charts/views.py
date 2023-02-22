from django.shortcuts import render, get_object_or_404
from .models import Chart, Song

def index(request):
    charts = Chart.objects.all()

    return render(request, 'charts/index.html', {
        'charts': charts,
    })

def detail(request, pk):
    chart = get_object_or_404(Chart, pk=pk)
    related_songs = Song.objects.filter(decade_id=chart.id).order_by('-rank').values()

    return render(request, 'charts/detail.html', {
        'chart': chart,
        'songs': related_songs,
    })