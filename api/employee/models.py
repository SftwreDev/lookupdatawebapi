from django.db import models


# Create your models here.
class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    raw_json = models.JSONField(default=dict)
    urn = models.IntegerField(blank=True, null=True)
    lead_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "employee"
