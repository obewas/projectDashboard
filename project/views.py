from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from django.urls import reverse_lazy
import openpyxl
from django.http import HttpResponse
# Create your views here.
# views.py


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = '__all__'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = "__all__"
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

def export_projects_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Projects"

    # Header row
    headers = ['Name', 'Status', 'Start Date', 'End Date','Completion %']
    ws.append(headers)

    # Data rows
    for project in Project.objects.all():
        ws.append([
            project.project_name,
            project.get_status_display(),
            project.start_date.strftime('%Y-%m-%d'),
            project.end_date.strftime('%Y-%m-%d'),
            project.completion_rate,
        ])

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=projects.xlsx'
    wb.save(response)
    return response
