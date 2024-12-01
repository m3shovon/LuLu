from django.db import models

class BudgetCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Expense(models.Model):
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"

class Budget(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
