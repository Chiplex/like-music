from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'clave_re/index.html')

def songs(request):
    return render(request, 'clave_re/songs.html')

def artists(request):
    return render(request, 'clave_re/artists.html')

def albums(request):
    return render(request, 'clave_re/albums.html')

def tempo_features(request):
    return render(request, 'clave_re/tempo_features.html')

def dynamic_features(request):
    return render(request, 'clave_re/dynamic_features.html')
    

