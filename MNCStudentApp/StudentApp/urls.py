from django.urls import path
from . import views

urlpatterns = [
path('', views.student_list, name='student_list'),
path('login/', views.login_view, name='login'),
path('student_list/', views.student_list, name='student_list'),
]