from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
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
    paginate_by = 5
    

    def get_context_data(self, **kwargs):        
        query = self.request.GET.get('query')
        context = super().get_context_data(**kwargs)
        context["query"] =query
        return context

    def get_queryset(self) -> QuerySet[Any]:
        data =  super().get_queryset()
        query = self.request.GET.get('query')
        all_category = self.request.GET.get('all')
        active = self.request.GET.get('active')
        inactive = self.request.GET.get('inactive')
        category_name= self.request.GET.get('category_name')
        category_fee = self.request.GET.get('category_fee')
        category_id = self.request.GET.get('category_id')
        delete_category = self.request.GET.getlist('category')
        delete_all_category = self.request.GET.get('all_category')
        if query:
            data = RecipeeCategory.objects.filter(
                name__contains = query
            )
        if all_category:
                data = RecipeeCategory.objects.all()
        
        if active:
            data = RecipeeCategory.objects.filter(status = True)

        if inactive:
            data = RecipeeCategory.objects.filter(status = False)    
    
        if category_name:
            data  = data.order_by('name')

        if category_fee:
            data = data.order_by('packing_fee')  
        
        if category_id:
            data = data.order_by('id')      
            return data  

        if delete_category:
           data = RecipeeCategory.objects.filter(id__in=delete_category).delete()

        if delete_all_category:
            data = RecipeeCategory.objects.all().delete()
        return data
    



class DeleteCategory(DeleteView):
    model = RecipeeCategory
    template_name ='food_app/delete-category.html'
    success_url = reverse_lazy('category')


class UpdateCategory(UpdateView):
    model = RecipeeCategory
    fields = '__all__'
    template_name ='food_app/update-category.html'
    success_url =reverse_lazy('category')

    

