from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model): 
    TA_CHOICES = [
        ('TA100-70020', 'TA100-70020'),
        ('TA100-11050', 'TA100-11050'),
        ('TA100-11051', 'TA100-11051'),
        ('TA100-11052', 'TA100-11052'),
        ('TA100-11053', 'TA100-11053'),
        ('TA100-11054', 'TA100-11054'),
        ('TA100-11055', 'TA100-11055'),
        ('TA100-11056', 'TA100-11056'),
        ('TA100-11057', 'TA100-11057'),
        ('TA100-11058', 'TA100-11058'),
    ]
    
    name = models.CharField(
        max_length=15,
        choices=TA_CHOICES,
        default='TA100-70020',
    )
    status_choices = [
        ('RUNNING', 'Running'),
        ('STOPPED', 'Stopped'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='STOPPED')

    def __str__(self):
        return self.name


class PDFFile(models.Model):
    pdf_duration = models.IntegerField(default=20,help_text="Duration of pdf in seconds")
    pdf_name = models.CharField(max_length=100,default='TA100-70020' ,help_text="Name of PDF file")
    pdf_file = models.FileField(upload_to='static/media/Pdf_files/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pdf_name

class VideoFile(models.Model):
    video_duration = models.IntegerField(default=20,help_text="Duration of video in seconds")
    video_name = models.CharField(max_length=100,default='TA100-70020' ,help_text="Name of Media file")
    video_file = models.FileField(upload_to='static/media/Videos_files/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.video_name

class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    upload_pdf = models.ManyToManyField(PDFFile, blank=True)
    upload_video = models.ManyToManyField(VideoFile, blank=True)

    def __str__(self):
        return f"Screen {self.screen_id} at {self.manager} for {self.product}"
    
