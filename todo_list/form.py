from django import forms
from todo_list.models import Todo


class TodoUpdateForm(forms.ModelForm):
    is_complete = forms.BooleanField(required=False, label="Complete")  # 필드 추가

    class Meta:
        model = Todo
        fields = ('title', 'description', 'start_date', 'end_date', 'is_complete')  # 필드 추가
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # 추가된 키워드 인자를 처리
        is_update = kwargs.pop('is_update', False)  # 'is_update' 키워드 추출
        super().__init__(*args, **kwargs)  # 부모 클래스의 __init__ 호출

        # 'is_update'가 False라면 'is_complete' 필드 제거
        if not is_update:
            self.fields.pop('is_complete')
