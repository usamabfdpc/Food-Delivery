from django.urls import path
from .import views
urlpatterns = [
   path('',views.IndexView.as_view(),name='index'),
   path('category',views.AllCategory.as_view(),name='category'),
   path('category/add',views.MakeCategory.as_view(),name='add-category'),
   path('category/delete/<pk>',views.DeleteCategory.as_view(),name='delete-category'),
   path('category/update/<pk>',views.UpdateCategory.as_view(),name='update-category'),
]
