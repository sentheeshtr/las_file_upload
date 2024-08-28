from django.db import models

class LasFile(models.Model):
    file = models.FileField(upload_to='las_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
