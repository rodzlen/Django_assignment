from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.
class Todo(models.Model):
    is_complete_choices=(
        (True,'완료'),
        (False,'미완료')
    )
    title = models.CharField('제목',max_length=50)
    description = models.TextField('내용')
    start_date = models.DateField('시작일자',null=True)
    end_date = models.DateField('마감일자',null=True)
    is_complete = models.BooleanField('완료여부', default=False, choices=is_complete_choices)
    created_at = models.DateTimeField('작성일자',auto_now_add=True)
    modified_at = models.DateTimeField('수정일자',auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)