from django.db import models

# Create your models here.
class workExperiences(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date =  models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    current_job = models.BooleanField()

    # add image of the companies logo eventually

    job_description = models.TextField()

    def __str__(self):
        return self.job_title

class Bio(models.Model):
    title = models.CharField(max_length=200)
    current_job = models.CharField(max_length=200)
    current_company = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title