from django.shortcuts import render, redirect
from .models import Expense, Budget, BudgetCategory
from .forms import ExpenseForm, BudgetForm, CategoryForm

def dashboard(request):
    expenses = Expense.objects.all()
    budgets = Budget.objects.all()
    total_expense = sum(exp.amount for exp in expenses)
    return render(request, 'App_Finance/dashboard.html', {'expenses': expenses, 'budgets': budgets, 'total_expense': total_expense})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'App_Finance/expense_form.html', {'form': form})

def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BudgetForm()
    return render(request, 'App_Finance/budget_form.html', {'form': form})
