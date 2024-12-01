from django.contrib import admin

# Register your models here.
from App_Task import models

admin.site.register(models.Type)
admin.site.register(models.Label)
admin.site.register(models.Project)
admin.site.register(models.Task)
admin.site.register(models.Notes)
