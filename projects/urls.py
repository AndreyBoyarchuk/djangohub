from django.urls import path
from . import views
urlpatterns = [

    path('project/<str:pk>/', views.project),
    path('projects/', views.projects),
    path('about/', views.about),
    path('', views.frontpage),
]
