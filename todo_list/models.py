from django.db import models

# Create your models here.
class Todo(models.Model):
    is_complete_choices=(
        (True,'완료'),
        (False,'미완료')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_complete = models.BooleanField(default=False, choices=is_complete_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)