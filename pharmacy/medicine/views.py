from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Medicine
from .forms import StudentForm, CourseForm, EnrollmentForm

# Create your views here.
def dashboard(request):
    context = {
        'total_medicines':  Medicine.objects.count(),
    }
    return render(request, 'dashboard.html', context)
