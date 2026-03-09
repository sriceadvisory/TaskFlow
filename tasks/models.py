from django.conf import settings
from django.db import models

# Create your models here.

class Tasks(models.Model):
    class Meta:
        indexes = [
            models.Index(fields = ['title', 'completed', 'due_date'], name = 'task_index')
        ]

    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        )

    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    completed = models.BooleanField(default=False, db_index=True)
    priority = models.IntegerField(default=0)
    due_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    
