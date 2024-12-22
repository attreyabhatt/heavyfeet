from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL ##auth.user
# Create your models here.

class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task_name = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    timestamp  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
