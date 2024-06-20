from django.db import models


# Create your models here.
class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)

    linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    is_demo_lead = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    n_employees = models.FloatField(blank=True, null=True)
    raw_json = models.JSONField(default=dict)
    company_name_linkedin = models.CharField(max_length=255, blank=True, null=True)
    urn = models.IntegerField(blank=True, null=True)
    campaign_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "lead"
