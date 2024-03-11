from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Meta:
        verbose_name = "Task"
        order_with_respect_to = 'user'

    TASK_TYPE = [
        ('DA', 'Data'),
        ('DE', 'Development'),
        ('AD', 'Admin'),
    ]

    TASK_STATUS = [
        ('OP', 'Opened'),
        ('CL', 'Closed'),
        ('AB', 'Aborted'),
        ('PA', 'Paused'),
    ]

    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(max_length=255, 
                                   blank=True,
                                   verbose_name='Descripction')
    type = models.CharField(max_length=2, choices=TASK_TYPE, 
                                   default='DE',
                                   verbose_name='Type')
    status = models.CharField(max_length=2, choices=TASK_STATUS, 
                                   default='OP',
                                   verbose_name='Status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    start_date = models.DateField(verbose_name='Start date')    
    end_date = models.DateField(verbose_name='End date')    
    start_time = models.TimeField(verbose_name='Start time')    
    end_time = models.TimeField(verbose_name='End time')    


    def __str__(self):
        return f'{self.pk} - {self.name}:  {self.description}'
    
