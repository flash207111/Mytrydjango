from django import forms
from .models import Courses


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'title',
        ]

    def clean_title(self, *args, **kwargs):      # Проверка валидации вводимых данных!!!!!
        title = self.cleaned_data.get('title')
        if 'abc' in title.lower():
            raise forms.ValidationError("This is not a valid title!")
        return title