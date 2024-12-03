from tkinter import Widget
from django import forms
from django.core.exceptions import ValidationError
from App_Task.models import Task, Project, Notes
from App_Auth.models import CustomerProfile
# from django.contrib.admin.widgets import AdminDateWidget
from tempus_dominus.widgets import DateTimePicker
from django.forms import DateInput, DateTimeInput


class ProjectForm(forms.ModelForm):
    # start_date = forms.DateField(widget=AdminDateWidget)
    # start_date = forms.DateTimeField(widget=DateTimePicker)
    class Meta:
        model = Project
        fields = ('name', 'start_date', 'end_date', 'assigned_to')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'end_date': DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            # 'start_date': DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            # 'end_date': DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            }
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ('__all__')
        exclude = ('completed_by',)
        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'end_date': DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            }
        
  
# class AssignTaskForm(forms.Form):
#     employees = forms.ModelMultipleChoiceField(
#         queryset=CustomerProfile.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         label='Employees'
#     )

#     def __init__(self, *args, **kwargs):
#         self.task = kwargs.pop('task')
#         super().__init__(*args, **kwargs)

#     def clean(self):
#         cleaned_data = super().clean()
#         employees = cleaned_data.get('employees')
#         if not employees:
#             raise ValidationError('You must select at least one employee')
#         for employee in employees:
#             if employee in self.task.employees.all():
#                 raise ValidationError(f'{employee} is already assigned to this task')
#         return cleaned_data


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
