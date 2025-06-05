# urls.py
from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView,
    ProjectCreateView, ProjectUpdateView, ProjectDeleteView
)
from .views import export_projects_excel

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/export/', export_projects_excel, name='export_projects_excel'),
]

