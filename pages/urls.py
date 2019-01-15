from django.urls import path

from . import views

"""
Class Way
path('', views.index, name='index'),
path('about/', views.about, name='about'),
"""

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]
