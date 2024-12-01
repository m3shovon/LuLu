from django.contrib import admin

# Register your models here.
from App_Finance import models

admin.site.register(models.BudgetCategory)
admin.site.register(models.Expense)
admin.site.register(models.Budget)