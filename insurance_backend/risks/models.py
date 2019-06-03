from django.db import models
from risk_types.models import RiskType, RiskField

# Create your models here.


class Risk(models.Model):
    name = models.CharField(max_length=100, unique=True)
    risk_type = models.ForeignKey(
        RiskType, related_name='risks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return 'Risk: %s, Risk Type: %s' % (self.name, self.risk_type)