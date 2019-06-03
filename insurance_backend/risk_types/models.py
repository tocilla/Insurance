from django.db import models

# Create your models here.


class RiskType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return 'Risk Type: %s' % (self.name)