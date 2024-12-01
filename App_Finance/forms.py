from django import forms
from .models import Expense, Budget, BudgetCategory

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'amount']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['name']
