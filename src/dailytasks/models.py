from django.db import models

# Create your models here.

class UserTask(models.Model):
    task_name = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
