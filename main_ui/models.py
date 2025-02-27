from django.db import models

# Create your models here.
class Issue(models.Model):
    issue_type = models.CharField(max_length=120)
    issue_desc = models.CharField(max_length=300)
    # assignee = FOREIGNKEY_REFERENCING USERS
    # raiser = FOREIGNKEY_REFERENCING USERS (OPTIONAL field)
    # date_raised = DATE_FIELD
    # last_update = DATE_FIELD
    # img = LOOK_HOW_TO_STORE_IMAGES (OPTIONAL field)
    resolved = models.BooleanField(default=False)
    location_lat = models.FloatField()
    location_long = models.FloatField()