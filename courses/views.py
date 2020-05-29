from django.shortcuts import render, get_object_or_404
from .models import Course #importando o model de cursos
# Create your views here.


def courses(request):

    courses = Course.objects.all() #pegando todos os cursos através do manage
    context = {
        'courses' : courses
    }
    
    return render(request, 'courses/index.html', context)

def details(request, id):

    #retirando o pk de '.../curses/?pk=1'

    #course = Course.objects.get(id=id)
    course = get_object_or_404(Course, id=id)
    context = { 'course' : course }

    return render(request, 'courses/details.html', context)