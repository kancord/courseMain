from django.shortcuts import render
from django.http import *
from .models import User,Course, Document, Subscribe
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_course=Course.objects.all().count()  #количество курсов
    return render(request,'index.html',context={'num_course':num_course})

def indextsturl(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_course= 'secreturl'
    return render(request,'index.html',context={'num_course':num_course})


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'course_list.html'

    def get_queryset(self):
        subs = Subscribe.objects.filter(subUser=self.request.user).values_list("course_id")
        return Course.objects.filter(id__in=subs)

@login_required
def CourseDetailView(request, pk):
    courseName = Course.objects.get(id=pk)
    subs = Subscribe.objects.filter(subUser=request.user).values_list("course_id")
    subs =([int(x[0]) for x in subs])
    if int(pk) in subs:
        queryset = Document.objects.filter(course_id=pk)
    else:
        queryset = Document.objects.none()
    return render(request,'course_detail.html', context={'docs':queryset, 'courseName':courseName })

