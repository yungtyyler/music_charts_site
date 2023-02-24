from django.shortcuts import render
from charts.models import Chart
from .forms import SignUpForm


def index(request):
    charts = Chart.objects.all()

    return render(request, 'core/index.html', {
        'charts': charts,
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/signup_success.html')
        else:
            form = SignUpForm()

    form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })