from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'photo'