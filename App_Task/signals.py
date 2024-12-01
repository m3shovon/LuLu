from django.db.models.signals import pre_save
from django.dispatch import receiver
from App_Task.models import Task

@receiver(pre_save, sender=Task)
def update_task_status(sender, instance, **kwargs):
    if instance.pk:  
        old_task = Task.objects.get(pk=instance.pk)
        if old_task.status != instance.status:
            pass