from django.urls import path
from .views import blog

app_name = 'Blog'

urlpatterns = [
    path('', blog, name='BlogIndex'),
]