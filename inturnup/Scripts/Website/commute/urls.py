from django.urls import path
from . import views

urlpatterns = [
    path('click/', views.commute_record, name='post_commute'),
]
