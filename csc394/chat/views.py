# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })