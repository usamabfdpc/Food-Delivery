from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import RecipeeCategory,Ingredients,ExtraIngredients
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DetailView,
    FormView,
    DeleteView,
)

# Create your views here.

class IndexView(TemplateView):
    template_name ='food_app/index.html'


class MakeCategory(CreateView):
    model = RecipeeCategory
    fields ="__all__"
    template_name = 'food_app/add-category.html'
    success_url =reverse_lazy('category')

    
    

class AllCategory(ListView):
    model = RecipeeCategory
    template_name ='food_app/categories.html'
    context_object_name ='categories' 
    paginate_by = 10
    

    def get_context_data(self, **kwargs):        
        query = self.request.GET.get('query')
        all_category = self.request.GET.get('all')
        active = self.request.GET.get('active')
        inactive = self.request.GET.get('inactive')
        context = super().get_context_data(**kwargs)
        context["query"] =query
        context["all"] =all_category
        context["active"] =active
        context["inactive"] =inactive
        return context

    
    def get_queryset(self) -> QuerySet[Any]:
        data =  super().get_queryset()
        query = self.request.GET.get('query')
        all_category = self.request.GET.get('all')
        active = self.request.GET.get('active')
        inactive = self.request.GET.get('inactive')
        category_name= self.request.GET.get('category_name')
        category_fee = self.request.GET.get('category_fee')
        category_status = self.request.GET.get('category_status')
        delete_all_category = self.request.POST.get('all_category')
        
        if query:
            data = RecipeeCategory.objects.filter(
                name__contains = query
            )        
        
        elif active:
            data = RecipeeCategory.objects.filter(status = True)

        elif inactive:
            data = RecipeeCategory.objects.filter(status = False)    
    
        elif all_category:
            data = RecipeeCategory.objects.all()

        elif category_name:
            data  = data.order_by('name')

        elif category_fee:
            data = data.order_by('packing_fee')  
        
        elif category_status:
            data = data.order_by('status')     
        
        else:
            data = data.order_by('id')

           
        
        if delete_all_category:
            data = RecipeeCategory.objects.all().delete()
        
        return data
    
    def post(self, request,*args,**kwargs) -> HttpResponse:
        delete_category = self.request.POST.getlist('category')
        if delete_category:
           data = RecipeeCategory.objects.filter(id__in=delete_category).delete()
        return HttpResponseRedirect(reverse_lazy('category'))  

        
       
    
        
    



class DeleteCategory(DeleteView):
    model = RecipeeCategory
    template_name ='food_app/delete-category.html'
    success_url = reverse_lazy('category')


class UpdateCategory(UpdateView):
    model = RecipeeCategory
    fields = '__all__'
    template_name ='food_app/update-category.html'
    success_url =reverse_lazy('category')

    

