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

class RiskField(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('decimal', 'Decimal'),
        ('boolean', 'Boolean'),
        ('option', 'Option'),
        ('date', 'Date'),
    )
    risk_type = models.ForeignKey(
        RiskType, related_name='risk_fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPES)
    required = models.BooleanField(default=True)

    def __str__(self):
        return 'Risk Field: %s, Risk Type: %s' % (self.name, self.risk_type)
		

class FieldOption(models.Model):
    risk_field = models.ForeignKey(
        RiskField, related_name='field_options', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return 'Risk Option: %s, Risk Field: %s' % (self.content, self.risk_field)
