from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('add-crud/', add),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),

    path('update-func/<int:id>', updateFunc),

    


]
