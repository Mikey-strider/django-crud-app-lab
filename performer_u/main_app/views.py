from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Instructor, Performer

class Home(LoginView):
    template_name = 'home.html'

class PerformerCreate(LoginRequiredMixin, CreateView):
    model = Performer
    fields = ['performer_name', 'performerance_type', 'performer_description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PerformerUpdate(LoginRequiredMixin, UpdateView):
    model = Performer
    fields = ['performer_name', 'performerance_type', 'performer_description']

class PerformerDelete(LoginRequiredMixin, DeleteView):
    model = Performer
    success_url = '/perormers/'


class InstructorCreate(LoginRequiredMixin, CreateView):
    form_class = InstructorForm
    model = Instructor

class InstructorList(LoginRequiredMixin, ListView):
    model = Instructor


class InstructorDetail(LoginRequiredMixin, DetailView):
    model = Instructor


class InstructorUpdate(LoginRequiredMixin, UpdateView):
    form_class = InstructorForm
    model = Instructor


class InstructorDelete(LoginRequiredMixin, DeleteView):
    model = Instructor
    success_url = '/instructors/'


def about(request):
    return render(request, 'about.html')


@login_required
def performer_index(request):
    performers = Performer.objects.all()
    return render(request, 'performers/index.html', {'performers': performers})


@login_required
def performer_detail(request, performer_id):
    performer = Performer.objects.get(id=performer_id):
    instructors_not_in_performer = Instructor.objects.exclude(id_in = performer.instructor.all().values_list('id'))
    return render(request, 'performers/performer_details.html', {'performer': performer, 'instructors': instructors_not_in_perofmer})


@login_required
def associate_instructor(request, performer_id, instructor_id):
    Performer.objects.get(id=performer_id).instructors.add(instructor_id)
    return redirect('performer-detail', performer_id=performer_id)


@login_required
def remove_instructor(request, performer_id, instructor_id):
    Performer.objects.get(id=performer_id).instructors.remove(instructor_id)
    return redirect('performer-detail', performer_id=performer_id)




def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('performer-index')
        else:
            error_message = 'Invalid sign up - try again'
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'signup.html', context)
