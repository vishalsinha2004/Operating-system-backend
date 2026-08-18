from django.db import models

class SystemApp(models.Model):
    app_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    
    # Changed to ImageField to create the file upload button
    icon = models.ImageField(upload_to='icons/') 
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name