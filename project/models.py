from django.db import models

# Create your models here.
project_status = (
    
)
class Project(models.Model):
    STATUS_CHOICES = [
        ('On Track','on_track' ),
        ('Complete','complete'),
        ('At Risk','at_risk'),
        ('Delayed','delayed' ),
    ]
    project_name = models.CharField(max_length=250)
    objective = models.TextField()
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    completion_rate = models.FloatField()
    budget = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='on_track')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
    
    def duration_in_days(self):
        return (self.end_date - self.start_date).days
    
