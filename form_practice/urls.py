from django.urls import path
from . import views

# Reserved key word for django
urlpatterns = [
    # name should be the same as function name in views
    path('', views.index, name='index')
]