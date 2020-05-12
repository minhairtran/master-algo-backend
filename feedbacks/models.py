from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def serialize(self): 
        return{
            "id": self.id,
            "content": self.content,
        }
