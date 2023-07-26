from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DetailView,
    FormView,
    DeleteView,
)
from .forms import CustomUserCreationForm
from .models import Users
# Create your views here.
class Index(TemplateView):
    template_name = 'users/index.html'

class HomePage(TemplateView):
     template_name = "users/homepage.html"

class Registration(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    queryset = Users.objects.all()
    success_url = reverse_lazy('index')

    # def get_success_url(self) -> str:
    #     return reverse('index')
    
    def form_valid(self, form):
        return super().form_valid(form)