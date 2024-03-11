from django.urls import path
from .views import index, detail

app_name = 'jumia'

urlpatterns = [
    path('', index, name= 'index'),
    path('detail/<int:id>/', detail, name='detail'),

]