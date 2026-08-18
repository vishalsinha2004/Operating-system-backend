from django.db import models

class SystemApp(models.Model):
    app_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/') 
    
    # --- NEW FIELDS FOR PROJECT DETAILS ---
    description = models.TextField(blank=True, null=True, help_text="Project overview")
    tech_stack = models.CharField(max_length=255, blank=True, null=True)
    frontend_repo = models.URLField(blank=True, null=True, help_text="GitHub Frontend Link")
    backend_repo = models.URLField(blank=True, null=True, help_text="GitHub Backend Link")
    live_link = models.URLField(blank=True, null=True, help_text="Live Hosted URL")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name