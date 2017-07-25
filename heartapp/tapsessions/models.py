from django.db import models

# Create your models here.
class Sequence(models.Model):
    created_at = models.DateTimeField('created at')
    
    def __str__(self):
        return self.created_at

class HeartBeat(models.Model):
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE, null=True)
    datetime_tapped = models.DateTimeField('datetime tapped')
    
    def __str__(self):
        return self.datetime_tapped
        