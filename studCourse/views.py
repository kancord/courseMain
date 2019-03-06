from django.shortcuts import render
from django.http import *
from .models import User,Course, Document, Subscribe
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DocumentForm, CourseForm
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
        if (self.request.user.is_staff):
            return Course.objects.all()
        subs = Subscribe.objects.filter(subUser=self.request.user).values_list("course_id")
        return Course.objects.filter(id__in=subs)

@login_required
def CourseDetailView(request, pk):
    courseName = Course.objects.get(id=pk)
    subs = Subscribe.objects.filter(subUser=request.user).values_list("course_id")
    subs =([int(x[0]) for x in subs])
    if (int(pk) in subs) or (request.user.is_staff):
        queryset = Document.objects.filter(course_id=pk)
    else:
        queryset = Document.objects.none()

    return render(request,'course_detail.html', context={'docs':queryset, 'courseName':courseName, 'courseid': pk})

class SubscribeListView(LoginRequiredMixin, generic.ListView):
    model = Subscribe
    context_object_name = 'subscribe_list'
    template_name = 'subscribe_list.html'

    def get_queryset(self):
        if (self.request.user.is_staff):
            return Subscribe.objects.all()
        else:
            return Subscribe.objects.none()

class CourseCreate(CreateView):
    model = Course
    fields = ['name']
    template_name = 'course_form.html'

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name']
    template_name = 'course_form.html'

class CourseDelete(DeleteView):
    model = Course
    template_name = 'course_confurm_delete.html'
    success_url = reverse_lazy('courses')

class DocumentCreate(CreateView):
    model = Document
    fields = '__all__'
    template_name = 'document_form.html'

class DocumentUpdate(UpdateView):
    model = Document
    fields = '__all__'
    template_name = 'document_form.html'

class DocumentDelete(DeleteView):
    model = Document
    template_name = 'document_confurm_delete.html'
    success_url = reverse_lazy('courses')

class SubCreate(CreateView):
    model = Subscribe
    fields = '__all__'
    template_name = 'sub_form.html'

class SubUpdate(UpdateView):
    model = Subscribe
    fields = '__all__'
    template_name = 'sub_form.html'

class SubDelete(DeleteView):
    model = Subscribe
    template_name = 'sub_confurm_delete.html'
    success_url = reverse_lazy('subs')