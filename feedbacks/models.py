from django.db import models

# Create your models here.


class Feedback(models.Model):
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return{
            "id": self.id,
            "content": self.content,
        }
