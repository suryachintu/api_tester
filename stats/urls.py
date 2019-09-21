from django.urls import path

from stats import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_test_case', views.add_test_case, name='add_test_case'),
]
