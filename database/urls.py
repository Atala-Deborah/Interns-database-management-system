from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Make this the root view
    path('add/', views.add_intern, name='add_intern'),
    path('edit/<int:pk>/', views.edit_intern, name='edit_intern'), 
    path('registry/', views.intern_registry, name='intern_registry'),
    path('delete/<int:id>/', views.delete_intern, name='delete_intern'),
    path('workshops/', views.workshops_view, name='workshops'),
    path('workshops/history/', views.past_workshops_view, name='workshop_history'),
    path('workshops/create/', views.create_workshop_view, name='create_workshop'),
    path('projects/', views.project_list, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('broadcast/new/', views.new_broadcast_view, name='new_broadcast'),
]
