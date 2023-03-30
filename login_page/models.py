from django.db import models

class PDFZipFile(models.Model):
    zip_file = models.FileField(upload_to='media/')

    class Meta:
        app_label = 'login_page'

    def __str__(self):
        return self.zip_file.name