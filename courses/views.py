from django.shortcuts import render
from .models import Course


# Create your views here.
def course_list(request):
    courses = Course.planned_courses()
    return render(request, 'course_list.html', context={'courses': courses})